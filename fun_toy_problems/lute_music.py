from typing import IO
from utf8unicode import codepoints_set

import argparse
import io


def luteplaying(ostream: IO[str]) -> None:
    poem = """## Fun with [Unicode](https://home.unicode.org/basic-info/overview/)
### 彈琴   Lute Playing
##### 劉長卿 Liu Changqing

> 泠泠七弦上 🎻  
> 靜聽松風寒 🌲  
> 古調雖自愛 🎶  
> 今人多不彈 😞  

<br/>
"""
    table_header = """
| Unicode Character | UTF-16 |
|:-----------------:|:------:|"""

    poem_unicode_set = sorted(codepoints_set(poem, {'\n', ' ', '#', '*', '>'}))

    ostream.write(f"{poem} \n")
    ostream.write(f"{table_header}\n")

    for c, u in poem_unicode_set:
        ostream.write(f"| **{c}** | {u} |\n")


def stream_stdout():
    ostream = io.StringIO()
    luteplaying(ostream)
    print(ostream.getvalue())


def stream_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_filepath", help="The file to which the markdown characters is written")
    args = parser.parse_args()

    with io.open(args.output_filepath, 'w', encoding='utf-8') as ostream:
        luteplaying(ostream)


if __name__ == '__main__':
    # stream_stdout()
    stream_file()
