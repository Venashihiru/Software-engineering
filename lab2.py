file=open('TestFile.cpp','r')
file1=file.read().split()
print(file1)
length=len(file1)
print(length)

switch_num=0
int_num=0
double_num=0
long_num=0
case_num=0
default_num=0
break_num=0
if_num=0
else_num=0
elseif_num=0
return_num=0

#1
#switch
i=0
switch="switch"
for i in range(length):
    if file1[i].find(switch)>=0:
        switch_num+=1
        i+=1
#print(switch_num)
#int
i=0
int="int"
for i in range(length):
    if file1[i].find(int)>=0:
        int_num+=1
        i+=1
print(int_num)
#double
i=0
double="double"
for i in range(length):
    if file1[i].find(double)>=0:
        double_num+=1
        i+=1
print(double_num)
#long
i=0
long="long"
for i in range(length):
    if file1[i].find(long)>=0:
        long_num+=1
        i+=1
print(long_num)
#case
i=0
case="case"
for i in range(length):
    if file1[i].find(case)>=0:
        case_num+=1
        i+=1
#print(case_num)
#break
i=0
break1="break"
for i in range(length):
    if file1[i].find(break1)>=0:
        break_num+=1
        i+=1
print(break_num)
#default
i=0
default="default"
for i in range(length):
    if file1[i].find(default)>=0:
        default_num+=1
        i+=1
print(default_num)
#if
i=0
if1="if"
for i in range(length):
    if file1[i].find(if1)>=0:
        if_num+=1
        i+=1
#print(if_num)
#else
i=0
else1="else"
for i in range(length):
    if file1[i].find(else1)>=0:
        else_num+=1
        i+=1
print(else_num)
#return
i=0
return1="return"
for i in range(length):
    if file1[i].find(return1)>=0:
        return_num+=1
        i+=1
print(return_num)
total_num=switch_num+int_num+double_num+long_num+case_num+default_num+break_num+if_num+else_num+return_num
print("total num", total_num)
