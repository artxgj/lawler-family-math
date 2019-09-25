from utf8unicode import codepoints_set
if __name__ == '__main__':
    poem="""
### 彈琴   Lute Playing
##### 劉長卿 Liu Changqing

> 泠泠七弦上 🎻
> 靜聽松風寒 🌲
> 古調雖自愛 🎶
> 今人多不彈 😞


"""

    print(poem)
    poem_unicode_set = sorted(codepoints_set(poem, {'\n', ' ', '#', '*', '>'}))

    print("| Unicode Character | UTF-16 |")
    print("|:-----------------:|:------:|")
    for c, u in poem_unicode_set:
        print(f"| **{c}** | {u} |")
