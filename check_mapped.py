import hashlib, json

mapped = {
    "1042309217394": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Albedo",
    "473681934875": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Alhatham",
    "946022066083": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Aloy",
    "785286258389": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Ambor",
    "835731809233": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_AmborCostumeWic",
    "277577329107": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Ayaka",
    "749862458876": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Ayato",
    "1046362094481": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Barbara",
    "25534756429": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Beidou",
    "427685508677": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Bennett",
    "732918771057": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Candace",
    "904500532120": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Chongyun",
    "605627160067": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Collei",
    "877860029262": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Cyno",
    "12122280200": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Diluc",
    "431788816910": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Diona",
    "922088853693": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Dori",
    "274470525294": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Eula",
    "447669190512": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Faruzan",
    "684854510503": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Feiyan",
    "214989448805": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Fischl",
    "825678894536": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Ganyu",
    "206065037160": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Gorou",
    "297804648619": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Heizo",
    "963247744232": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Hutao",
    "854897602155": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Itto",
    "499988100774": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Kaeya",
    "39735012131": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Kazuha",
    "563316376606": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Keqing",
    "1049031365179": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Klee",
    "477851122337": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Kokomi",
    "140071354591": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Layla",
    "1073550944859": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Lisa",
    "199547022230": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Mona",
    "392616996388": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_MonaCostumeWic",
    "774107336447": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Nahida",
    "287333874699": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Nilou",
    "543924713185": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Ningguang",
    "238347703458": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Noel",
    "848919837478": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Qin",
    "65888889995": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_QinCostumeWic",
    "768433745742": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Qiqi",
    "841526146027": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Razor",
    "929682762700": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Rosaria",
    "1322171893": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_RosariaCostumeWic",
    "145353165708": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Sara",
    "1037799041788": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Sayu",
    "1057021090451": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Shenhe",
    "316043044519": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Shinobu",
    "107311159123": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Shougun",
    "216788343221": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Sucrose",
    "97665877161": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Tartaglia",
    "350813596685": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Tighnari",
    "1004435191584": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Tohma",
    "791325476555": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Venti",
    "968776755473": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Wanderer",
    "759702221843": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Xiangling",
    "792831116348": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Xiao",
    "740869541794": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Xingqiu",
    "928732280866": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Xinyan",
    "7128980643": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Yae",
    "468352599067": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Yaoyao",
    "38873359887": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Yelan",
    "682256853693": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Yoimiya",
    "750114103264": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Yunjin",
    "466440488192": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarIcon_Zhongli",
    "363960273266": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Albedo",
    "746695013531": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Alhatham",
    "286410797995": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Aloy",
    "77548430500": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Ambor",
    "747250651579": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Ayaka",
    "778468255250": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Ayato",
    "915620527091": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Barbara",
    "419578863189": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Beidou",
    "198163363759": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Bennett",
    "2752998701": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Candace",
    "199616559934": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Chongyun",
    "1095500167355": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Collei",
    "575499981817": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Cyno",
    "706730428356": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Diluc",
    "246088268312": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Diona",
    "809215419176": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Dori",
    "253494852278": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Eula",
    "622514517691": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Faruzan",
    "62163122498": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Feiyan",
    "1066237005561": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Fischl",
    "343401226033": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Ganyu",
    "331899379240": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Gorou",
    "119843081059": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Heizo",
    "929802017017": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Hutao",
    "1081032396746": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Itto",
    "358979393636": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Kaeya",
    "929760447282": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Kazuha",
    "782556886873": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Keqing",
    "89765275088": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Klee",
    "989337344155": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Kokomi",
    "835005298605": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Layla",
    "603594485101": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Lisa",
    "740500943507": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Mona",
    "193660448670": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Nahida",
    "877147122354": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Nilou",
    "798333514230": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Ningguang",
    "422736908593": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Noel",
    "118754362983": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Qin",
    "508549374247": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Qiqi",
    "151333293430": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Razor",
    "726541148276": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Rosaria",
    "686583136591": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Sara",
    "423069185881": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Sayu",
    "695579896452": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Shenhe",
    "308972304649": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Shinobu",
    "125208832301": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Shougun",
    "235188432797": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Sucrose",
    "53711716576": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Tartaglia",
    "879191726529": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Tighnari",
    "653759469314": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Tohma",
    "701172667543": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Venti",
    "587420965713": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Wanderer",
    "771499910821": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Xiangling",
    "387019389467": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Xiao",
    "633398919570": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Xingqiu",
    "876525684309": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Xinyan",
    "961034544969": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Yae",
    "1031264553862": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Yaoyao",
    "456810556887": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Yelan",
    "49304494290": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Yoimiya",
    "494391965454": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Yunjin",
    "301776228001": "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_Zhongli",
}


with open('output_assetindex.json', 'r') as f:
    ai = json.load(f)
    
typeList = list(set(ai["Types"].values()))

def compute_name_hash(path, t):
    path = (path + t).encode('ascii')
    pad = ((len(path) >> 8) + 1) << 8
    bts = path + bytes([0] * (pad - len(path)))
    m = hashlib.md5()
    m.update(bts)
    output = m.digest()
    num = 0
    for i in range(4, -1, -1):
        num <<= 8
        num |= output[i]
    return num
    
if __name__ == '__main__':
    for i in mapped.keys():

        if mapped[i] == "":
            continue

        flag = False
        for t in typeList:
            if compute_name_hash(mapped[i], t) == int(i):
                # print(f"{i}: {mapped[i]}") 
                flag = True
                break

        if flag == False:
            print(f"{i} is not correct")