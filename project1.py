import csv


def write(info):
     with open('student_info.csv','w+',newline='') as f1:
          wr=csv.writer(f1)

          wr.writerow(["Name","Age","Contact_Number","Email_ID"])
     

          wr.writerow(info)


if __name__=='__main__':
     c=True
     n=1
     while(c):
          s=input("Enter the student information for student #{} in the following format: (Name Age Contact_Number Email_ID):\n".format(n))
          s_list=s.split(' ')

          print("\nThe entered information is -\nName:  {}\nAge:  {}\nContact_Number:  {}\nEmail_ID:  {}"
                .format(s_list[0],s_list[1],s_list[2],s_list[3]))

          ck=input("Is the entered information correct? (Y/N): ")

          if ck=="Y":
               write(s_list)

               c1=input("Enter (Y/N) if you want to input information for another student:\n")
               if c1=="Y":
                    c=True
                    n+=1
               elif c1=="N":
                    c=False


          elif ck=="N":
               print("\nPlease re-enter the values")
      
               




        

