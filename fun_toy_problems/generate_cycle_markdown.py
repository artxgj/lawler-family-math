import argparse
import io

from chinese_calendar import *
from p3lib.markdown import Markdown, MdCellAlign


def genmd_chinese_calender(iostream):
    field_names = ['Gregorian Year', 'Chinese Zodiac', 'Heavenly Stem', 'Earthly Branch']
    field_alignments = [MdCellAlign.center for _ in range(len(field_names))]

    iostream.write(f"{Markdown.h3('Programmatically-generated Sexagenary Cycle (六十干支)')}\n")
    iostream.write(f"{Markdown.line('References:')}\n")

    ref_sexagenary = Markdown.ul(Markdown.link("Sexagenary Cycle", "https://en.wikipedia.org/wiki/Sexagenary_cycle"))
    ref_chzodiac = Markdown.ul(Markdown.link("Chinese Zodiac", "https://en.wikipedia.org/wiki/Chinese_zodiac"))
    ref_gregcal = Markdown.ul(Markdown.link("Gregorian Calendar", "https://en.wikipedia.org/wiki/Gregorian_calendar"))

    iostream.write(f"{ref_sexagenary}\n")
    iostream.write(f"{ref_chzodiac}\n")
    iostream.write(f"{ref_gregcal}\n")
    iostream.write("\n")

    table_headers = Markdown.table_header(field_names, field_alignments)
    iostream.write(f"{table_headers}\n")

    for year in range(1984, 2044):
        row = Markdown.table_row([f"{year}", f"{zodiac_emoji(year)}{zodiac_chinese_character(year)}", heavenly_stem(year), earthly_branch(year)])
        iostream.write(f"{row}\n")


def mdstdout():
    output = io.StringIO()
    genmd_chinese_calender(output)
    print(output.getvalue())
    output.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sexagen_filepath", help="The sexagenary output filepath")
    args = parser.parse_args()

    # /Users/arthurkho/github/p3/data/tmp/sexagenary-cycle-1984.md
    with io.open(args.sexagen_filepath, 'w', encoding='utf-8') as ostream:
        genmd_chinese_calender(ostream)


if __name__ == '__main__':
    # mdstdout()
    main()
