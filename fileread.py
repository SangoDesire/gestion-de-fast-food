from tkinter import *
root=Tk()
fw = open("../Sample/sample.txt", "w")
fw.write("je suis entrain decrire dans mon fichier creer\n ")
fw.write("je reecris dans mon fichier creer deuxième fois \n ")
fw.close()

#**************************** except handling********************
while True:
    try:
        number = int(input("what is your favorite housey no? \n"))
        print(18 / number)
        break
    except ValueError:
        print("Make sure and enter a number ")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break

    finally:
        print("Loop complete")








