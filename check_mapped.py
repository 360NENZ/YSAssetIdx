import hashlib, json

mapped = {
    "371373618540": "ART/UI/Atlas/GachaSlotImg/UI_Costume_AmborCostumeWic",
    "656244161384": "ART/UI/Atlas/GachaSlotImg/UI_Costume_AyakaCostumeBruhling", # test
    "1092633568505": "ART/UI/Atlas/GachaSlotImg/UI_Costume_BarbaraCostumeSummertime",
    "253200261877": "ART/UI/Atlas/GachaSlotImg/UI_Costume_DilucCostumeFlamme",
    "154775512325": "ART/UI/Atlas/GachaSlotImg/UI_Costume_FischlCostumeHighness",
    "1098632683755": "ART/UI/Atlas/GachaSlotImg/UI_Costume_KeqingCostumeFeather",
    "228158811228": "ART/UI/Atlas/GachaSlotImg/UI_Costume_LisaCostumeStudentin",
    "983654557316": "ART/UI/Atlas/GachaSlotImg/UI_Costume_MonaCostumeWic",
    "627358202102": "ART/UI/Atlas/GachaSlotImg/UI_Costume_NingguangCostumeFloral",
    "878193737078": "ART/UI/Atlas/GachaSlotImg/UI_Costume_QinCostumeSea",
    "1058334083707": "ART/UI/Atlas/GachaSlotImg/UI_Costume_QinCostumeWic",
    "753231826581": "ART/UI/Atlas/GachaSlotImg/UI_Costume_RosariaCostumeWic",
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