# モールス
morse_japanese = {'ア': '--.--', 'イ': '.-', 'ウ': '..-', 'エ': '-.---', 'オ': '.-...', 'カ': '.-..', 'キ': '-.-..', 'ク': '...-', 'ケ': '-.--', 'コ': '----', 'サ': '-.-.-', 'シ': '--.-.', 'ス': '---.-', 'セ': '.---.', 'ソ': '---.', 'タ': '-.', 'チ': '..-.', 'ツ': '.--.', 'テ': '.-.--', 'ト': '..-..', 'ナ': '.-.', 'ニ': '-.-.', 'ヌ': '....', 'ネ': '--.-', 'ノ': '..--', 'ハ': '-...', 'ヒ': '--..-', 'フ': '--..', 'ヘ': '.', 'ホ': '-..', 'マ': '-..-', 'ミ': '..-.-', 'ム': '-', 'メ': '-...-', 'モ': '-..-.', 'ヤ': '.--', '': '', 'ユ': '-..--', 'ヨ': '--', 'ラ': '...', 'リ': '--.', 'ル': '-.--.', 'レ': '---', 'ロ': '.-.-', 'ワ': '-.-', 'ヰ': '.-..-', 'ヱ': '.--..', 'ヲ': '.---', 'ン': '.-.-.', 'ー': '.--.-', '゛': '..', '゜': '..--.', '、': '.-.-.-'}

mmnk = "うんち"

# dfs
def morse(crypto, answer):
    if crypto == "":
        print(answer)
        return True
    for c, tontsu in morse_japanese.items():
        if len(crypto) >= len(tontsu):
            ansplus = answer + c
            if morse(crypto[len(tontsu):], ansplus):
                return True
    return False

# 入力
print("Please input the Cryptography: ")
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

# 日本語ですか？
print("This is Japanese? (Y/n): ")
isJapanese = input()
if isJapanese == "n" or isJapanese == "N" or isJapanese == "false" or isJapanese == "False" or isJapanese == "FALSE":
    # fuck
    print("fuck")


# 貪欲に当てていく。
# 間違えたら戻る。

ans = ""
if not morse(aisu, ans):
    print("変換できなかった")