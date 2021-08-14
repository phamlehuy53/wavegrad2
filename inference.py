from lightning_model import Wavegrad2
from omegaconf import OmegaConf as OC
import os
import argparse
import datetime
from glob import glob
import torch
import librosa as rosa
from scipy.io.wavfile import write as swrite
import matplotlib.pyplot as plt
from utils.stft import STFTMag
import numpy as np
from g2p_en import G2p
from pypinyin import pinyin, Style
import re

from dataloader import TextAudioDataset


def save_stft_mag(wav, fname):
    fig = plt.figure(figsize=(9, 3))
    plt.imshow(rosa.amplitude_to_db(stft(wav[0].detach().cpu()).numpy(),
               ref=np.max, top_db = 80.),
               aspect='auto',
               origin='lower',
               interpolation='none')
    plt.colorbar()
    plt.xlabel('Frames')
    plt.ylabel('Channels')
    plt.tight_layout()
    fig.savefig(fname, format='png')
    plt.close()
    return

def read_lexicon(lex_path):
    lexicon = {}
    with open(lex_path) as f:
        for line in f:
            temp = re.split(r"\s+", line.strip("\n"))
            word = temp[0]
            phones = temp[1:]
            if word.lower() not in lexicon:
                lexicon[word.lower()] = phones
    return lexicon

def preprocess_eng(hparams, text):
    lexicon = read_lexicon(hparams.data.lexicon_path)

    g2p = G2p()
    phones = []
    words = re.split(r"([,;.\-\?\!\s+])", text)
    for w in words:
        if w.lower() in lexicon:
            phones += lexicon[w.lower()]
        else:
            phones += list(filter(lambda p: p != " ", g2p(w)))
    phones = "{" + "}{".join(phones) + "}"
    phones = re.sub(r"\{[^\w\s]?\}", "{sp}", phones)
    print('g2p: ', phones)

    trainset = TextAudioDataset(hparams, hparams.data.train_dir, hparams.data.train_meta, train=False)

    text = trainset.get_text(phones)
    text = text.unsqueeze(0)
    return text


def preprocess_vie(hparams, text):
    lexicon = read_lexicon(hparams.data.lexicon_path)

    phones = []
    words = re.split(r"([,;.\-\?\!\s+])", text)
    for w in words:
        if w.lower() in lexicon:
            phones += lexicon[w.lower()]
        else:
            print(f"Phone not found {w}")
            pass
    phones = "{" + "}{".join(phones) + "}"
    phones = re.sub(r"\{[^\w\s]?\}", "{sp}", phones)
    print('g2p: ', phones)

    trainset = TextAudioDataset(hparams, hparams.data.train_dir, hparams.data.train_meta, train=False)

    text = trainset.get_text(phones)
    text = text.unsqueeze(0)
    return text

def preprocess_mandarin(hparams, text):
    lexicon = read_lexicon(hparams.data.lexicon_path)

    phones = []
    pinyins = [
        p[0]
        for p in pinyin(
            text, style=Style.TONE3, strict=False, neutral_tone_with_five=True
        )
    ]
    for p in pinyins:
        if p in lexicon:
            phones += lexicon[p]
        else:
            phones.append("sp")

    phones = "{" + " ".join(phones) + "}"
    print('g2p: ', phones)

    trainset = TextAudioDataset(hparams, hparams.data.train_dir, hparams.data.train_meta, train=False)

    text = trainset.get_text(phones)
    text = text.unsqueeze(0)

    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--checkpoint',
                        type=str,
                        required=True,
                        help="Checkpoint path")
    parser.add_argument('--text',
                        type=str,
                        default=None,
                        help="raw text to synthesize, for single-sentence mode only")
    parser.add_argument('--speaker',
                        type=str,
                        default='LJSpeech',
                        help="speaker name")
    parser.add_argument('--pace',
                        type=int,
                        default=1.0,
                        help="control the pace of the whole utterance")
    parser.add_argument('--steps',
                        type=int,
                        required=False,
                        help="Steps for sampling")
    parser.add_argument('--device',
                        type=str,
                        default='cuda',
                        required=False,
                        help="Device, 'cuda' or 'cpu'")

    args = parser.parse_args()
    #torch.backends.cudnn.benchmark = False
    hparams = OC.load('hparameter.yaml')
    os.makedirs(hparams.log.test_result_dir, exist_ok=True)
    if args.steps is not None:
        hparams.ddpm.max_step = args.steps
        if args.steps == 8:
            hparams.ddpm.noise_schedule = \
                "torch.tensor([1e-6,2e-6,1e-5,1e-4,1e-3,1e-2,1e-1,9e-1])"
    else:
        args.steps = hparams.ddpm.max_step
    model = Wavegrad2(hparams).to(args.device)
    stft = STFTMag()
    ckpt = torch.load(args.checkpoint, map_location='cpu')
    model.load_state_dict(ckpt['state_dict'] if not('EMA' in args.checkpoint) else ckpt)
    if hparams.data.lang == 'eng':
        text = preprocess_eng(hparams, args.text)
    if hparams.data.lang == 'vie':
        text = preprocess_vie(hparams, args.text)

    speaker_dict = {spk: idx for idx, spk in enumerate(hparams.data.speakers)}
    spk_id = [speaker_dict[args.speaker]]
    spk_id = torch.LongTensor(spk_id)

    text = text.cuda()
    spk_id = spk_id.cuda()

    wav_recon, align, *_ = model.inference(text, spk_id, pace=args.pace)

    save_stft_mag(wav_recon, os.path.join(hparams.log.test_result_dir, f'{args.text}.png'))
    swrite(os.path.join(hparams.log.test_result_dir, f'{args.text}.wav'),
           hparams.audio.sampling_rate, wav_recon[0].detach().cpu().numpy())

