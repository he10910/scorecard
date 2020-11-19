import json
with open("reportcard\\scorecard\\setting.json" , "r" , encoding="utf-8") as jfile:
    jdata = json.load(jfile)

subject = jdata["subject"]    #自定義科目
student = jdata["student"]    #自定義人名

allsub = len(subject)
allstu = len(student)
#sublist = " ".join(subject)
stulist = " ".join(str(student))

p = []
n = 0
while n+1 <= allsub:
    p.append("{:^10s}".format(subject[n]))
    n += 1
sublist = f"{p[0]}{p[1]}"


reportcard = []                      #成績初始化
for i in range(allstu):
    reportcard.append([0]*allsub)

for i in range(allstu):
    for j in range(allsub):
        reportcard[i][j] = input(f"{student[i]}的{subject[j]}:")  #設定數值
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
subavelist = " ".join(tmplist)


def scoreline(whos):                           #獲得成績排序
    scoreline = " ".join(reportcard[whos])
    return scoreline

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

print("{:^10s}{}{:^10s}{:^10s}".format("名字", sublist , "總分" , "平均"))      #第一行title
for i in range(allstu):                        #中間
    print(student[i] , scoreline(i) , allplus(i) , "{:.2f}".format(allplus(i)/allsub))

print("{:^10s}{}{:^10s}{:^10s}".format("XX" , subavelist , "XX" , allsubave) )