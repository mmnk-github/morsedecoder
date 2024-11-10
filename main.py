# モールス
chosen_morse = {}
morse_japanese = {'ア': '--.--', 'イ': '.-', 'ウ': '..-', 'エ': '-.---', 'オ': '.-...', 'カ': '.-..', 'キ': '-.-..', 'ク': '...-', 'ケ': '-.--', 'コ': '----', 'サ': '-.-.-', 'シ': '--.-.', 'ス': '---.-', 'セ': '.---.', 'ソ': '---.', 'タ': '-.', 'チ': '..-.', 'ツ': '.--.', 'テ': '.-.--', 'ト': '..-..', 'ナ': '.-.', 'ニ': '-.-.', 'ヌ': '....', 'ネ': '--.-', 'ノ': '..--', 'ハ': '-...', 'ヒ': '--..-', 'フ': '--..', 'ヘ': '.', 'ホ': '-..', 'マ': '-..-', 'ミ': '..-.-', 'ム': '-', 'メ': '-...-', 'モ': '-..-.', 'ヤ': '.--', 'ユ': '-..--', 'ヨ': '--', 'ラ': '...', 'リ': '--.', 'ル': '-.--.', 'レ': '---', 'ロ': '.-.-', 'ワ': '-.-',  'ヲ': '.---', 'ン': '.-.-.', 'ー': '.--.-', '゛': '..', '゜': '..--.', '、': '.-.-.-'}
morse_english = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

def replace_morse(ton, tsu):
    new_dict = {}
    for c, tontsu in chosen_morse.items():
        new_tontsu = ""
        for t in tontsu:
            if t == '-':
                new_tontsu = new_tontsu + tsu
            elif t == '.':
                new_tontsu = new_tontsu + ton
            else:
                print("?")
                exit(0)
        new_dict[c] = new_tontsu
    return new_dict

# dfs
def dfs(crypto, answer):
    res = []
    cnt = 0
    if crypto == "":
        print(answer)
        return 1
    for c, tontsu in chosen_morse.items():
        if len(crypto) >= len(tontsu):
            if crypto[:len(tontsu)] == tontsu:
                ansplus = answer + c
                cnt = cnt + dfs(crypto[len(tontsu):], ansplus)
    return cnt

import sys

sys.setrecursionlimit(100000)

# 入力
print("Please input the Morse Code: ")
aisu = str(input())
if aisu == "":
    print("kara-mojiretsu")
    exit(0)

# トンツー対応
print("ton(.) = ")
ton = input()
if ton == "":
    ton = "."

print("tsu(-) = ")
tsu = input()
if tsu == "":
    tsu = "-"

if ton == tsu:
    print("何考えてんの？")
    exit(0)

# 辞書を変換
morse_japanese = replace_morse(ton, tsu)

# 日本語ですか？
print("日本語：1, English：2")
chosen_language = input()
if chosen_language == "1":
    # 日本語
    chosen_morse = morse_japanese
elif chosen_language == "2":
    # English
    chosen_morse = morse_english
else:
    # fuck
    print("fuck")
    exit(0)

# 貪欲に当てていく。
# 間違えたら戻る。
ans = dfs(aisu, "")

print("count: " + str(ans))
if ans == 0:
    print("残念")
    exit(0)
print("finish.")