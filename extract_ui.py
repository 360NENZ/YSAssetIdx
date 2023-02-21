# this is just for fun
import json, requests
import urllib.request, zipfile, subprocess

with open('output_assetindex.json', 'r') as f:
    ai = json.load(f)

avatarIcon = "ART/UI/Atlas/ItemIcon/UI_AvatarIcon_"
gachaImg = "ART/UI/Atlas/GachaSlotImg/UI_Gacha_AvatarImg_"

weaponPlusItem = "ART/UI/Atlas/ItemIcon/UI_EquipIcon_Bow_Amos"
weaponPlusItemEnd = "ART/UI/Atlas/ItemIcon/UI_Mall_Purchase_Blessofmoon"

firstIconIdx = 0
lastIconIdx = 9876543210

firstGachaIdx = 0
lastGachaIdx = 9876543210

firstWeaponIdx = 0
lastWeaponIdx = 9876543210

for i in ai["SubAssets"].keys():
    """
    if firstIconIdx == 0:
        if avatarIcon in ai["SubAssets"][i][0]["Name"]:
            firstIconIdx = i
    
    if avatarIcon in ai["SubAssets"][i][0]["Name"]:
        lastIconIdx = i
    
    if firstGachaIdx == 0:
        if gachaImg in ai["SubAssets"][i][0]["Name"]:
            firstGachaIdx = i
    
    if gachaImg in ai["SubAssets"][i][0]["Name"]:
        lastGachaIdx = i
    """

    if weaponPlusItem == ai["SubAssets"][i][0]["Name"]:
        firstWeaponIdx = i

    if weaponPlusItemEnd == ai["SubAssets"][i][0]["Name"]:
        lastWeaponIdx = i


blks = []

"""
for i in range(int(firstIconIdx), int(lastIconIdx) + 1):
    blks.append(ai["Assets"][str(i)]["Id"])

for i in range(int(firstGachaIdx), int(lastGachaIdx) + 1):
    blks.append(ai["Assets"][str(i)]["Id"])
"""

for i in range(int(firstWeaponIdx), int(lastWeaponIdx)):
    blks.append(ai["Assets"][str(i)]["Id"])

blks = ['{0:0>8}'.format(i) for i in list(set(blks))]

print(blks)

for blk in blks:
    url = f"https://autopatchhk.yuanshen.com/client_game_res/3.5_live/output_12691481_708ada59fe/client/StandaloneWindows64/AssetBundles/blocks/00/{blk}.blk"

    r = requests.get(url)

    f = open(f"./blk/{blk}.blk", 'wb')
    f.write(r.content)
    f.close()

asset_studio = "https://github.com/paimooon/YSRes/files/10318744/net472.zip"

urllib.request.urlretrieve(asset_studio, "studio.zip")
zipfile.ZipFile("studio.zip", 'r').extractall("./studio/")

for blk in blks:
    subprocess.run(["./studio/AssetStudioCLI.exe", f"./blk/{blk}.blk", "./Texture2D/", "--game", "GI", "--ai_file", "./output_assetindex.json", "--type", "Texture2D"])
    