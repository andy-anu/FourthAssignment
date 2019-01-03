myUniqueList = []
myLeftovers=[]
def addtoList(Number):
    if len(myUniqueList) == 0:
        myUniqueList.append(Number)
        print("myUniqueList :",myUniqueList)
        return True
    else:
        myLeftovers.append(Number)
        print("myLeftovers :",myLeftovers)
        return False


addtoList(6)
addtoList(8)
addtoList(10)
