from utf8unicode import Unicode, utf8_unicode_set

if __name__ == '__main__':
    poem="""
# 彈琴   Lute Playing
### 劉長卿 Liu Changqing

泠泠七弦上 🎻
靜聽松風寒 🌲
古調雖自愛 🎶
今人多不彈 😞
"""
    print(poem)
    poem_unicode_set = sorted(utf8_unicode_set(poem, {'\n', ' ', '#', '*'}))

    for c, u in poem_unicode_set:
        print(f"**{c}** {u}  ")
