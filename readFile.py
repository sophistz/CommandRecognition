def getStrTargetList(file):
    targetList = []
    for line in open(file):
        targetList.append(line.split())
    return targetList
