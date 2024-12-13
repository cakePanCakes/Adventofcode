import convertImport

def safeincrease(report = []):
    for i in range(len(report)-1):
        if (int(report[i]) >= int(report[i+1]) or int(report[i+1]) > int(report[i])+3):
            return False
    return True

def safedecrease(report = []):
    for i in range(len(report)-1):
        if (int(report[i]) <= int(report[i+1]) or int(report[i+1]) < int(report[i])-3):
            return False
    return True

def dampener(report = []):
    if(safeincrease(report) or safedecrease(report)):
            return True
    
    for i in range(len(report)):
        tmp = report.pop(i)
        if(safeincrease(report) or safedecrease(report)):
            return True
        report.insert(i, tmp)
    return False
    
def safereports(data = []):
    safe = 0
    for report in data:
        if(safeincrease(report) or safedecrease(report)):
            safe+=1
    return safe

def safewithdampener(data = []):
    safe = 0
    for report in data:
        if(dampener(report) or dampener(report)):
            safe+=1
    return safe

#unusalData = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]
unusalData = convertImport.dayTwoInput()
print(safewithdampener(unusalData))