import os
import pickle


def addrecord():
    print()
    print("Adding a new Record")
    print("===================")
    f=open("covid19.dat",'ab')
    adhaar_no=input("Enter adhaar no.(less than 7 characters expected):")
    name=input("Enter name of patient(in not more than 20 characters):")
    phn_no=input("Enter phone no. of patient")
    address=input("Enter address of the patient(in not more than 24 characters):")
    sex=input("Enter MALE/FEMALE/OTHER:")
    age=int(input("Enter age of the patient:"))
    vac=int(input("enter no. of vaccines taken(0/1/2):"))
    v=""
    if vac>0:
        for i in range(vac):
            v1=input("enter name of vaccine(covisheild/covaxin)(please enter all letters in lower case):")
            v2=int(input("enter number of doses taken(1/2):"))
            if v2==2:
                v+=v1+','
            else:
                v+=v1+'(dose1)'+','
    else:
        v="no vaccine taken"        
            
    dis=input("Enter district of patient:")
    wd=int(input("enter ward number:"))
    rec=[adhaar_no,name,phn_no,address,sex,dis,wd,age,v]
    pickle.dump(rec,f)
    f.close()
    print("Record saved!")
    input("Press any key to continue")

def search():
    print("Search a Record")
    print("===================")
    f=open("covid19.dat",'rb')
    r=input("Enter adhaar no. to search:")
    while True:
        try:
            rec=pickle.load(f)
            if rec[0]==r:
                print("Adhaar no.=",rec[0])
                print("Name=",rec[1])
                print("phone no.=",rec[2])
                print("address=",rec[3])
                print("sex=",rec[4])
                print("district=",rec[5])
                print("ward no=",rec[6])
                print("age=",rec[7])
                print("vaccination taken",rec[8])
        except EOFError:
            break
    f.close()
    input("Press any key to continue")


def display():
     print()
     print("\t\t\t\t\t\t\t\t LIST OF ALL COVID POSITIVE CASES")
     print("="*167)
     f=open("covid19.dat",'rb')
     i=0
     print ("{:<1} {:<6} {:<0} {:<21} {:<1} {:<11} {:<1} {:<25} {:<1} {:<7} {:<1} {:<19} {:<2} {:<4} {:<1} {:<3} {:<1} {:34} {:1}".format
            ('| ','AADHAR','| ','NAME','| ','PHONE.','| ','ADDRESS','| ','SEX','| ','DISTRICT','| ','WARD','| ','AGE','| ','VACCINATION STATUS','| '))
     print("="*167)
     while True:
         try:
             rec=pickle.load(f)
             aadar,name,ph,add,sex,dis,wd,age,v=rec
             print ("{:<1} {:<6} {:<0} {:<21} {:<1} {:<11} {:<1} {:<25} {:<1} {:<7} {:<1} {:<19} {:<2} {:<4} {:<1} {:<3} {:<1} {:34} {:1}".format
                    ('| ',aadar,'| ',name,'| ',ph,'| ',add,'| ',sex,'| ',dis,'| ',wd,'| ',age,'| ',v,'| '))
             print("="*167)
             i+=1
         except EOFError:
             break
     f.close()
     print("Total no. of records",i)
     input("Press any key to continue")


def age():
    f=open("covid19.dat",'rb')
    c1=0
    c2=0
    c3=0
    c4=0
    while True:
        try:
            rec=pickle.load(f)
            if int(rec[7])<18:
                c1+=1
            elif rec[7]>=18 and rec[7]<45:
                c2+=1
            elif rec[7]>=45 and rec[7]<=60:
                c3+=1
            elif rec[7]>60:
                c4+=1
       
        except EOFError:
            break
    print("Covid patients below age of 18",c1),print("Covid patients between age of 18 and 45",c2),print("Covid patients between age of 45 and 60",c3)
    print("Covid patients above 60 ",c4)
    f.close()
    input("Press any key to continue")



def vaceff():
    f=open("covid19.dat",'rb')
    c=0
    t=0
    s=0
    n=0
    while True:
        try:
            co=0
            rec=pickle.load(f)
            if 'covaxine,covisheild,'==rec[8] or 'covisheild,covaxine,'==rec[8]:
                t+=1
                co=1
            if 'covaxine,'==rec[8]or 'covisheild(dose1),covaxine,'==rec[8]or'covaxine,covisheild(dose1),'==rec[8]:
                c+=1
                co=1
            if 'covisheild,'==rec[8]or'covaxine(dose1),covisheild,'==rec[8]or'covisheild,covaxine(dose1),'==rec[8]:
                s+=1
                co=1    
            if co==0:
                n+=1
        except EOFError:
             break
    print("no. of people affected after taking both vaccines:",t)
    print("no. of people affected after two doses of covaxin:",c)
    print("no. of people affected after taking two doses of covisheild:",s)
    print("no. of people affected without taking both the doses of covaxin and covisheild:",n)
    f.close()
    input("Press any key to continue")


def mainmenu():
    ch=0
    while True:
        print("\n")
        print("Main Menu")
        print("==========")
        print(" 1. Add a new Record")
        print(" 2. Search a patient's Record")
        print(" 3. List all patient's Records")
        print(" 4. Display no. of positive cases age wise")
        print(" 5. Display no. of people affected after vaccination")
        print(" 0. Exit")
        ch=int(input('Enter your choice:'))
        if ch==1:
            addrecord()
        elif ch==2:
            search()
        elif ch==3:
            display()
        elif ch==4:
            age()
        elif ch==5:
            vaceff()
        elif ch==0:
            print("Software Terminated")
            break
        

mainmenu()