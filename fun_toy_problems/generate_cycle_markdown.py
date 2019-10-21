import argparse
import io

from chinese_calendar import *
from p3lib.markdown import Markdown


def mdcalstream(ostream):
    static_part = """### Programmatically-generated Sexagenary Cycle (六十干支)
References:  
- [Sexagenary Cycle](https://en.wikipedia.org/wiki/Sexagenary_cycle) 
- [Chinese Zodiac](https://en.wikipedia.org/wiki/Chinese_zodiac) 
- [Gregorian Calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) 

| Gregorian Year | Chinese Zodiac | Heavenly Stem | Earthly Branch |
| :---: | :---: | :---: | :---: |
"""

    ostream.write(f"{static_part}")

    for year in range(1984, 2044):
        row = Markdown.table_row([f"{year}", f"{zodiac_emoji(year)}{zodiac_chinese_character(year)}", heavenly_stem(year), earthly_branch(year)])
        ostream.write(f"{row}\n")


def mdstdout():
    output = io.StringIO()
    mdcalstream(output)
    print(output.getvalue())
    output.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sexagen_filepath", help="The sexagenary output filepath")
    args = parser.parse_args()

    with io.open(args.sexagen_filepath, 'w', encoding='utf-8') as ostream:
        mdcalstream(ostream)


if __name__ == '__main__':
    # mdstdout()
    main()
