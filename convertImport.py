def dayOneInput():
    input = ""
    with open('C:\\Users\\Jean-Luca\\Desktop\\test folder\\Advend\\input.txt') as f:
        IDs = f.read()
        newIDs = IDs.split()
        firstList = []
        secondList = []
        for i in range(len(newIDs)):
            if(i % 2 == 0):
                firstList.append(newIDs[i])
            else:
                secondList.append(newIDs[i])
    return [firstList,secondList]

def dayTwoInput():
    input = ""
    with open('C:\\Users\\Jean-Luca\\Desktop\\test folder\\Advend\\dayTwoInput.txt') as f:
        records = f.read()
        splitRecords = records.split("\n")
        recordsList = []
        for record in splitRecords:
            recordsList.append(record.split())
        return recordsList
    
def dayThreeInput():
    with open('C:\\Users\\Jean-Luca\\Desktop\\test folder\\Advend\\dayThreeInput.txt') as f:
        return f.read()