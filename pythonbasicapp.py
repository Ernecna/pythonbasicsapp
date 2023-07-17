def calAverage(line):
 line=line[:-1] ## cancel for the spaces between lines
 list=line.split(":")
 name=list[0]
 grades=list[1].split(",")
 sum=0
 for x in grades:
  sum+=(int)(x)
 letgrad=""
 sum=sum/3
 if sum>90:
    letgrad="AA"
 elif 90>sum>80:
   letgrad="BA"
   
 elif 80>sum>70:
   letgrad="BB"

 elif 70>sum>60:
    letgrad="CB"
 elif 60>sum>50:
   letgrad="CC"
 else:
   letgrad="FF"

 return name+":"+ letgrad+"\n"

def readGradesAvg():
    with open("examgrades.txt","r",encoding="utf-8") as file:
        for line in file:
         print(calAverage(line),end="")



    


def entertheGrades():
    name=input("Name:")
    surname=input("SurName:")
    g1=input("grade1:")
    g2=input("grade2:")
    g3=input("grade3:")

    with open("examgrades.txt","a",encoding="utf-8") as file:
     file.write(name+' '+surname+':'+g1+','+g2+','+g3+"\n")




def recordtheGrades():
    with open("examgrades.txt","r",encoding="utf-8") as file:
       list=[]
       for i in file:
          list.append(calAverage(i))

       with open("result.txt","w",encoding="utf-8")as file2:
          for i in list:
             file2.write(i)








while True:
    command=input("1-Show grades\n 2-Enter grades\n3-Record the grades\n 4- EXIT\n")

    if command=="1":
        readGradesAvg()
    elif command=="2":
        entertheGrades()
    elif command=="3":
        recordtheGrades()
    elif command=="4":
        print("SUCCESFULLY EXIT YOU ENTERED 4")
        break;
    else:
        print("İNVALİD COMMAND")
        



