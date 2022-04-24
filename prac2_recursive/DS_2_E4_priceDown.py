menuDict = {'콩나물 해장국':4500,'갈비탕':9000,'돈가스':8000}
menuDict['팟타이'] = 7000

for key in menuDict.keys() :
    menuDict[key] -= 500
    
print(menuDict)