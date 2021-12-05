from dataclasses import dataclass

@dataclass
class BinaryData:
    zero: int = 0
    one : int = 0
    
filename = "./input.txt"

with open(filename, "r") as f:
    content = f.read()

GammaNum = '            '
EpsilonNum = '            '
mylist = [BinaryData() for i in range(12)]

def CreateBinaryNumber():
    global GammaNum
    global EpsilonNum
    for counter, i in enumerate(mylist):
        if i.one > i.zero:
           GammaNum = GammaNum[:counter] + "1" + GammaNum[counter+1:]
           EpsilonNum = EpsilonNum[:counter] + "0" + EpsilonNum[counter+1:]
        else:
            GammaNum = GammaNum[:counter] + "0" + GammaNum[counter+1:]
            EpsilonNum = EpsilonNum[:counter] + "1" + EpsilonNum[counter+1:]
        print("ones: " , i.one, " Zeros: ", i.zero)

for item in content.split("\n"):
    for i in range(12):
         if item[i] == "0":
            mylist[i].zero = mylist[i].zero + 1
         else:
            mylist[i].one = mylist[i].one + 1
CreateBinaryNumber()
# 2 is for base 2 to convert binary to decmial
print(int(GammaNum, 2))
print(int(EpsilonNum,2))
print("Answer")
print(int(GammaNum, 2) * int(EpsilonNum,2))
