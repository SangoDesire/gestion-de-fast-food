from tkinter import *
import tkinter.messagebox
import random
import time
from PIL import Image, ImageTk
import webbrowser
import datetime


root=Tk()
root.geometry("13x750+0+0")
root.title(" GESTION DE FAST FOOD ")
root.configure(background="black")
root.iconbitmap('images/food.ico')

Tops=Frame(root,width=1350,height=100,bd=14,relief="groove")
Tops.pack()

f1=Frame(root,width=900,height=630,bg="black", bd=8,relief="groove")
f1.pack(side=LEFT)

f2=Frame(root, width=440,height=650,bd=8,relief="groove")
f2.pack(side=RIGHT)

fla=Frame(f1,width=900,height=330,bd=8,bg="white",relief="groove")
fla.pack(side=TOP)

f2a=Frame(f1,width=900,height=320,bd=8,relief="groove")
f2a.pack(side=TOP)

ft2=Frame(f2,width=440,height=650,bd=12,relief="groove")
ft2.pack(side=TOP)

fb2=Frame(f2,width=440,height=50,bd=16,relief="groove")
fb2.pack(side=BOTTOM)

flaa=Frame(fla,width=400,height=330,bd=16,relief="groove")
flaa.pack(side=LEFT)

flab=Frame(fla,width=400,height=330,bd=16,relief="groove")
flab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=320,bd=14,relief="groove")
f2aa.pack(side=LEFT)

f2ab=Frame(f2a,width=450,height=320,bd=14,relief="groove")
f2ab.pack(side=RIGHT)

Tops.configure(background="black")
f1.configure(background="black")
f2.configure(background="black")

lblInfo=Label(Tops, font=("Arial",24,"bold") , bg= "powder blue",
              text= " GESTION DE FAST FOOD " , justify="center",bd=16,padx=420,pady=20)
lblInfo.grid(row=0,column=0)

#************  lien vers un site de fast food *************
def lien_html():
    webbrowser.open('https://www.mcdonalds.com/us/en-us.html')

#===============================================================================
# Création de l'objet image
load = Image.open("images/fst1.jpg")
# Création de la photo à partir de l'objet image
photo = ImageTk.PhotoImage(load)

# Redimensionner l'image
load.thumbnail((10,12))
lbl_img = Label(Tops,image=photo, fg="blue", cursor="hand2",bg="black",
                pady=10,padx=0).place(x=0)
lbl_img1 = Label(Tops, text="contacts:\n 48049901\n 03741365",bg="orange",
                font=("courier New","12"),pady=26,padx=35).place(x=1104)
btnlien= Button(Tops, text="voir plus de menus",font=("courier New","8"),activebackground="orange",command=lien_html).place(x=968)

#================================== variables =================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
ReceiptRef = StringVar()
Paidtax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

E_Latta = StringVar()
E_Expresso = StringVar()
E_IcedLatta = StringVar()
E_valleCoffee = StringVar()
E_Cappuccino = StringVar()
E_AfricanCoffee = StringVar()
E_AmericanCoffee  = StringVar()
E_IcedCappuccino = StringVar()

E_CoffeeCake = StringVar()
E_RedVelvetCake = StringVar()
E_BlackForestCake = StringVar()
E_BostonCreamCake = StringVar()
E_LagosChocoCake = StringVar()
E_KillBurnCake = StringVar()
E_CarltonChocoCake = StringVar()
E_QueenParkCake = StringVar()

E_Latta.set("0")
E_Expresso.set("0")
E_IcedLatta.set("0")
E_valleCoffee.set("0")
E_Cappuccino.set("0")
E_AfricanCoffee.set("0")
E_AmericanCoffee.set("0")
E_IcedCappuccino.set("0")
E_CoffeeCake.set("0")
E_RedVelvetCake.set("0")
E_BlackForestCake.set("0")
E_BostonCreamCake.set("0")
E_LagosChocoCake.set("0")
E_KillBurnCake.set("0")
E_CarltonChocoCake.set("0")
E_QueenParkCake.set("0")

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")

DateofOrder.set(time.strftime("%d%m%y"))

# ================================= Drinks Checkbox  ===============================================
Latta = Checkbutton(flaa, text="Malta\t", variable=var1, onvalue=1, offvalue=0,
                        font=("arial", 18, "bold")).grid(row=0, sticky=W)
Expresso = Checkbutton(flaa, text="Expresso\t", variable=var2, onvalue=1, offvalue=0,
                           font=("arial", 18, "bold")).grid(row=1, sticky=W)
IcedLatta = Checkbutton(flaa, text="Malta_Sucré\t", variable=var3, onvalue=1, offvalue=0,
                            font=("arial", 18, "bold")).grid(row=2, sticky=W)
ValleCoffee = Checkbutton(flaa, text="Café_Colombien\t", variable=var4, onvalue=1, offvalue=0,
                             font=("arial", 18, "bold")).grid(row=3, sticky=W)
Cappuccino = Checkbutton(flaa, text="Cappuccino\t", variable=var5, onvalue=1, offvalue=0,
                             font=("arial", 18, "bold")).grid(row=4, sticky=W)
AfricanCoffee = Checkbutton(flaa, text="Café_Africain\t", variable=var6, onvalue=1, offvalue=0,
                                font=("arial", 18, "bold")).grid(row=5, sticky=W)
AmericanCoffee = Checkbutton(flaa, text="Café_Americain\t", variable=var7, onvalue=1, offvalue=0,
                                font=("arial", 18, "bold")).grid(row=6, sticky=W)
IcedCappuccino = Checkbutton(flaa, text="Cappucci_lait\t", variable=var8, onvalue=1, offvalue=0,
                                 font=("arial", 18, "bold")).grid(row=7, sticky=W)

# =============================== Cakes =================================================================
CoffeeCake = Checkbutton(flab, text="Gateau_au_café\t", variable=var9, onvalue=1, offvalue=0,
                            font=("arial", 18, "bold")).grid(row=0, sticky=W)
RedVelvetCake = Checkbutton(flab, text="Gateau_aufour\t", variable=var10, onvalue=1, offvalue=0,
                                font=("arial", 18, "bold")).grid(row=1, sticky=W)
BlackForestCake = Checkbutton(flab, text="Gateau_Oeuf\t", variable=var11, onvalue=1, offvalue=0,
                                  font=("arial", 18, "bold")).grid(row=2, sticky=W)
BostonCreamCake = Checkbutton(flab, text="Gateau_Crèmeux\t", variable=var12, onvalue=1, offvalue=0,
                                font=("arial", 18, "bold")).grid(row=3, sticky=W)
LagosChocoCake = Checkbutton(flab, text="Gateau_Lagos\t", variable=var13, onvalue=1, offvalue=0,
                                font=("arial", 18, "bold")).grid(row=4, sticky=W)
killburnChocoCake = Checkbutton(flab, text="Gateau_killBurn \t", variable=var14, onvalue=1, offvalue=0,
                                    font=("arial", 18, "bold")).grid(row=5, sticky=W)
CarltonChocoCake = Checkbutton(flab, text="Gateau_Carlton \t", variable=var15, onvalue=1, offvalue=0,
                                   font=("arial", 18, "bold")).grid(row=6, sticky=W)
QueenParkCake = Checkbutton(flab, text="Gateau_QueenPark\t", variable=var16, onvalue=1, offvalue=0,
                                font=("arial", 18, "bold")).grid(row=7, sticky=W)

# ================================= widgets for Drinks =============================================

txtLatta = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_Latta)
txtLatta.grid(row=0, column=1)
txtExpresso = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_Expresso)
txtExpresso.grid(row=1, column=1)
txtIcedLatta = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_IcedLatta)
txtIcedLatta.grid(row=2, column=1)
txtValleCoffee = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_valleCoffee)
txtValleCoffee.grid(row=3, column=1)
txtCappuccino = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_Cappuccino)
txtCappuccino.grid(row=4, column=1)
txtAfricanCoffee = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_AfricanCoffee)
txtAfricanCoffee.grid(row=5, column=1)
txtAmericanCoffee = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_AmericanCoffee)
txtAmericanCoffee.grid(row=6, column=1)
txtIcedCappuccino = Entry(flaa, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_IcedCappuccino)
txtIcedCappuccino.grid(row=7, column=1)

# *********************** Enter widgets for cake ***********************************************************
txtCoffeeCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_CoffeeCake)
txtCoffeeCake.grid(row=0, column=1)
txtRedVelvetCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_RedVelvetCake)
txtRedVelvetCake.grid(row=1, column=1)
txtBlackForestCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_BlackForestCake)
txtBlackForestCake.grid(row=2, column=1)
txtBostonCreamCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_BostonCreamCake)
txtBostonCreamCake.grid(row=3, column=1)
txtLagosChocoCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_LagosChocoCake)
txtLagosChocoCake.grid(row=4, column=1)
txtKillBurnCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_KillBurnCake)
txtKillBurnCake.grid(row=5, column=1)
txtCarltonChocoCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_CarltonChocoCake)
txtCarltonChocoCake.grid(row=6, column=1)
txtQueenParkCake = Entry(flab, font=("arial", 16, "bold"), bd=8, width=6, justify='left',textvariable=E_QueenParkCake)
txtQueenParkCake.grid(row=7, column=1)

# ******************************** Informations ***********************************
lblReceipt = Label(ft2, font=("arial", 12, "bold"), text = "RECU:", bd=2, anchor=W)
lblReceipt.grid(row=0, column=0, sticky=W)

txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

# *********************** Cost Items Informations **************************************
lblCostofDrinks = Label(f2aa, font=("arial", 16, "bold"), text="Coùt_des_Boissons", bd=8)
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks = Entry(f2aa, font=("arial", 11, "bold"), bd="8", justify=LEFT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1, sticky=W)

lblCostofCakes = Label(f2aa, font=("arial", 16, "bold"), text="Coût_des_Gateaux", bd=8)
lblCostofCakes.grid(row=1, column=0, sticky=W)
txtCostofCakes = Entry(f2aa, font=("arial", 11, "bold"), bd="8", justify=LEFT,textvariable=CostofCakes)
txtCostofCakes.grid(row=1, column=1, sticky=W)

lblServiceCharge = Label(f2aa, font=("arial", 16, "bold"), text="Charge service", bd=8)
lblServiceCharge.grid(row=2, column=0, sticky=W)
txtServiceCharge = Entry(f2aa, font=("arial", 11, "bold"), bd="8", justify=LEFT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2, column=1, sticky=W)

# ****************  payment Informations ********************************************

lblTax = Label(f2ab, font=("arial", 16, "bold"), text="Taxe", bd=8)
lblTax.grid(row=0, column=0, sticky=W)
txtTax = Entry(f2ab, font=("arial", 11, "bold"), bd="8", justify=LEFT,textvariable=Paidtax)
txtTax.grid(row=0, column=1, sticky=W)

lblSubTotal = Label(f2ab, font=("arial", 16, "bold"), text="Sous_Total", bd=8)
lblSubTotal.grid(row=1, column=0, sticky=W)
txtSubTotal = Entry(f2ab, font=("arial", 11, "bold"), bd="8", justify=LEFT,textvariable=SubTotal)
txtSubTotal.grid(row=1, column=1, sticky=W)

lblTotalCost = Label(f2ab, font=("arial", 16, "bold"), text="Coût_Total ", bd=8)
lblTotalCost.grid(row=2, column=0, sticky=W)
txtTotalCost = Entry(f2ab, font=("arial", 11, "bold"), bd="8", justify=LEFT,textvariable=TotalCost)
txtTotalCost.grid(row=2, column=1, sticky=W)

#  ************************ Methods Definition **************************************
def qExit():
        qExit = tkinter.messagebox.askyesno("Sortie du System ", "Souhaitez_Vous quittez l'Application? ")
        if qExit > 0:
            root.destroy()
        return

def reset():
    Paidtax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latta.set("0")
    E_Expresso.set("0")
    E_IcedLatta.set("0")
    E_valleCoffee.set("0")
    E_Cappuccino.set("0")
    E_AfricanCoffee.set("0")
    E_AmericanCoffee.set("0")
    E_IcedCappuccino.set("0")
    E_CoffeeCake.set("0")
    E_RedVelvetCake.set("0")
    E_BlackForestCake.set("0")
    E_BostonCreamCake.set("0")
    E_LagosChocoCake.set("0")
    E_KillBurnCake.set("0")
    E_CarltonChocoCake.set("0")
    E_QueenParkCake.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    txtLatta.configure(state=DISABLED)
    txtExpresso.configure(state=DISABLED)
    txtIcedLatta.configure(state=DISABLED)
    txtValleCoffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfricanCoffee.configure(state=DISABLED)
    txtAmericanCoffee.configure(state=DISABLED)
    txtIcedCappuccino.configure(state=DISABLED)

    txtCoffeeCake.configure(state=DISABLED)
    txtRedVelvetCake.configure(state=DISABLED)
    txtBlackForestCake.configure(state=DISABLED)
    txtBostonCreamCake.configure(state=DISABLED)
    txtLagosChocoCake.configure(state=DISABLED)
    txtKillBurnCake.configure(state=DISABLED)
    txtCarltonChocoCake.configure(state=DISABLED)
    txtQueenParkCake.configure(state=DISABLED)

#************************* Check Buttons **************************************************
def checkButton_value():
    if (var1.get() == 1):
        txtLatta.configure(state=NORMAL)
    elif var1.get() == 0:
        txtLatta.configure(state=DISABLED)
        E_Latta.set("0")
    if (var2.get() == 1):
        txtExpresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtExpresso.configure(state=DISABLED)
        E_Expresso.set("0")
    if (var3.get() == 1):
        txtIcedLatta.configure(state=NORMAL)
    elif var3.get() == 0:
        txtIcedLatta.configure(state=DISABLED)
        E_IcedLatta.set("0")
    if (var4.get() == 1):
        txtValleCoffee.configure(state=NORMAL)
    elif var4.get() == 0:
        txtValleCoffee.configure(state=DISABLED)
        E_valleCoffee.set("0")
    if (var5.get() == 1):
        txtCappuccino.configure(state=NORMAL)
    elif var5.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")
    if (var6.get() == 1):
        txtAfricanCoffee.configure(state=NORMAL)
    elif var6.get() == 0:
        txtAfricanCoffee.configure(state=DISABLED)
        E_AfricanCoffee.set("0")
    if (var7.get() == 1):
        txtAmericanCoffee.configure(state=NORMAL)
    elif var7.get() == 0:
        txtAmericanCoffee.configure(state=DISABLED)
        E_AmericanCoffee.set("0")
    if (var8.get() == 1):
        txtIcedCappuccino.configure(state=NORMAL)
    elif var8.get() == 0:
        txtIcedCappuccino.configure(state=DISABLED)
        E_IcedCappuccino.set("0")
    if (var9.get() == 1):
        txtCoffeeCake.configure(state=NORMAL)
    elif var9.get() == 0:
        txtCoffeeCake.configure(state=DISABLED)
        E_CoffeeCake.set("0")
    if (var10.get() == 1):
        txtRedVelvetCake.configure(state=NORMAL)
    elif var10.get() == 0:
        txtRedVelvetCake.configure(state=DISABLED)
        E_RedVelvetCake.set("0")
    if (var11.get() == 1):
        txtBlackForestCake.configure(state=NORMAL)
    elif var11.get() == 0:
        txtBlackForestCake.configure(state=DISABLED)
        E_BlackForestCake.set("0")
    if (var12.get() == 1):
        txtBostonCreamCake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtBostonCreamCake.configure(state=DISABLED)
        E_BostonCreamCake.set("0")
    if (var13.get() == 1):
        txtLagosChocoCake.configure(state=NORMAL)
    elif var13.get() == 0:
        txtLagosChocoCake.configure(state=DISABLED)
        E_LagosChocoCake.set("0")
    if (var14.get() == 1):
        txtKillBurnCake.configure(state=NORMAL)
    elif var14.get() == 0:
        txtKillBurnCake.configure(state=DISABLED)
        E_KillBurnCake.set("0")
    if (var15.get() == 1):
        txtCarltonChocoCake.configure(state=NORMAL)
    elif var15.get() == 0:
        txtCarltonChocoCake.configure(state=DISABLED)
        E_CarltonChocoCake.set("0")
    if (var16.get() == 1):
        txtQueenParkCake.configure(state=NORMAL)
    elif var16.get() == 0:
        txtQueenParkCake.configure(state=DISABLED)
        E_QueenParkCake.set("0")

#-------------- Definition Cost of Items *****************************************************
def costofItems():
     Item1 = float(E_Latta.get())
     Item2 = float(E_Expresso.get())
     Item3 = float(E_IcedLatta.get())
     Item4 = float(E_valleCoffee.get())
     Item5 = float(E_Cappuccino.get())
     Item6 = float(E_AfricanCoffee.get())
     Item7 = float(E_AmericanCoffee.get())
     Item8 = float(E_IcedCappuccino.get())

     Item9 = float(E_CoffeeCake.get())
     Item10 = float(E_RedVelvetCake.get())
     Item11 = float(E_BlackForestCake.get())
     Item12 = float(E_BostonCreamCake.get())
     Item13 = float(E_LagosChocoCake.get())
     Item14 = float(E_KillBurnCake.get())
     Item15 = float(E_CarltonChocoCake.get())
     Item16 = float(E_QueenParkCake.get())

     PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) + (Item4 * 1.89) \
                     + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)
     PriceofCakes = (Item9 * 1.2) + (Item10 * 1.99) + (Item11 * 2.05) + (Item12 * 1.89) \
                    + (Item14 * 2.99) + (Item15 * 2.39) + (Item16 * 1.29)

     DrinksPrice = str('%2f' % PriceofDrinks),"fcfa"
     CakesPrice = str('%2f' % PriceofCakes),"fcfa"
     CostofDrinks.set(DrinksPrice)
     CostofCakes.set(CakesPrice)

     SC = str('%2f' % (1.59)),"fcfa"

     ServiceCharge.set(SC)

     SubTotalofItems = str('%2f' % (PriceofDrinks + PriceofCakes + 1.59)),"fcfa"
     SubTotal.set(SubTotalofItems)

     Tax = str('%2f' % (PriceofDrinks + PriceofCakes + 1.59 + 0.15)),"fcfa"
     Paidtax.set(Tax)

     TT = ((PriceofDrinks + PriceofCakes + 1.59) * 0.15)
     TC =  str('%2f' % (PriceofDrinks + PriceofCakes + 1.59 + TT)),"fcfa"
     TotalCost.set(TC)

def receipt():
         txtReceipt.delete("1.0", END)
         X = random.randint(10908, 500876)
         randomref = str("x")
         #Random_Ref.set("Bill    ", +randomref)
         txtReceipt.insert(END, 'Ref_Reçu :\t\t\t' + ReceiptRef.get() + '\t\t' + DateofOrder.get() + "\n")

         txtReceipt.insert(END, 'Articles \t\t\t\t\t' + "Montant des Articles \n\n")

         txtReceipt.insert(END, 'Malta \t\t\t\t\t' + E_Latta.get() + "\n")
         txtReceipt.insert(END, 'Expresso \t\t\t\t\t' + E_Expresso.get() + "\n")
         txtReceipt.insert(END, 'Malta_Sucré \t\t\t\t\t' + E_IcedLatta.get() + "\n")
         txtReceipt.insert(END, 'Café_Colombien \t\t\t\t\t' + E_valleCoffee.get() + "\n")
         txtReceipt.insert(END, 'Cappucinno \t\t\t\t\t' + E_Cappuccino.get() + "\n")
         txtReceipt.insert(END, 'Café_Africain \t\t\t\t\t' + E_AfricanCoffee.get() + "\n")
         txtReceipt.insert(END, 'Café_Americain \t\t\t\t\t' + E_AmericanCoffee.get() + "\n")
         txtReceipt.insert(END, 'Cappuccino_Sucré \t\t\t\t\t' + E_IcedCappuccino.get() + "\n")

         txtReceipt.insert(END, 'Gateau_au_Café\t\t\t\t\t' + E_CoffeeCake.get() + "\n")
         txtReceipt.insert(END, 'Gateau_au_four\t\t\t\t\t' + E_RedVelvetCake.get() + "\n")
         txtReceipt.insert(END, 'Gateau_Oeuf \t\t\t\t\t' + E_BlackForestCake.get() + "\n")
         txtReceipt.insert(END, 'Gateau_Crèmeux \t\t\t\t\t' + E_BostonCreamCake.get() + "\n")
         txtReceipt.insert(END, 'Gateau_Lagos\t\t\t\t\t' + E_LagosChocoCake.get() + "\n")
         txtReceipt.insert(END, 'Gateau_KillBurn \t\t\t\t\t' + E_KillBurnCake.get() + "\n")
         txtReceipt.insert(END, 'Gateau_Carlton\t\t\t\t\t' + E_CarltonChocoCake.get() + "\n")
         txtReceipt.insert(END, 'Gateau_Queen\t\t\t\t\t' + E_QueenParkCake.get() + "\n")

         txtReceipt.insert(END,
                           'Montant_de_Boissons :\t\t' + CostofDrinks.get() + '\tSous_Total:\t\t' + SubTotal.get() + "\n")
         txtReceipt.insert(END,'Montant_Gateaux:\t\t' + CostofCakes.get() + '\tSous_Total:\t\t' + SubTotal.get() + "\n")
         txtReceipt.insert(END,
                           'Charge_des_Services  :\t\t' + ServiceCharge.get() + 'Sous_Total\t\t' + TotalCost.get() + "\n")

     #===========================Button ============================================================================
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=("arial", 12, "bold"),
                       width=5, text="Total", command=costofItems).grid(row=0, column=0)
btnReceipt = Button(fb2, padx=16, pady=1, bd=2, fg="black", font=("arial", 12, "bold"),
                         width=5, text="Réçu", command=receipt).grid(row=0, column=1)
btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=("arial", 12, "bold"),
                       width=5, text="Reinitialiser", command=reset).grid(row=0, column=2)
btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=("arial", 12, "bold"),
                      width=5, text="Quittez", command=qExit).grid(row=0, column=3)

root.mainloop()