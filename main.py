# モールス
morse_japanese = {'ア': '--.--', 'イ': '.-', 'ウ': '..-', 'エ': '-.---', 'オ': '.-...', 'カ': '.-..', 'キ': '-.-..', 'ク': '...-', 'ケ': '-.--', 'コ': '----', 'サ': '-.-.-', 'シ': '--.-.', 'ス': '---.-', 'セ': '.---.', 'ソ': '---.', 'タ': '-.', 'チ': '..-.', 'ツ': '.--.', 'テ': '.-.--', 'ト': '..-..', 'ナ': '.-.', 'ニ': '-.-.', 'ヌ': '....', 'ネ': '--.-', 'ノ': '..--', 'ハ': '-...', 'ヒ': '--..-', 'フ': '--..', 'ヘ': '.', 'ホ': '-..', 'マ': '-..-', 'ミ': '..-.-', 'ム': '-', 'メ': '-...-', 'モ': '-..-.', 'ヤ': '.--', 'ユ': '-..--', 'ヨ': '--', 'ラ': '...', 'リ': '--.', 'ル': '-.--.', 'レ': '---', 'ロ': '.-.-', 'ワ': '-.-', 'ヰ': '.-..-', 'ヱ': '.--..', 'ヲ': '.---', 'ン': '.-.-.', 'ー': '.--.-', '゛': '..', '゜': '..--.', '、': '.-.-.-'}

#def 

# dfs
def dfs(crypto, answer):
    if crypto == "":
        print(answer)
        return
    for c, tontsu in morse_japanese.items():
        # print(crypto + ", " + c)
        if len(crypto) >= len(tontsu):
            if crypto[:len(tontsu)] == tontsu:
                ansplus = answer + c
                # print('a' + crypto[:len(tontsu)])
                dfs(crypto[len(tontsu):], ansplus)

import sys

sys.setrecursionlimit(100000)

# 入力
print("Please input the Morse Code: ")
aisu = str(input())
if aisu == "":
    print("kara-mojiretsu")
    exit(0)

# トンツー対応
print("ton = ")
ton = input()
if ton == "":
    ton = "."

print("tsu = ")
tsu = input()
if tsu == "":
    tsu = "-"

if ton == tsu:
    print("何考えてんの？")
    exit(0)

# 暗号を変換


# 日本語ですか？
print("This is Japanese? (Y/n): ")
isJapanese = input()
if isJapanese == "n" or isJapanese == "N" or isJapanese == "false" or isJapanese == "False" or isJapanese == "FALSE":
    # fuck
    print("fuck")


# 貪欲に当てていく。
# 間違えたら戻る。

ans = ""
dfs(aisu, ans)

print("finish.")