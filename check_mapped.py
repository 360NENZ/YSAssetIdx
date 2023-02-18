import hashlib, json

mapped = {
    "347916310387": "Data/_BinOutput/Ability/Temp/AvatarAbilities/ConfigAbility_Avatar_Lisa",
    "232447844481": "Data/_BinOutput/Ability/Temp/AvatarAbilities/ConfigAbility_Avatar_Mika",
    "376888510756": "Data/_BinOutput/Ability/Temp/AvatarAbilities/ConfigAbility_Avatar_Mona",
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