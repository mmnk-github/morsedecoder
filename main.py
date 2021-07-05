# モールス
morse_japanese = {'ア': '--.--', 'イ': '.-', 'ウ': '..-', 'エ': '-.---', 'オ': '.-...', 'カ': '.-..', 'キ': '-.-..', 'ク': '...-', 'ケ': '-.--', 'コ': '----', 'サ': '-.-.-', 'シ': '--.-.', 'ス': '---.-', 'セ': '.---.', 'ソ': '---.', 'タ': '-.', 'チ': '..-.', 'ツ': '.--.', 'テ': '.-.--', 'ト': '..-..', 'ナ': '.-.', 'ニ': '-.-.', 'ヌ': '....', 'ネ': '--.-', 'ノ': '..--', 'ハ': '-...', 'ヒ': '--..-', 'フ': '--..', 'ヘ': '.', 'ホ': '-..', 'マ': '-..-', 'ミ': '..-.-', 'ム': '-', 'メ': '-...-', 'モ': '-..-.', 'ヤ': '.--', 'ユ': '-..--', 'ヨ': '--', 'ラ': '...', 'リ': '--.', 'ル': '-.--.', 'レ': '---', 'ロ': '.-.-', 'ワ': '-.-', 'ヰ': '.-..-', 'ヱ': '.--..', 'ヲ': '.---', 'ン': '.-.-.', 'ー': '.--.-', '゛': '..', '゜': '..--.', '、': '.-.-.-'}

def replace_morse(ton, tsu):
    new_dict = {}
    for c, tontsu in morse_japanese.items():
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
    if crypto == "":
        print(answer)
        return
        #nanikore = []
        #nanikore.append(answer)
        #return nanikore
    for c, tontsu in morse_japanese.items():
        if len(crypto) >= len(tontsu):
            if crypto[:len(tontsu)] == tontsu:
                ansplus = answer + c
                dfs(crypto[len(tontsu):], ansplus)
                #res.extend(dfs(crypto[len(tontsu):], ansplus))
    #return res
    return

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
print("Is this Japanese? (Y/n): ")
isJapanese = input()
if isJapanese == "n" or isJapanese == "N" or isJapanese == "false" or isJapanese == "False" or isJapanese == "FALSE":
    # fuck
    print("fuck")

# 貪欲に当てていく。
# 間違えたら戻る。
dfs(aisu, "")
exit(0)

ans = dfs(aisu, "")
print("count: " + str(len(ans)))
if len(ans) == 0:
    print("残念")
    exit(0)
ans.sort()
print(ans)
print("finish.")