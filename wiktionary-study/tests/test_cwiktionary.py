import unittest

from cjkwicktionary import WiktEntryCJKV, WiktMinnanPronunciation


class TestCJKWikicode(unittest.TestCase):
    def setUp(self):
        self.cjkv = """
        {{also|傢|冢|冡}}
{{character info/new}}
==Translingual==
{{stroke order|strokes=10}}
{{stroke order|type=animate}}
===Han character===
{{Han char|rn=40|rad=宀|as=07|sn=10|four=30232|canj=JMSO|ids=⿱宀豕}}
====Derived characters====
* {{l|mul|[[傢]], [[嫁]], [[稼]]}}
====Descendants====
* [[𛀢]]
====References====
{{Han ref|kx=0286.170|dkj=07169|dj=0566.030|hdz=20930.150|uh=5BB6}}
----
==Chinese==
===Glyph origin===
{{Han etym}}
{{Han compound|宀|豕|c1=s|c2=p|t1=roof|t2=pig|ls=psc|no_och2=y}}.
{{lang|zh|豕}} is an abbreviation of {{och-l|豭|male pig, boar}} (''{{w|Shuowen Jiezi}}''), a homophone of {{zh-l|家}} in {{w|Old Chinese}}. See {{zh-l|*豭}} for more on the glyph composition.
===Etymology 1===
{{zh-forms|alt=𡦼}}
{{zh-wp}}
[[File:Ranch style home in Salinas, California.JPG|thumb|200px|{{lang|zh|一座居住有一家人的房屋}}]]
Cognate with {{cog|bo|མཁར||castle; house}} ({{zh-ref|Schuessler, 2007}}). 
{{och-l|嫁|to give a girl in marriage}} is the [[exoactive]] of {{och-l|家|house; household; family}}.
====Pronunciation 1====
{{zh-pron
|m=jiā,jia
|ma=y
|m-s=
|dg=җя1
|c=gaa1
|c-t=
|g=
|h=pfs=kâ;gd=ga1
|j=
|mb=gá
|md=gă
|mn=ke/ka
|mn_note=ke - vernacular; ka - literary
|mn-t=gê1/gia1
|mn-t_note=gê1 - vernacular; gia1 - literary (used only in operas)
|w=1ka,1jia
|w_note=1jia is literary
|x=
|mc=y
|oc=y
|cat=n,suf,cls,pron
}}
=====Definitions=====
{{zh-hanzi}}
# [[home]]
#: {{zh-x|我 的 家 就 在 這裡。|My '''home''' is here.}}
# [[house]]
# [[family]]; [[household]]
#: {{zh-x|家庭|family}}
#: {{zh-x|家族|clan; family}}
# {{lb|zh|polite|for family member}} [[my]]
# [[domesticated]]; [[domestic]]
# {{n-g|Classifier for families, businesses and companies.}}
# [[school of thought]]; [[philosophical]] [[school]]
#: {{zh-x|^儒家|Confucian school}}
#: {{zh-x|^道家|Daoist School}}
# {{†}} [[fief]] of [[ministers]] or [[senior]] [[officials]]
# {{n-g|Suffix denoting a person with a certain occupation or social standing.}} [[-er]]
# {{n-g|Suffix denoting specialist in a certain activity or field.}} [[-ist]]; [[-er]]
#: {{zh-x|藝術家|artist}}
#: {{zh-x|科學家|scientist}}
# {{n-g|Suffix used after a noun to specify a type of person.}}
#: {{zh-x|老人家 身體 可 還 好 啊？|Is the parent of yours well?|M-UIB}}
#: {{zh-x|一 個 姑娘{niang}-家，成天 不 想 著[着]{zhe} 學好{hǎor}，天天 跟 道{dàor}上{shang} 的 男人 鬼混，像 什麼 樣子{zi}！||M-UIB}}
# {{surname|zh}}
======Synonyms======
{{zh-dial}}
{{zh-dial|房子}}
* {{q|suffix used after a noun to specify a type of person}}: {{zh-l|家家}}, {{q|Cantonese}} {{zh-l|人家|tr=jan<sup>4</sup> gaa<sup>1</sup>}}
=====Compounds=====
{{zh-der|家財|家蠶|家產|家長里短|家長里短兒|家常|家常便飯|家常話|家仇|家醜|家畜|家傳|家祠|家慈|家大業大|家當|家當兒|家道|家底|家底兒|家電|家丁|家法|家訪|家風|家父|家鴿|家館|家規|家戶|傢伙|家雞|家給人足|家計|家祭|家家|家家兒|家家戶戶|家教|家姐|家景|家境|家居|家具|家眷|家君|家口|家累|家裡|家門|家廟|家母|家娘|家奴|家貧如洗|家破人亡|家譜|家雀兒|家禽|家人|家舍|家生子|家生子兒|家聲|家甚|家史|家世|家事|家室|家書|家屬|家鼠|家數|家私|家天下|家庭|家庭病床|家庭承包|家庭婦女|家庭教育|家庭手工業|家庭影院|家徒四壁|家兔|家蚊|家屋|家無擔石|家無儋石|家務|家弦胡誦|家鄉|家小|家信|家兄|家學|家訓|家鴨|家嚴|家宴|家燕|家養|家業|家蠅|家用|家魚|家喻戶曉|家園|家院|家宅|家長|家長制|家珍|家種|家主|家資|家子|家族|家世寒微|家中|家人一等|家伙|家俱|家傭|家僮|家和萬事興|家培|家壩水電站|家姊|家家有本難念的經|家常菜|家常豆腐|家庭主夫|家庭主婦|家庭作業|家庭地址|家庭成員|家庭教師|家庭暴力|家庭消費者|家庭煮夫|家庭生活|家政|家政員|家政學|家族樹|家暴|家樂福|家灶|家用電器|家用電腦|家童|家累千金，坐不垂堂|家臣|家貲萬貫|家轎|家鄉雞|家醜不可外傳|家醜不可外傳，流言切莫輕信|家醜不可外揚|家鴨綠頭鴨|丟到家|主權國家|乾嘉三大家|事怕行家|二奶專家|人家|人類學家|企業家|住家|佛家|作家|作曲家|俗家|做人家|傳家|傾家|儒家|元曲四大家|全家|公家|六家|六朝四大家|兵家|冒險家|冤家|出家|分家|分析家|到家|劇作家|加拿大皇家|勤儉起家|化學家|半路出家|占星家|原子科學家|古生物學家|史學家|史家|合家|吉野家|名家|名畫家|周家|咱家|哀家|哲學家|唐初四大家|唐宋八大家|商家|四海為家|回娘家|回家|回老家|國家|地理學家|地質學家|地震學家|塗家|墨家|外交家|多民族國家|夢想家|大家|大投資家|大數學家|天文學家|天體物理學家|女家|女管家|娘家|娼家|婆家|婦道人家|學家|安家|宋四家|官宦人家|官家|宜家|客家|實幹家|實業家|專家|專門家|對家|小說家|居家|岳家|工業化國家|巧家|希西家|店家|廠家|微生物學家|心理學家|思想家|想家|愛國如家|慈善家|成家|戰略家|戲劇家|批評家|抄家|投資家|持家|指揮家|挨家|探家|探險家|搬家|攝影家|收藏家|改革家|政治家|故家|教育家|數學家|文字學家|文學家|新儒家|新興經濟國家|星命家|星家|暖巢管家|書法家|書畫家|有核國家|本家|東家|核國家|植物學家|楊福家|歌唱家|歷史學家|歷史家|民家|民用核國家|氣候學家|水利家|法學家|法家|洪家|活動家|流氓國家|海灣國家|渾家|滕家|演講家|漢學家|漫畫家|炒家|物理學家|獨家|王家|玩偶之家|玩家|現代新儒家|理學家|理論家|瑪家|生態學家|生物化學家|生物學家|生理學家|男家|男管家|畫家|當代新儒家|當家|病家|病毒學家|病理學家|登山家|發家|發展中國家|發展的國家|發明家|發達國家|白手起家|百家|皇家|破家|神學家|神經學家|私家|科學家|算命家|管家|精神學家|經濟學家|編譯家|編輯家|縱橫家|美食家|翻譯家|老人家|老家|考古學家|考古家|自家|自成一家|舉家|舊家|舞蹈家|航海家|船家|良家|莊家|華潤萬家|藝術家|藥物學家|行家|親家|觀察家|計算機科學家|評論家|詭辯家|語言學家|諸子十家|諸子百家|貨比三家|買家|貽笑方家|資本家|贏家|走娘家|蹺家|軍事家|辛普森一家|農家|返家|送貨到家|運動家|道家|道德家|鄰家|酒家|醫學家|醫學專家|醫家|金融家|銀行家|鋪家|鋼琴家|鑒賞家|闔家|陰陽家|雄辯家|雕刻家|雜劇四大家|雜家|非核國家|非核武器國家|革命家|音樂家|預言家|養家|首家|富家|劉家隔|焦家莊|郭家堡|雷家祠|羅家橋|段家|楊家坳|徐家山|蘇家壋|王家橋|斯家場|劉家場|萬家|三家垸 |莊家鋪|陳家鋪|畢家塘|黃家潭|余家棚|董家剅|蔣家沖|戴家場|瞿家灣|黃家口|張家灣|馬家寨|朱家峪|莊家山|楊家廠|孟家溪|毛家港|甘家廠|閻家河|張家畈|丁家塝|張家港|楊家浲|張家集|付家灣|柴家廟|涂家堖|伍家崗|土家族|張家莊|馬家店|顧家店|艾家|徐家棚|伍家|張家嶺|陶家嶺|馬家嶺|嚴家墩|黎家垸|樊家巷|聶家河|姚家店|潘家灣|王家畈|國家公園|吳家灣|梅家河|高家堰|賀家坪|付家堰|五峰土家族自治縣|秦家坪|胡家營|譚家灣|好家伙|楊家|華家河|丁家營|習家店|範家|麻家渡|蔣家堰|恩施土家族苗族自治州|楊家坡|胡家塘|李家河|唐家墩|黃家營|裴家橋|鞏家灣|周家灣|施家灣|彭家灣|蔡家營|高家沖|邵家樓|彪家廟|彭家嶺|席家埡|五家洲|白家堰|楊家湖|陳家樓|龍家溝|汪家臺|陳家沖|喬家坪|羅家|亮家堖|車家店|祁家溝|余家橋|解家沖|梁家畈|許家沖|林家溪|韓家灣|黃家沖|徐家|逐家|趙家|郭家|譚家|陳家港|而家:ji4 gaa1|頭家|滑家壋|凌家湖|雷家店|陶家河|金家橋|梅家岩|馬家坳|趙家畈|羌家壪/羌家塆|家財萬貫|國破家亡|家家酒}}
====Pronunciation 2====
{{zh-pron
|mn=xm,zz,ta,kh,tp,tn,yl,lk,sx,hc,pn:ka/qz,jj,ph:kāi/zz,kh,tc:ka/km,mg:kai
|mn-t=ga1
|dial=n
|cat=n
}}
=====Definitions=====
{{zh-hanzi}}
# {{lb|zh|Min Nan}} {{zh-only|家己|ka-kī}}
====Pronunciation 3====
{{zh-pron
|mn=xm,qz,lk:kha/zz,tp,kh,tn,sx,yl,hc,tc:khia/xm,zz,twv:khia
|mn-t=kia1
|dial=n
|cat=n
}}
=====Definitions=====
{{zh-hanzi}}
# {{lb|zh|Min Nan}} {{zh-only|私家|tr=-}}
===Etymology 2===
{{zh-forms|alt=價}}
====Pronunciation====
{{zh-pron
|m=jie
|dial=n
|cat=
}}
====Definitions====
{{zh-hanzi}}
# {{rfdef|zh}}
{{zh-cat|Beginning|Family|Collectives}}
----
==Japanese==
===Kanji===
{{ja-kanji|grade=2|rs=宀07}}
====Readings====
{{ja-readings
|goon=け, く
|kanon=か, こ
|kun=いえ-<いへ-, や-, うち-
}}
====Compounds====
{{der-top|Compounds}}
* {{ja-r|家%屋|か%おく}}
* {{ja-r|家具|かぐ}}
* {{ja-r|家%族|か%ぞく}}
* {{ja-r|家%庭|か%てい}}
* {{ja-r|家禽|かきん}}: [[domestic]] [[fowl]], [[poultry]]
* {{ja-r|家守|やもり}}: [[gecko]]
* {{ja-r|家守|やもり}}: [[guarding]] a [[house]], or a person who does such; real estate agent in the Edo period
{{der-bottom}}
===Etymology 1===
{{ja-kanjitab|いえ|yomi=k}}
{{IPAfont|⟨ipe<sub>1</sub>⟩}} → *{{IPAchar|/ipʲe/}} → {{IPAchar|/iɸe/}} → {{IPAchar|/iwe/}} → {{IPAchar|/ie/}}
From {{inh|ja|ojp|sort=いえ|-}}.
Possibly related to {{m|ja|廬|tr=iho → io||[[temporary]] [[hut]]}}.
====Pronunciation====
{{ja-pron|yomi=k|いえ|acc=2|acc_ref=DJR,NHK}}
====Noun====
{{ja-noun|いえ|hhira=いへ}}
# a [[house]]
# one's own [[home]]
# a [[home]], [[household]]
#* {{quote-book|ja
||
|{{ruby|{{w2|ja|魔法使いの嫁|[魔法使いの嫁](The Ancient Magus Bride)|sc=Jpan}}}}
||17
|last=Yamazaki
|first=Kore
|chapter={{lang|ja|第1篇　April showers bring May flowers.|sc=Jpan}}
|trans-chapter=Composition 1: [[April showers bring May flowers]].
|trans-title={{w|The Ancient Magus' Bride|The Ancient Magus’ Bride}}
|genre=fiction
|location=Tokyo
|publisher={{w|Mag Garden}}
|nodate=y
|volume=1}}
#*: {{ja-usex|ここが僕の'''家'''　そして今日から君が暮らす'''家'''でもある|^ここ が ぼく の '''いえ'''　^そして きょう から きみ が くらす '''いえ''' で も ある|This is my home. From now on, you will live here, too.}}
# a [[family]]
===Etymology 2===
{{ja-kanjitab|や|yomi=k}}
{{rfe|ja|sort=や}}
====Alternative forms====
* {{ja-l|屋}}
====Pronunciation====
{{ja-pron|yomi=k|や|acc=1|acc_ref=DJR,NHK}}
====Noun====
{{ja-noun|や}}
# a [[house]]
====Suffix====
{{ja-pos|や|suffix}}
# house of something, place where some business is conducted
# person who does that thing
=====See also=====
* {{ja-r|者|-しゃ}}
* {{ja-r|手|-しゅ}}
===Etymology 3===
{{ja-kanjitab|うち|yomi=k}}
Cognate with {{m|ja|内|tr=uchi||[[middle]]}}.<ref name="DJR"/>
====Pronunciation====
{{ja-pron|yomi=k|うち|acc=0|acc_ref=DJR,NHK}}
====Noun====
{{ja-noun|うち}}
# a [[house]]
# one's house
=====Descendants=====
* {{desc|bor=1|en|hooch}}
===Etymology 4===
{{ja-kanjitab|yomi=i|sort=ち}}
Contraction of ''uchi'' above.
Often following the genitive case marker {{ja-r|の}} which contracts to ''-n''.
====Noun====
{{ja-noun|ち}}
# a [[house]]
#: {{ja-usex-inline|俺ん'''家'''に来ない？|^おれん'''ち''' に こない？|Wanna come to my '''place'''?}}
===Etymology 5===
{{ja-kanjitab|か|yomi=kanon}}
From {{der|ja|ltc|sort=か|-}} {{ltc-l|家}}.
The {{m|ja|漢音|tr=kan'on|lit=[[Han]] [[sound]]}}, so likely a latter borrowing from {{cog|ltc|-}}.
====Suffix====
{{ja-pos|か|suffix}}
# an [[expert]], [[professional]], [[performer]]
=====Derived terms=====
* {{ja-r|漫画家|まんがか}}
===Etymology 6===
{{ja-kanjitab|け|yomi=goon}}
The {{m|ja|呉音|tr=goon|lit=[[Wu]] [[sound]]}}, so likely the initial borrowing from {{cog|ltc|-}}.
====Suffix====
{{ja-pos|け|suffix}}
# {{n-g|representing [[relationship]] to a [[family]]}}
#: {{ja-usex-inline|[[平]]'''家'''|^たいら-'''け'''|the Taira family}}
===References===
<references/>
[[Category:Japanese basic words|いえ]]
----
==Korean==
===Hanja===
{{ko-hanja|hangeul=[[가]], [[고]]}}
# home; family; household
====Compounds====
{{der-top}}
* {{ko-inline|가구|||家口}}
* {{ko-inline|가장|||家長}}
* {{ko-inline|가정|||家庭}}
* {{ko-inline|가족|||家族}}
* {{ko-inline|작가|||作家}}
{{der-bottom}}
----
==Okinawan==
===Kanji===
{{head|ryu|Han character|hiragana|やー|romaji|yā}}
====Compounds====
* {{l|ryu|家内|tr=ちねー, chinē|t=household}}
* {{l|ryu|家鴨|tr=あひる, ahiru, あひらー, ahirā, あふぃらー, afirā|t=[[domestic duck]]}}
===Noun===
{{head|ryu|noun|hiragana|やー|romaji|yā|sort=やあ}}
# [[house]]
====Derived terms====
* {{l|ryu|新家|tr=みーやー, mīyā|t=new house}}
* {{l|ryu|家人衆|tr=やーにんじゅ, yāninju|t=family}}
{{C|ryu|Buildings|Housing|sort=やあ}}
----
==Vietnamese==
===Han character===
{{vi-hantu|[[gia]], [[nhà]]|rs=宀07}}
# {{rfdef|vi|sort=宀07}}
----
==Yonaguni==
===Kanji===
{{head|yoi|Han character|hiragana|だー|romaji|dā}}
===Noun===
{{head|yoi|noun|hiragana|だー|romaji|dā|sort=たあ'}}
# [[house]]
{{C|yoi|Buildings|Housing|sort=たあ'}}
        """

        self.no_cjkv = """
    {{also|hokkien}}
{{interwiktionary|code=zh-min-nan}}
==English==
{{wikipedia}}

===Alternative forms===
* {{q|Philippines}} {{l|en|Fookien}}

===Etymology===
Borrowed from {{bor|en|nan|-}} {{zh-l|福建|Fujian|tr=Hok-kiàn}}.

===Proper noun===
{{en-proper noun}}

# A dialect [[subgroup]] of the [[Min Nan]] branch of the Chinese language which is mainly spoken in the south-eastern part of mainland China ([[Fujian]] province), [[Taiwan]], and by [[overseas Chinese]] of [[Hoklo]] descent.<!--This subgroup of Min Nan is also known as the Min Tai Division. It encompasses several major variants, which are generally mutually intelligible: Amoy Min (Amoy dialect), Quanzhou dialect, Zhangzhou dialect, and Taiwanese Minnan.-->

====Synonyms====
* {{l|en|Hoklo}}, {{l|en|Fukien}}, {{l|en|Fukienese}}

====Hypernyms====
* {{l|en|Min Nan}}, {{l|en|Minnan}}, {{l|en|Southern Min}}
* {{l|en|Quanzhou}}–[[Zhangzhou]], Chinchew–Changchew

====Hyponyms====
* {{l|en|Taiwanese}}
* {{l|en|Quanzhou}} dialect, Chinchew
* {{l|en|Xiamen}} dialect, [[Amoy]], Xiamenese
* {{l|en|Quanzhou}} dialect, Changchew

====Translations====
{{trans-top|dialect of the Chinese language}}
* Burmese: {{t|my|လက်ရှေစကား|sc=Mymr}}
* Chinese:
*: Cantonese: {{t|yue|福建話|sc=Hani}}, {{t|yue|福建话|tr=fuk1 gin3 waa6-2|sc=Hani}}, {{t|yue|閩南語|sc=Hani}}, {{t|yue|闽南语|tr=man5 naam4 jyu5|sc=Hani}}, {{t|yue|閩南話|sc=Hani}}, {{t|yue|闽南话|tr=man5 naam4 waa6-2|sc=Hani}}, {{t|yue|鶴佬話|sc=Hani}}, {{t|yue|鹤佬话|tr=hok3 lou2 waa6-2|sc=Hani}}, {{t|yue|福佬話|sc=Hani}}, {{t|yue|福佬话|tr=fuk1 lou2 waa6-2|sc=Hani}}
*: Hakka: {{t|hak|學老話|sc=Hani}}, {{t|hak|学老话|tr=Ho̍k-ló-fa|sc=Hani}}
*: Mandarin: {{t|cmn|福建話|sc=Hani}}, {{t|cmn|福建话|tr=Fújiànhuà|sc=Hani}}, {{t+|cmn|閩南語|sc=Hani}}, {{t+|cmn|闽南语|tr=Mǐnnányǔ|sc=Hani}}, {{t|cmn|福佬話|sc=Hani}}, {{t|cmn|福佬话|tr=Fúlǎohuà|sc=Hani}}
*: Min Nan: {{t|nan|福建話|sc=Hani}}, {{t|nan|福建话|tr=Hok-kiàn-ōe|sc=Hani}}, {{t+|nan|閩南語|sc=Hani}}, {{t+|nan|闽南语|tr=Bân-lâm-gú, Bân-lâm-gí|sc=Hani}}, {{t|nan|福佬話|sc=Hani}}, {{t|nan|福佬话|tr=Hok-ló-oē|sc=Hani}}, {{t|nan|河洛話|sc=Hani}}, {{t|nan|河洛话|tr=Hō-ló-oē, Ho̍h-ló-oē|sc=Hani}}, {{t|nan|咱人話|sc=Hani}}, {{t|nan|咱人话|tr=Lán-lâng-ōe|sc=Hani}} {{qualifier|Quanzhou, Zhangzhou}}, {{t|nan|咱厝話|sc=Hani}}, {{t|nan|咱厝话|tr=Lán-chhù-ōe|sc=Hani}} {{qualifier|Quanzhou, Zhangzhou}}
* Indonesian: {{t+|id|bahasa Hokkien}}
* Japanese: {{t+|ja|福建語|tr=ふっけんご, fukkengo}}
{{trans-mid}}
* Khmer: {{t|km|ហុកកៀន|tr=hok kien|sc=Khmr}}, {{t|km|ចិនហុកគៀន|tr=chən hok kien|sc=Khmr}}
* Lao: {{t-needed|lo}}
* Malay: {{t|ms|bahasa Hokkien}}
* Portuguese: {{t|pt|hokkien|m}}
* Russian: {{t|ru|хо́ккиен|m}}, {{t|ru|фуцзяньхуа́|m}}, {{t|ru|фуцзя́ньский|m}}
* Thai: {{t|th|ภาษาจีนฮกเกี้ยน|tr=paasăa jeen hókgîan}}
* Vietnamese: {{t|vi|tiếng Mân Nam}}
{{trans-bottom}}

{{trans-see|Min Nan}}

====Related terms====
* {{l|en|Fujian}}

====See also====
* Other branches of Min Nan (limited mutual intelligibility): [[Teochew]] (Chaoshan Division); Zhenan Min Division; Zhongshan Min Division; Qiongwen Division; Leizhou Min Division; Longyan Min Division

===Further reading===
* {{ethnologue|code=nan}}

[[Category:en:Languages]]
"""

    def test_WiktEntryCJKV_languages_exist(self):
        method_expectedvalue = [('chinese', '==Chinese'), ('japanese', "==Japanese"), ('korean', "==Korean"), ('vietnamese', "==Vietnamese")]
        cjkv = WiktEntryCJKV()

        for lang_method, expected in method_expectedvalue:
            with self.subTest(text=lang_method):
                lang_section = getattr(cjkv, lang_method)(self.cjkv)
                actual = lang_section[:len(expected)]
                self.assertEqual(expected, actual)

    def test_WiktEntryCJKV_languages_exceptions(self):
        methods = ['chinese', 'japanese', 'korean', 'vietnamese']
        cjkv = WiktEntryCJKV()

        for method in methods:
            with self.subTest(text=method):
                with self.assertRaises(ValueError):
                    getattr(cjkv, method)(self.no_cjkv)


if __name__ == '__main__':
    unittest.main()
