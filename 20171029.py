a=0
for x in range(1,5):
    for y in range(1,5):                
        for z in range(1,5):
            if x!=y and y!=z and x!=z:
                a+=1
                print (str(x)+str(y)+str(z))
                print ('%d %d %d') %(x,y,z)
                print a


h=input("high:")
w=input("weight:")
bmi=float(w)/(float(h)*float(h))
if bmi<18.5:
    print "����BMIָ��Ϊ��%.2f  ����ƫ��" % bmi
elif bmi>=24:
    print "����BMIָ��Ϊ��%.2f  ����ƫ��" % bmi
else:
    print "����BMIָ��Ϊ��%.2f  ��������" % bmi


#-*- coding:utf-8 -*-
import random
total=0
a=0
while True:
    num=random.randint(1,100)
    x=input("�Ƿ������Ϸ��1:���� 2���˳�\n")
    if str(x)=='1':
        total +=1
        print total
        print "who is it:"
        while True:
            a +=1
            ans=input()
            if ans<num:
                print "too small"
            elif ans>num:
                print "too big"
            else:
                print "bingo"
                break
        
    elif str(x)=='2':
        break
    
    if total>0:
        agv=a/total
        print agv


     
     






