#This code is adopted from
#https://github.com/keithito/tacotron
from . import cmudict

_pad = '<pad>'
_punc = list('!\'(),-.:~? ')
_SILENCES = ['sp', 'spn', 'sil']
_eng_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

# arpabet WITH stress
# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

_a_silences = ['@' + s for s in _SILENCES]

# arpabet WITHOUT stress
_cmu_characters = [
    'AA', 'AE', 'AH',
    'AO', 'AW', 'AY',
    'B', 'CH', 'D', 'DH', 'EH', 'ER', 'EY',
    'F', 'G', 'HH', 'IH', 'IY',
    'JH', 'K', 'L', 'M', 'N', 'NG', 'OW', 'OY',
    'P', 'R', 'S', 'SH', 'T', 'TH', 'UH', 'UW',
    'V', 'W', 'Y', 'Z', 'ZH'
]
_cmu_characters = ['@' + s for s in _cmu_characters]

# Korean jamo
_jamo_leads = "".join([chr(_) for _ in range(0x1100, 0x1113)])
_jamo_vowels = "".join([chr(_) for _ in range(0x1161, 0x1176)])
_jamo_tails = "".join([chr(_) for _ in range(0x11A8, 0x11C3)])
_jamo_trashes = "".join([chr(_) for _ in range(0x11C4, 0x1215)])
_kor_characters = list(_jamo_leads + _jamo_vowels + _jamo_tails)

# Characters to represent Chinese
_cht_characters = list('abcdefghijklmnopqrstuvwxyz12345')

# Japanese characters
_jap_romaji_characters = [
     'N', 'a', 'b', 'by', 'ch', 'cl', 'd', 'dy', 'e', 'f', 'g',
     'gy', 'h', 'hy', 'i', 'j', 'k', 'ky', 'm', 'my', 'n', 'ny',
     'o', 'p', 'pau', 'py', 'r', 'ry', 's', 'sh', 't', 'ts', 'u',
     'v', 'w', 'y', 'z'
]

_jap_kana_characters = [
     '、',
     'ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お',
     'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご',
     'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ',
     'た', 'だ', 'ち', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど',
     'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び',
     'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ',
     'ま', 'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ',
     'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'ゔ',
     'ー'
]

## English
# eng, eng2 (use arpabet WITH stress)
eng_symbols = [_pad] + _eng_characters + _punc + _arpabet + _a_silences
# cmu (use arpabet WITHOUT stress)
cmu_symbols = [_pad] + _eng_characters + _punc + _cmu_characters + _a_silences

## Korean
# kor
kor_symbols = [_pad] + _kor_characters + _punc + _SILENCES + list(_jamo_trashes)

# Chinese
# cht
cht_symbols = [_pad] + _cht_characters + _punc

# Japanese
# jap, jap_romaji
jap_romaji_symbols = [_pad] + _jap_romaji_characters + _punc
# jap_kana
jap_kana_symbols = [_pad] + _jap_kana_characters + _punc

# vie
_punctuation = '  !"\'(),-.:;?[]{}'
_vie_phones = ['a', 'ai', 'am', 'an', 'ang', 'anh', 'ao', 'au', 'ay', 'b', 'c', 'ch', 'd', 'e', 'em', 'en', 'eng', 'enh', 'eo', 'f', 'g', 'gh', 'gi', 'h', 'i', 'ia', 'im', 'in', 'ing', 'inh', 'iu', 'iê', 'iêm', 'iên', 'iêng', 'iêu', 'iế', 'iếc', 'iếm', 'iến', 'iếng', 'iếp', 'iết', 'iếu', 'iề', 'iềm', 'iền', 'iềng', 'iều', 'iể', 'iểm', 'iển', 'iểng', 'iểu', 'iễ', 'iễm', 'iễn', 'iễng', 'iễu', 'iệ', 'iệc', 'iệm', 'iện', 'iệng', 'iệp', 'iệt', 'iệu', 'k', 'kh', 'kw', 'l', 'm', 'n', 'ng', 'ngh', 'nh', 'o', 'oa', 'oai', 'oam', 'oan', 'oang', 'oanh', 'oay', 'oe', 'oem', 'oen', 'oeng', 'oeo', 'oi', 'om', 'on', 'ong', 'oo', 'ooc', 'oom', 'oon', 'oong', 'oà', 'oài', 'oàm', 'oàn', 'oàng', 'oành', 'oày', 'oá', 'oác', 'oách', 'oái', 'oán', 'oáng', 'oánh', 'oáp', 'oát', 'oáy', 'oã', 'oãi', 'oãn', 'oãng', 'oãy', 'oè', 'oèn', 'oèo', 'oé', 'oéc', 'oém', 'oén', 'oét', 'oò', 'oòn', 'oòng', 'oó', 'oóc', 'oón', 'oóng', 'oõ', 'oă', 'oăm', 'oăn', 'oăng', 'oạ', 'oạc', 'oạch', 'oại', 'oạm', 'oạn', 'oạng', 'oạnh', 'oạp', 'oạt', 'oạy', 'oả', 'oải', 'oảm', 'oản', 'oảng', 'oảnh', 'oảy', 'oắ', 'oắc', 'oắm', 'oắn', 'oắng', 'oắt', 'oằ', 'oằm', 'oằn', 'oằng', 'oẳ', 'oẳn', 'oẳng', 'oẵ', 'oẵn', 'oẵng', 'oặ', 'oặc', 'oặm', 'oặn', 'oặt', 'oẹ', 'oẹt', 'oẻ', 'oẻm', 'oẻn', 'oẻng', 'oẻo', 'oẽ', 'oẽo', 'oọ', 'oọc', 'oọn', 'oọng', 'oỏ', 'p', 'ph', 'q', 'r', 's', 'sh', 't', 'th', 'tr', 'u', 'ua', 'ui', 'um', 'un', 'ung', 'uyu', 'uỷu', 'uỳu', 'uýu', 'uỹu', 'uy', 'uyn', 'uynh', 'uyê', 'uyên', 'uyế', 'uyếc', 'uyến', 'uyết', 'uyề', 'uyền', 'uyể', 'uyển', 'uyễ', 'uyễn', 'uyệ', 'uyện', 'uyệt', 'uâ', 'uân', 'uâng', 'uây', 'uầy', 'uấy', 'uẩy', 'uẫy', 'uậy', 'uê', 'uên', 'uênh', 'uô', 'uôc', 'uôi', 'uội', 'uôm', 'uôn', 'uông', 'uý', 'uých', 'uýn', 'uýnh', 'uýp', 'uýt', 'uơ', 'uơn', 'uơng', 'uấ', 'uấc', 'uấn', 'uất', 'uầ', 'uần', 'uầng', 'uẩ', 'uẩn', 'uẩng', 'uẫ', 'uẫn', 'uậ', 'uận', 'uật', 'uế', 'uếc', 'uếch', 'uến', 'uếnh', 'uết', 'uề', 'uền', 'uềnh', 'uể', 'uển', 'uểnh', 'uễ', 'uệ', 'uệc', 'uệch', 'uện', 'uệnh', 'uệt', 'uố', 'uốc', 'uối', 'uốm', 'uốn', 'uống', 'uốt', 'uồ', 'uồi', 'uồm', 'uồn', 'uồng', 'uổ', 'uổc', 'uổi', 'uổn', 'uổng', 'uỗ', 'uỗi', 'uỗm', 'uỗn', 'uỗng', 'uộ', 'uộc', 'uộm', 'uộn', 'uộng', 'uột', 'uớ', 'uớt', 'uờ', 'uờn', 'uờng', 'uở', 'uởn', 'uởng', 'uỡ', 'uỡn', 'uợ', 'uỳ', 'uỳn', 'uỳnh', 'uỵ', 'uỵc', 'uỵch', 'uỵp', 'uỵt', 'uỷ', 'uỷn', 'uỷnh', 'uỹ', 'v', 'w', 'x', 'y', 'ym', 'yn', 'ynh', 'yê', 'yêm', 'yên', 'yế', 'yếc', 'yếm', 'yến', 'yết', 'yề', 'yền', 'yể', 'yểm', 'yển', 'yễ', 'yễn', 'yệ', 'yện', 'yệt', 'z', 'à', 'ài', 'àm', 'àn', 'àng', 'ành', 'ào', 'àu', 'ày', 'á', 'ác', 'ách', 'ái', 'ám', 'án', 'áng', 'ánh', 'áo', 'áp', 'át', 'áu', 'áy', 'â', 'âm', 'ân', 'âng', 'âp', 'âu', 'ây', 'ã', 'ãi', 'ãm', 'ãn', 'ãng', 'ãnh', 'ão', 'ãu', 'ãy', 'è', 'èm', 'èn', 'èng', 'èo', 'é', 'éc', 'ém', 'én', 'éng', 'éo', 'ép', 'ét', 'ê', 'êm', 'ên', 'êng', 'ênh', 'êu', 'ì', 'ìa', 'ìm', 'ìn', 'ình', 'ìu', 'í', 'ía', 'íc', 'ích', 'ím', 'ín', 'ính', 'íp', 'ít', 'íu', 'ò', 'òa', 'òe', 'òi', 'òm', 'òn', 'òng', 'ó', 'óa', 'óc', 'óe', 'ói', 'óm', 'ón', 'óng', 'óp', 'ót', 'ô', 'ôi', 'ôm', 'ôn', 'ông', 'õ', 'õa', 'õe', 'õi', 'õm', 'õn', 'õng', 'ù', 'ùa', 'ùi', 'ùm', 'ùn', 'ùng', 'ùy', 'ú', 'úa', 'úc', 'úi', 'úm', 'ún', 'úng', 'úp', 'út', 'úy', 'ý', 'ých', 'ýn', 'ýnh', 'ýp', 'ýt', 'ă', 'ăm', 'ăn', 'ăng', 'đ', 'ĩ', 'ĩa', 'ĩm', 'ĩn', 'ĩnh', 'ĩu', 'ũ', 'ũa', 'ũi', 'ũm', 'ũn', 'ũng', 'ũy', 'ơ', 'ơi', 'ơm', 'ơn', 'ơng', 'ơt', 'ư', 'ưa', 'ưi', 'ưn', 'ưng', 'ươ', 'ươi', 'ươm', 'ươn', 'ương', 'ướ', 'ước', 'ưới', 'ướm', 'ướn', 'ướng', 'ướp', 'ướt', 'ươu', 'ườu', 'ướu', 'ưởu', 'ưỡu', 'ượu', 'ườ', 'ười', 'ườm', 'ườn', 'ường', 'ưở', 'ưởi', 'ưởn', 'ưởng', 'ưỡ', 'ưỡi', 'ưỡn', 'ưỡng', 'ượ', 'ược', 'ượi', 'ượm', 'ượn', 'ượng', 'ượp', 'ượt', 'ạ', 'ạc', 'ạch', 'ại', 'ạm', 'ạn', 'ạng', 'ạnh', 'ạo', 'ạp', 'ạt', 'ạu', 'ạy', 'ả', 'ảc', 'ảch', 'ải', 'ảm', 'ản', 'ảng', 'ảnh', 'ảo', 'ảu', 'ảy', 'ấ', 'ấc', 'ấm', 'ấn', 'ấng', 'ấp', 'ất', 'ấu', 'ấy', 'ầ', 'ầm', 'ần', 'ầng', 'ầu', 'ầy', 'ẩ', 'ẩm', 'ẩn', 'ẩng', 'ẩu', 'ẩy', 'ẫ', 'ẫm', 'ẫn', 'ẫng', 'ẫu', 'ẫy', 'ậ', 'ậc', 'ậm', 'ận', 'ậng', 'ập', 'ật', 'ậu', 'ậy', 'ắ', 'ắc', 'ắm', 'ắn', 'ắng', 'ắp', 'ắt', 'ằ', 'ằm', 'ằn', 'ằng', 'ẳ', 'ẳm', 'ẳn', 'ẳng', 'ẵ', 'ẵm', 'ẵn', 'ẵng', 'ẵp', 'ặ', 'ặc', 'ặm', 'ặn', 'ặng', 'ặp', 'ặt', 'ẹ', 'ẹc', 'ẹm', 'ẹn', 'ẹo', 'ẹp', 'ẹt', 'ẹy', 'ẻ', 'ẻm', 'ẻn', 'ẻng', 'ẻo', 'ẽ', 'ẽm', 'ẽn', 'ẽo', 'ế', 'ếc', 'ếch', 'ếm', 'ến', 'ếng', 'ếnh', 'ếp', 'ết', 'ếu', 'ề', 'ềm', 'ền', 'ềng', 'ềnh', 'ều', 'ể', 'ểm', 'ển', 'ểng', 'ểnh', 'ểu', 'ễ', 'ễm', 'ễn', 'ễng', 'ễnh', 'ễu', 'ệ', 'ệc', 'ệch', 'ệm', 'ện', 'ệng', 'ệnh', 'ệp', 'ệt', 'ệu', 'ỉ', 'ỉa', 'ỉm', 'ỉn', 'ỉnh', 'ỉu', 'ị', 'ịa', 'ịc', 'ịch', 'ịm', 'ịn', 'ịnh', 'ịp', 'ịt', 'ịu', 'ọ', 'ọa', 'ọc', 'ọe', 'ọi', 'ọm', 'ọn', 'ọng', 'ọp', 'ọt', 'ỏ', 'ỏa', 'ỏe', 'ỏi', 'ỏm', 'ỏn', 'ỏng', 'ố', 'ốc', 'ối', 'ốm', 'ốn', 'ống', 'ốp', 'ốt', 'ồ', 'ồi', 'ồm', 'ồn', 'ồng', 'ổ', 'ổc', 'ổi', 'ổm', 'ổn', 'ổng', 'ỗ', 'ỗi', 'ỗm', 'ỗn', 'ỗng', 'ộ', 'ộc', 'ội', 'ộm', 'ộn', 'ộng', 'ộp', 'ột', 'ớ', 'ớc', 'ới', 'ớm', 'ớn', 'ớng', 'ớp', 'ớt', 'ờ', 'ời', 'ờm', 'ờn', 'ờng', 'ở', 'ởi', 'ởm', 'ởn', 'ởng', 'ỡ', 'ỡi', 'ỡm', 'ỡn', 'ỡng', 'ợ', 'ợc', 'ợi', 'ợm', 'ợn', 'ợng', 'ợp', 'ợt', 'ụ', 'ụa', 'ục', 'ụi', 'ụm', 'ụn', 'ụng', 'ụp', 'ụt', 'ụy', 'ủ', 'ủa', 'ủi', 'ủm', 'ủn', 'ủng', 'ủy', 'ứ', 'ứa', 'ức', 'ứi', 'ứn', 'ứng', 'ứt', 'ưu', 'ừu', 'ứu', 'ửu', 'ữu', 'ựu', 'ừ', 'ừa', 'ừi', 'ừm', 'ừn', 'ừng', 'ử', 'ửa', 'ửi', 'ửn', 'ửng', 'ữ', 'ữa', 'ữi', 'ữn', 'ững', 'ự', 'ựa', 'ực', 'ựi', 'ựn', 'ựng', 'ựt', 'ỳ', 'ỳn', 'ỳnh', 'ỵ', 'ỵc', 'ỵch', 'ỵn', 'ỵp', 'ỵt', 'ỷ', 'ỷn', 'ỷnh', 'ỹ', 'sp', 'spn', 'sil']
vie_symbols = _vie_phones
