from zhmodules import ZhModuleDataPage

import argparse
import json
import re

# see sample input at the bottom of the file
regex_dialsyn = re.compile(r'^\s+\["(.+)"]\s+=\s*[{"](.*)["}],*$')


def lua2dict(lua_export: str):
    dialsyn_dict = {}
    for line in lua_export.split('\n'):
        kvpair = re.match(regex_dialsyn, line)
        if kvpair:
            dialsyn_dict[kvpair.group(1).strip()] = kvpair.group(2).strip().replace('"', '')

    return dialsyn_dict


def extract_dialectal_synonyms(infilepath, outfilepath):
    outdict = {}
    dsapi = ZhModuleDataPage()
    with open(infilepath, 'r') as infile:
        for line in infile:
            word = line.strip()
            lua_export = dsapi.get_synonym_data(word)
            outdict[word] = lua2dict(lua_export)

    with open(outfilepath, 'w', encoding='utf8') as outfile:
        json.dump(outdict, outfile,  ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infilepath", help="dialectal synonyms module data filepath", required=True)
    parser.add_argument("-o", "--outfilepath", help="dialectal synonyms output filepath", required=True)
    args = parser.parse_args()

    extract_dialectal_synonyms(args.infilepath, args.outfilepath)

"""
    export.list = {
        ["meaning"]		= "comet",
        ["note"]		= "",
        
        ["Classical"]	= { "彗星", "帚星", "欃槍", "掃星" },
        ["Formal"]		= { "彗星" },
        ["Taxonomic"]	= { "" },
        
        ["Beijing"]		= { "掃帚星" },
        ["Taiwan"]		= { "掃帚星", "掃把星" },
        ["Tianjin"]		= { "" },
        ["Harbin"]		= { "掃帚星" },
        ["Shenyang"]	= { "" },
        ["Hailar"]		= { "掃把星" },
        ["Ulan Hot"]	= { "掃把星" },
        ["Tongliao"]	= { "掃把星" },
        ["Chifeng"]		= { "掃帚星" },
        ["Bayanhot"]	= { "掃帚星" },
        ["Jinan"]		= { "掃帚星" },
        ["Muping"]		= { "掃帚星" },
        ["Luoyang"]		= { "掃帚星" },
        ["Wanrong"]		= { "掃帚星" },
        ["Ronghe"]		= { "" },
        ["Xi'an"]		= { "掃帚星" },
        ["Qingdao"]		= { "掃帚星" },
        ["Zhengzhou"]	= { "掃帚星" },
        ["Xining"]		= { "掃帚星" },
        ["Xuzhou"]		= { "掃帚星" },
        ["Yinchuan"]	= { "掃帚星" },
        ["Lanzhou"]		= { "掃帚星" },
        ["Ürümqi"]		= { "掃帚星" },
        ["Wuhan"]		= { "掃帚星" },
        ["Huanggang"]	= { "" },
        ["Chengdu"]		= { "掃把星" },
        ["Guiyang"]		= { "掃把星" },
        ["Guilin"]		= { "掃帚星" },
        ["Liuzhou"]		= { "掃把星" },
        ["Kunming"]		= { "" },
        ["Yangzhou"]	= { "掃帚星" },
        ["Nanjing"]		= { "掃帚星" },
        ["Hefei"]		= { "" },
        ["Nantong"]		= { "掃帚星" },
        ["Malaysia-M"]	= { "" },
        ["Singapore-M"]	= { "" },
        ["Gansu-DG"]	= { "掃帚星" },
        ["Shaanxi-DG"]	= { "" },
        
        ["Taiyuan"]		= { "掃帚星", "掃星" },
        ["Pingyao"]		= { "掃帚星" },
        ["Xinzhou"]		= { "掃帚星" },
        ["Baochang"]	= { "亮星" },
        ["Jining"]		= { "掃帚星" },
        ["Hohhot"]		= { "掃帚星" },
        ["Baotou"]		= { "掃帚星" },
        ["Dongsheng"]	= { "掃帚星" },
        ["Linhe"]		= { "掃帚星" },
        ["Haibowan"]	= { "掃帚星" },
        
        ["Shanghai"]	= { "掃帚星" },
        ["Suzhou"]		= { "掃帚星" },
        ["Wuxi"]		= { "掃帚星" },
        ["Hangzhou"]	= { "掃帚星" },
        ["Chongming"]	= { "掃帚星" },
        ["Wenzhou"]		= { "搽掃星", "妖星" },
        ["Danyang"]		= { "掃帚星" },
        ["Jinhua"]		= { "掃帚星", "笤帚星" },
        ["Tangxi"]		= { "" },
        ["Ningbo"]		= { "掃帚星" },
        
        ["Changsha"]	= { "掃把星" },
        ["Shuangfeng"]	= { "" },
        ["Xiangtan"]	= { "" },
        ["Loudi"]		= { "掃帚星" },
        ["Quanzhou-X"]	= { "彗星" },
        
        ["Nanchang"]	= { "掃帚星" },
        ["Lichuan"]		= { "掃帚星" },
        ["Pingxiang"]	= { "掃把星" },
        
        ["Meixian"]		= { "祛把星" },
        ["Xingning"]	= { "掃把星" },
        ["Huizhou"]		= { "掃把星" },
        ["Huizhou-SK"]	= { "" },
        ["Huizhou-HL"]	= { "" },
        ["Huiyang"]		= { "" },
        ["Huidong-PS"]	= { "" },
        ["Huidong-DL"]	= { "星瀉屎" },
        ["Dongguan-H"]	= { "掃把星" },
        ["Longmen-PL"]	= { "" },
        ["Longmen-LX"]	= { "" },
        ["Boluo"]		= { "" },
        ["Shenzhen-H"]	= { "掃把星" },
        ["Zengcheng-ZG"]= { "" },
        ["Zhongshan-WGS"]	= { "掃把星" },
        ["Zhongshan-NLHS"]	= { "彗星" },
        ["Wuhua-SZ"]	= { "掃把星" },
        ["Wuhua-HC"]	= { "桿掃星", "掃把星" }, --桿掃星 written as 稈掃星
        ["Wuhua-CB"]	= { "人殃頭" },
        ["Wuhua-MY"]	= { "出人殃" },
        ["Heyuan"]		= { "" },
        ["Zijin-GZ"]	= { "" },
        ["Longchuan-TC"]= { "" },
        ["Longchuan-SD"]= { "" },
        ["Heping-LZ"]	= { "" },
        ["Lianping-ZX"]	= { "" },
        ["Lianping-LJ"]	= { "" },
        ["Qujiang"]		= { "掃把星" },
        ["Xinfeng-MT"]	= { "" },
        ["Xinfeng-DX"]	= { "" },
        ["Xiaosanjiang"]= { "天星過位" },
        ["Liannan"]		= { "" },
        ["Conghua-H"]	= { "彗星" },
        ["Jiexi"]		= { "" },
        ["Luchuan-LC"]	= { "" },
        ["Luchuan-DQ"]	= { "掃把星" },
        ["Changting"]	= { "掃帚星" },
        ["Pingyu"]		= { "星瀉屎" },
        ["Wuping"]		= { "掃把星" },
        ["Liancheng"]	= { "掃把星" },
        ["Ninghua"]		= { "桿掃星" },
        ["Yudu"]		= { "掃星" },
        ["Ruijin"]		= { "芒掃星" },
        ["Shicheng"]	= { "桿掃星" },
        ["Shangyou"]	= { "芒掃星" },
        ["Taoyuan"]		= { "" },
        ["Miaoli"]		= { "掃把星", "長尾星" },
        ["Liudui"]		= { "掃把星", "長尾星" },
        ["Hsinchu"]		= { "掃把星" },
        ["Dongshi"]		= { "掃把星" },
        ["Raoping"]		= { "掃把星" },
        ["Yunlin"]		= { "掃把星" },
        ["Hong Kong-H"]	= { "掃把星" },
        ["Sabah-B"]		= { "" },
        ["Sabah-L"]		= { "" },
        ["Senai"]		= { "掃把星" },
        ["Singkawang"]	= { "" },
        
        ["Jixi"]		= { "笤帚星", "掃帚星" },
        ["Shexian"]		= { "" },
        ["Tunxi"]		= { "笤帚星" },
        ["Xiuning"]		= { "" },
        ["Yixian"]		= { "" },
        ["Qimen"]		= { "" },
        ["Wuyuan"]		= { "" },
        ["Fuliang"]		= { "" },
        ["Dexing"]		= { "" },
        ["Jingde"]		= { "" },
        ["Zhanda"]		= { "" },
        
        ["Guangzhou"]	= { "掃把星", "彗星" },
        ["Hong Kong"]	= { "掃把星", "彗星" },
        ["HK Weitou"]	= { "掃把星" },
        ["Kam Tin"]		= { "掃把星" },
        ["Ting Kok"]	= { "" },
        ["Tung Ping Chau"]= { "" },
        ["Macau"]		= { "掃把星" },
        ["Panyu"]		= { "掃把星", "彗星" },
        ["Huadu"]		= { "掃把星" },
        ["Conghua"]		= { "星賴屎" },
        ["Zengcheng"]	= { "掃扒星" },
        ["Foshan"]		= { "掃把星" },
        ["Nanhai"]		= { "鬼火" },
        ["Shunde"]		= { "掃把星" },
        ["Sanshui"]		= { "掃把星" },
        ["Gaoming"]		= { "彗星" },
        ["Zhongshan"]	= { "掃把星" },
        ["Zhuhai"]		= { "掃把星" },
        ["Doumen-T"]	= { "掃把星" },
        ["Doumen-S"]	= { "掃桿星" },
        ["Jiangmen"]	= { "掃把星" },
        ["Xinhui"]		= { "掃把星" },
        ["Taishan"]		= { "掃把星" },
        ["Kaiping"]		= { "掃桿星" },
        ["Enping"]		= { "掃桿星" },
        ["Heshan"]		= { "彗星" },
        ["Dongguan"]	= { "掃把星", "彗星" }, --彗星 written as 篲星
        ["Bao'an"]		= { "彗星" },
        ["Dapeng"]		= { "" },
        ["Shaoguan"]	= { "掃把星" },
        ["Yunfu"]		= { "掃把星" },
        ["Yangjiang"]	= { "掃把星", "掃宅星" },
        ["Xinyi"]		= { "掃把星" },
        ["Lianjiang"]	= { "掃把星" },
        ["Nanning"]		= { "掃把星" },
        ["Wuzhou"]		= { "掃把星" },
        ["Yulin"]		= { "掃桿星" },
        ["Hepu"]		= { "掃把星" },
        ["Kuala Lumpur"]= { "掃把星" },
        ["Ho Chi Minh City"]= { "掃把星" },
        
        ["Nanning-P"]	= { "掃把星" },
        ["Guilin-P"]	= { "掃巴星" },
        
        ["Xiamen"]		= { "掃帚星", "拖尾星", "歹星" },
        ["Tong'an"]		= { "" },
        ["Quanzhou"]	= { "掃帚星" },
        ["Jinjiang"]	= { "掃帚星" },
        ["Nan'an"]		= { "" },
        ["Shishi"]		= { "" },
        ["Hui'an"]		= { "" },
        ["Anxi"]		= { "" },
        ["Yongchun"]	= { "掃帚星", "賊星" },
        ["Dehua"]		= { "" },
        ["Zhangzhou"]	= { "掃帚星", "長尾星", "疶屎星", "落屎星", "反亂星", "反星" },
        ["Longhai"]		= { "" },
        ["Changtai"]	= { "" },
        ["Hua'an"]		= { "" },
        ["Nanjing-MN"]	= { "" },
        ["Pinghe"]		= { "" },
        ["Zhangpu"]		= { "" },
        ["Yunxiao"]		= { "" },
        ["Zhao'an"]		= { "" },
        ["Dongshan"]	= { "" },
        ["Taipei"]		= { "疶屎星", "掃帚星" },
        ["Kaohsiung"]	= { "掃帚星" },
        ["Tainan"]		= { "掃帚星" },
        ["Taichung"]	= { "掃帚星" },
        ["Wuqi"]		= { "" },
        ["Hsinchu-MN"]	= { "掃帚星", "疶屎星" },
        ["Taitung"]		= { "" },
        ["Lukang"]		= { "掃帚星" },
        ["Sanxia"]		= { "掃帚星" },
        ["Yilan"]		= { "掃帚星", "落屎星" },
        ["Kinmen"]		= { "掃帚星" },
        ["Magong"]		= { "掃帚星" },
        ["Malaysia-MN"]	= { "長尾星" },
        ["Singapore-MN"]	= { "掃帚星" },
        ["Philippine-MN"]	= { "" },
        ["Pingnan"]		= { "彗星" },
        ["Chaozhou"]	= { "掃帚星" },
        ["Shantou"]		= { "" },
        ["Haifeng"]		= { "掃茜星" },
        ["Thailand-MN-T"]	= { "彗星" },
        ["Johor Bahru"]	= { "彗星" },
        ["Wenchang"]	= { "" },
        ["Haikou"]		= { "掃把星" },
        ["Leizhou"]		= { "掃帚星" },
        
        ["Putian"]		= { "掃帚星" },
        ["Xianyou"]		= { "掃帚星" },
        
        ["Shaxi"]		= { "掃帚星" },
        ["Sanxiang"]	= { "掃把星" },
        
        ["Fuzhou"]		= { "掃帚星", "筅帚星" },
        ["Changle"]		= { "" },
        ["Fuqing"]		= { "掃帚星" },
        ["Pingtan"]		= { "" },
        ["Yongtai"]		= { "" },
        ["Gutian"]		= { "" },
        ["Fu'an"]		= { "" },
        ["Ningde"]		= { "" },
        ["Shouning"]	= { "" },
        ["Zhouning"]	= { "" },
        ["Fuding"]		= { "" },
        ["Matsu"]		= { "" },
        
        ["Jian'ou"]		= { "掃帚星" },
        ["Dikou"]		= { "" },
        ["Songxi"]		= { "" },
        ["Zhenghe"]		= { "" },
        ["Zhenqian"]	= { "" },
        ["Jianyang"]	= { "" },
        ["Wuyishan"]	= { "" },
        ["Shibei"]		= { "" },
        
        ["Fu'an-She"]	= { "" },
        ["Fuding-She"]	= { "" },
        ["Luoyuan-She"]	= { "" },
        ["Sanming-She"]	= { "" },
        ["Shunchang-She"]	= { "" },
        ["Hua'an-She"]	= { "" },
        ["Guixi-She"]	= { "" },
        ["Cangnan-She"]	= { "" },
        ["Jingning-She"]	= { "" },
        ["Lishui-She"]	= { "" },
        ["Longyou-She"]	= { "" },
        ["Chaozhou-She"]	= { "" },
        ["Fengshun-She"]	= { "" },
    }
    
    return export
"""