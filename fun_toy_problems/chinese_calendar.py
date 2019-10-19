__all__ = ['heavenly_stem', 'earthly_branch', 'zodiac_emoji', 'zodiac_chinese_character']

ZodiacHanzi = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
ZodiacEmojis = '🐭🐂🐯🐰🐲🐍🐎🐑🐒🐔🐶🐷'
HeavenlyStems = '甲乙丙丁戊己庚辛壬癸'
EarthlyBranches = '子丑寅卯辰巳午未申酉戌亥'

_DEFAULT_CYCLE_BASE_YEAR = 1984
_sexagenary = 60

def _sexagenary_cycle_offset(year):
    return (year - _DEFAULT_CYCLE_BASE_YEAR) % _sexagenary

def cycle_base_year(year):
    num_years = (year - _DEFAULT_CYCLE_BASE_YEAR) // 60 * 60
    return _DEFAULT_CYCLE_BASE_YEAR + num_years

def heavenly_stem(year):
    index = _sexagenary_cycle_offset(year) % len(HeavenlyStems)
    return HeavenlyStems[index]

def earthly_branch(year):
    index = _sexagenary_cycle_offset(year) % len(EarthlyBranches)
    return EarthlyBranches[index]

def zodiac_emoji(year):
    index = _sexagenary_cycle_offset(year) % len(EarthlyBranches)
    return ZodiacEmojis[index]

def zodiac_chinese_character(year):
    index = _sexagenary_cycle_offset(year) % len(EarthlyBranches)
    return ZodiacHanzi[index]

if __name__ == '__main__':
    for year in range(1984, 2044):
        print(f'{year}: {zodiac_emoji(year)} {zodiac_chinese_character(year)} {heavenly_stem(year)}{earthly_branch(year)}')
