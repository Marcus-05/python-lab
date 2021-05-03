dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
finaldict = {}

finaldict.update(dic1)
finaldict.update(dic2)
finaldict.update(dic3)
print(finaldict)

for values in finaldict:
    print(f"key : {values } value : {finaldict[values]}")
