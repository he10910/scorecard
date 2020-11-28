import json

with open("setting.json" , "r" , encoding="utf-8") as jfile:
    jdata = json.load(jfile)

subject = jdata["subject"]    #自定義科目
student = jdata["student"]    #自定義人名

allsub = len(subject)
allstu = len(student)
stulist = " ".join(str(student))

def sublist():
    for i in range(allsub) :
        print("{:^10s}".format(str(subject[i])),end="")
    return ""

reportcard = [[0 for i in range(allsub)] for j in range(allstu)  ]                    #成績單初始化

for i in range(allstu):
    for j in range(allsub):
        reportcard[i][j] = input(f"{student[i]} {subject[j]}:")  #設定數值
print("-"*10)

def subava(sub):                            #獲得單科平均
    s = 0
    n = 0
    while n+1 <= allstu:
        s += int(reportcard[n][sub])
        n += 1
    return "{:.2f}".format(s/allstu)

n = 0      
tmplist = []                           #製作科目平均列表
while n+1 <= allsub:
    tmplist.append("{:^10s}".format(str(subava(n))))
    n += 1
subavelist = "".join(tmplist)

def scoreline(whos):                           #獲得成績排序
    for i in range(allsub):
        print("{:^10s}".format(str(reportcard[whos][i])),end = "")
    return ""
def allplus(whos):                            #獲得單人總分
    s = 0
    n = 0
    while n+1 <= allsub:
        s += int(reportcard[whos][n])
        n += 1
    return s

n = 0                         #全科總分
s = 0
for i in range(allstu):
    for j in range(allsub):
        s += int(reportcard[i][j])
allsubplus = s

allsubave = "{:.2f}".format(allsubplus/(allsub*allstu))     #全科平均

print("{0:^10s}{1}{2:^10s}{3:^10s}".format("name",sublist(),"total","avarage"))

for i in range(allstu):                        #中間
    print("{0:^10s}{1}{2:^10d}{3:^10.2f}".format(student[i],scoreline(i),allplus(i),allplus(i)/allsub))

print("{0:^10s}{1}{2:^10s}{3:^10s}".format("avarage",subavelist,"XX",allsubave))
