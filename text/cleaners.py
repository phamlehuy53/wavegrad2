#This code is from
#https://github.com/keithito/tacotron

'''
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
  1. "english_cleaners" for English text
  2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
'''

import re
from unidecode import unidecode
from unicodedata import normalize
from pypinyin import pinyin, Style
from .numbers import normalize_numbers


# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')

# List of (regular expression, replacement) pairs for abbreviations:
_abbreviations = [(re.compile('\\b%s\\.' % x[0], re.IGNORECASE), x[1]) for x in [
  ('mrs', 'misess'),
  ('mr', 'mister'),
  ('dr', 'doctor'),
  ('st', 'saint'),
  ('co', 'company'),
  ('jr', 'junior'),
  ('maj', 'major'),
  ('gen', 'general'),
  ('drs', 'doctors'),
  ('rev', 'reverend'),
  ('lt', 'lieutenant'),
  ('hon', 'honorable'),
  ('sgt', 'sergeant'),
  ('capt', 'captain'),
  ('esq', 'esquire'),
  ('ltd', 'limited'),
  ('col', 'colonel'),
  ('ft', 'fort'),
]]

_cht_norm = [(re.compile(r'[%s]' % x[0]), x[1]) for x in [
  ('。．；', '.'),
  ('，、', ', '),
  ('？', '?'),
  ('！', '!'),
  ('─‧', '-'),
  ('…', '...'),
  ('《》「」『』〈〉（）', "'"),
  ('：︰', ':'),
  ('　', ' ')
]]

def expand_abbreviations(text):
  for regex, replacement in _abbreviations:
    text = re.sub(regex, replacement, text)
  return text


def expand_numbers(text):
  return normalize_numbers(text)


def lowercase(text):
  return text.lower()


def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)


def convert_to_ascii(text):
  return unidecode(text)


def basic_cleaners(text):
  '''Basic pipeline that lowercases and collapses whitespace without transliteration.'''
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def transliteration_cleaners(text):
  '''Pipeline for non-English text that transliterates to ASCII.'''
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def english_cleaners(text):
  '''Pipeline for English text, including number and abbreviation expansion.'''
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = expand_numbers(text)
  text = expand_abbreviations(text)
  text = collapse_whitespace(text)
  return text

def korean_cleaners(text, for_dict=None, dictionary=None):
  '''Pipeline for Korean text, including collapses whitespace.'''
  text = collapse_whitespace(text)
  text = normalize('NFKD', text)
  return text


def chinese_cleaners(text):
  '''Pipeline for Chinese text, including collapses whitespace.'''
  for regex, replacement in _cht_norm:
    text = re.sub(regex, replacement, text)
  text = collapse_whitespace(text)
  text = text.strip()
  text = [
    p[0] for p in pinyin(
      text, style=Style.TONE3, strict=False, neutral_tone_with_five=True
    )
  ]
  text = "".join(text)
  return text

def japanese_romaji_cleaners(text):
  '''Pipeline for Japanese text, including collapses whitespace.'''
  text = collapse_whitespace(text)
  return text

def japanese_cleaners(text):
    return japanese_romaji_cleaners(text)

def japanese_kana_cleaners(text):
  '''Pipeline for Japanese text, including collapses whitespace.'''
  text = collapse_whitespace(text)
  return text
def vietnamese_cleaners(text):
    # TODO: What punctuations is needed
    # text = re.sub('['+punctuation+']', ' ', text) #
    text = lowercase(text)
    # text = expand_numbers(text) # TODO: expand vietnamese numbers

    # TODO:Need abbreviation for vietnamese
    # text = expand_abbreviations(text)
    text = collapse_whitespace(text)
    text = text.strip()
    return text