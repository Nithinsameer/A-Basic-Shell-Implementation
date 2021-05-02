from datetime import date

import os

import shutil

today = date.today()

print("\n")

print(".......CDSS PROJECT BASIC SHELL.......")

print("\n")

def mufunc():

    while(True):

        try:

            entry = str(input("$nithinsameer@-nithinsameer$:"))

            #####----functions for all the commands---####
            def name():

                print(os.name)

            def date():

                print("Today's date is", today)



            def cmd(cmd):

                 os.system(entry)

            def pwd():#present working directory

                print(os.getcwd())


            def pid():

                pid = os.getpid()

                print(pid)



            if entry == "name":

                name()

            elif entry =="date":

                date()
            elif entry =="gid":

                print(os.getgid())



            elif entry=="pwd":

                pwd()

            elif entry=="pid":

                pid()



            elif entry =="ls":

                #os.system('ls')
                print(os.system("ls"))

            elif entry =="echo":

                a = str(input(""))

                print("\n",a)

            elif entry =="isdir":

                directory = str(input(""))

                isfile = os.path.isdir(directory)

                print("\n")

                print(isfile)

            elif entry =="cat":

                try:


                    file0 = str(input(""))

                    f = open(file0,"w+")

                    f.close()


                except OSError as error:

                    print(error)

            elif entry =="Cat":

                try:


                    file0 = str(input(""))

                    f = open(file0,"r+")

                    contents = f.read()

                    for content in contents:

                        print(content,end ="")


                    f.close()


                except OSError as error:

                    print(error)




            elif entry =="rm":#remove

                try:

                    file0 = str(input(""))

                    os.remove(file0)

                except OSError as error:

                    print(error)

            elif entry =="cp":#copy

                try:

                    a = str(input(""))

                    b = str(input(""))

                    shutil.copy(a,b)

                except OSError as error:

                    print(error)

            elif entry =="mv":#move basefile destination file

                try:

                    a = str(input(""))

                    b = str(input(""))

                    shutil.move(a,b)

                except OSError as error:

                    print(error)



            elif entry =="isfile":#to check whether the file is present or not

                file1 = str(input(""))

                isfile = os.path.isfile(file1)

                print("\n")

                print(isfile)



            elif entry =="mkdir":# make directory

                directory = str(input(""))

                try:
                    os.mkdir(directory)

                    print("Directory '%s' created" %directory)

                except OSError as error:

                    print(error)


            elif entry== "rmdir": #remove directory

                directory = str(input(""))

                try:
                    os.rmdir(directory)

                    print("Directory '%s' removed" %directory)

                except OSError as error:

                    print(error)


            elif entry == "exit":

                break

            else:

                print("\n$Bash!!.. command not found..")

        except OSError as error:

            print(error)

mufunc()