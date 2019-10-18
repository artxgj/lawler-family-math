import argparse
from chinese_calendar import *

def markdown_header(write):
    write('### Programmatically-generated Sexagenary Cycle (六十干支)\n')
    write('Gregorian Year | Chinese Zodiac | Heavenly Stem | Earthly Branch\n')
    write(':------------: | :------------: | :-----------: | :------------:\n')



with open('sexagenary-cycle-1984.md', 'wt', encoding='utf-8') as outf:
    markdown_header(outf.write)
    for year in range(1984, 2044):
        outf.write(f'{year} | {zodiac_emoji(year)}{zodiac_chinese_character(year)} | {heavenly_stem(year)} | {earthly_branch(year)}\n')
