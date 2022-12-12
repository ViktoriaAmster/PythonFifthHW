def codingRLE (sourceData: str):
    newData = ''
    lenOfData = 0
    while lenOfData < len(sourceData):
        count = 1
        while (lenOfData + 1 < len(sourceData)) and (sourceData[lenOfData + 1] == sourceData[lenOfData]):
            count += 1
            lenOfData += 1
        newData = newData + str(count) + sourceData[lenOfData]
        lenOfData += 1
    print(newData)
    return newData


def decodingRLE (data_):
    deCod = ''
    lenOfData = 0
    count = ''
    for i in data_:
        if i.isdigit():
            count = count + i
        else:
            deCod = deCod + (i * int(count))
            count = ''
    print(deCod)

sourceFile = r'file.txt'
with open(sourceFile, 'r') as ourFile:
    data_ = ourFile.read()
print(data_)
decodingRLE(codingRLE(data_))

