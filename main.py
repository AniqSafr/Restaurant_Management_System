import random
from tkinter import *
from tkinter import filedialog, messagebox
import time

root = Tk()

#variables
var0 = IntVar()
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
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()


costFoodvar =StringVar()
costDrinkvar =StringVar()
costDessertvar =StringVar()
subTotalVar =StringVar()
serviceTaxVar =StringVar()
totalvar =StringVar()

#food section
def textRoti():
    if var0.get()==1:
        rotiCanai.config(state=NORMAL)
        rotiCanai.delete(0,END)
        rotiCanai.focus()
    else:
        rotiCanai.config(state=DISABLED)
        String.set('0')

def textCapati():
    if var1.get()==1:
        capati.config(state=NORMAL)
        capati.delete(0,END)
        capati.focus()
    else:
        capati.config(state=DISABLED)
        String1.set('0')

def textMeeGoreng():
    if var2.get()==1:
        meeGoreng.config(state=NORMAL)
        meeGoreng.delete(0,END)
        meeGoreng.focus()
    else:
        meeGoreng.config(state=DISABLED)
        String2.set('0')

def texttomYam():
    if var3.get()==1:
        tomYam.config(state=NORMAL)
        tomYam.delete(0,END)
        tomYam.focus()
    else:
        tomYam.config(state=DISABLED)
        String3.set('0')

def textNaanCheese():
    if var4.get()==1:
        naanCheese.config(state=NORMAL)
        naanCheese.delete(0,END)
        naanCheese.focus()
    else:
        naanCheese.config(state=DISABLED)
        String4.set('0')

def textLaksa():
    if var5.get()==1:
        laksa.config(state=NORMAL)
        laksa.delete(0,END)
        laksa.focus()
    else:
        laksa.config(state=DISABLED)
        String5.set('0')

def textKaripap():
    if var6.get()==1:
        karipap.config(state=NORMAL)
        karipap.delete(0,END)
        karipap.focus()
    else:
        karipap.config(state=DISABLED)
        String6.set('0')

def textOnde2():
    if var7.get()==1:
        onde2.config(state=NORMAL)
        onde2.delete(0,END)
        onde2.focus()
    else:
        onde2.config(state=DISABLED)
        String7.set('0')

def textCoqBadak():
    if var8.get()==1:
        coqBadak.config(state=NORMAL)
        coqBadak.delete(0,END)
        coqBadak.focus()
    else:
        coqBadak.config(state=DISABLED)
        String8.set('0')

#drink section
def textMilo():
    if var9.get()==1:
        milo.config(state=NORMAL)
        milo.delete(0,END)
        milo.focus()
    else:
        milo.config(state=DISABLED)
        String9.set('0')

def textTeh():
    if var10.get()==1:
        teh.config(state=NORMAL)
        teh.delete(0,END)
        teh.focus()
    else:
        teh.config(state=DISABLED)
        String10.set('0')

def textneslo():
    if var12.get()==1:
        neslo.config(state=NORMAL)
        neslo.delete(0,END)
        neslo.focus()
    else:
        neslo.config(state=DISABLED)
        String12.set('0')

def textextraJoss():
    if var13.get()==1:
        extraJoss.config(state=NORMAL)
        extraJoss.delete(0,END)
        extraJoss.focus()
    else:
        extraJoss.config(state=DISABLED)
        String13.set('0')

def textappleJuice():
    if var14.get()==1:
        appleJuice.config(state=NORMAL)
        appleJuice.delete(0,END)
        appleJuice.focus()
    else:
        appleJuice.config(state=DISABLED)
        String14.set('0')

def textayaqNyoq():
    if var15.get()==1:
        ayaqNyoq.config(state=NORMAL)
        ayaqNyoq.delete(0,END)
        ayaqNyoq.focus()
    else:
        ayaqNyoq.config(state=DISABLED)
        String15.set('0')

def texthazelnut():
    if var16.get()==1:
        hazelnut.config(state=NORMAL)
        hazelnut.delete(0,END)
        hazelnut.focus()
    else:
        hazelnut.config(state=DISABLED)
        String16.set('0')

def textorangeJuice():
    if var17.get()==1:
        orangeJuice.config(state=NORMAL)
        orangeJuice.delete(0,END)
        orangeJuice.focus()
    else:
        orangeJuice.config(state=DISABLED)
        String17.set('0')

def textsoda():
    if var18.get()==1:
        soda.config(state=NORMAL)
        soda.delete(0,END)
        soda.focus()
    else:
        soda.config(state=DISABLED)
        String18.set('0')

#dessert section

def textcheeseCake():
    if var19.get()==1:
        cheeseCake.config(state=NORMAL)
        cheeseCake.delete(0,END)
        cheeseCake.focus()
    else:
        cheeseCake.config(state=DISABLED)
        String19.set('0')

def textindulgence():
    if var20.get()==1:
        indulgence.config(state=NORMAL)
        indulgence.delete(0,END)
        indulgence.focus()
    else:
        indulgence.config(state=DISABLED)
        String20.set('0')

def textCroissant():
    if var22.get()==1:
        Croissant.config(state=NORMAL)
        Croissant.delete(0,END)
        Croissant.focus()
    else:
        Croissant.config(state=DISABLED)
        String22.set('0')

def textwaffle():
    if var23.get()==1:
        waffle.config(state=NORMAL)
        waffle.delete(0,END)
        waffle.focus()
    else:
        waffle.config(state=DISABLED)
        String23.set('0')

def textChocolate():
    if var24.get()==1:
        Chocolate.config(state=NORMAL)
        Chocolate.delete(0,END)
        Chocolate.focus()
    else:
        Chocolate.config(state=DISABLED)
        String24.set('0')

def textCaramel():
    if var25.get()==1:
        Caramel.config(state=NORMAL)
        Caramel.delete(0,END)
        Caramel.focus()
    else:
        Caramel.config(state=DISABLED)
        String25.set('0')

def textcrepe():
    if var26.get()==1:
        crepe.config(state=NORMAL)
        crepe.delete(0,END)
        crepe.focus()
    else:
        crepe.config(state=DISABLED)
        String26.set('0')

def textBrowniese():
    if var27.get()==1:
        Brownies.config(state=NORMAL)
        Brownies.delete(0,END)
        Brownies.focus()
    else:
        Brownies.config(state=DISABLED)
        String27.set('0')

def textmuffin():
    if var28.get()==1:
        muffin.config(state=NORMAL)
        muffin.delete(0,END)
        muffin.focus()
    else:
        muffin.config(state=DISABLED)
        String28.set('0')

def reset():
    String.set('0')
    String1.set('0')
    String2.set('0')
    String3.set('0')
    String4.set('0')
    String5.set('0')
    String6.set('0')
    String7.set('0')
    String8.set('0')

    String9.set('0')
    String10.set('0')
    String12.set('0')
    String13.set('0')
    String14.set('0')
    String15.set('0')
    String16.set('0')
    String17.set('0')
    String18.set('0')

    String19.set('0')
    String20.set('0')
    String22.set('0')
    String23.set('0')
    String24.set('0')
    String25.set('0')
    String26.set('0')
    String27.set('0')
    String28.set('0')

    rotiCanai.config(state=DISABLED)
    capati.config(state=DISABLED)
    meeGoreng.config(state=DISABLED)
    tomYam.config(state=DISABLED)
    naanCheese.config(state=DISABLED)
    laksa.config(state=DISABLED)
    karipap.config(state=DISABLED)
    onde2.config(state=DISABLED)
    coqBadak.config(state=DISABLED)
    milo.config(state=DISABLED)
    teh.config(state=DISABLED)
    neslo.config(state=DISABLED)
    extraJoss.config(state=DISABLED)
    appleJuice.config(state=DISABLED)
    ayaqNyoq.config(state=DISABLED)
    hazelnut.config(state=DISABLED)
    orangeJuice.config(state=DISABLED)
    soda.config(state=DISABLED)
    cheeseCake.config(state=DISABLED)
    indulgence.config(state=DISABLED)
    Croissant.config(state=DISABLED)
    waffle.config(state=DISABLED)
    Chocolate.config(state=DISABLED)
    Caramel.config(state=DISABLED)
    crepe.config(state=DISABLED)
    Brownies.config(state=DISABLED)
    muffin.config(state=DISABLED)

    var0.set(0)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)

    costFoodvar.set('')
    costDrinkvar.set('')
    costDessertvar.set('')
    subTotalVar.set('')
    serviceTaxVar.set('')
    totalvar.set('')
    textReceipt.delete(1.0, END)

def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None :
            pass
        else:
            bill = textReceipt.get(1.0, END)
            url.write(bill)
            url.close()
            messagebox.showinfo('Informartion','Your bill is succesfully saved')

def receipt():
    if costFoodvar.get() != '' or costDrinkvar.get() != '' or costDessertvar.get() != '':
        textReceipt.delete(1.0,END)
        x = random.randint(100,1000)
        billNumber = 'Bill' + str(x)
        date = time.strftime('%d/%m/%y')
        textReceipt.insert(END, 'Receipt Ref: \t\t             ' + billNumber+'\t\t            '+date+'\n')
        textReceipt.insert(END,'*******************************************************************\n')
        textReceipt.insert(END,'Item:\t\t\t\t Price(RM)\n')
        textReceipt.insert(END,'*******************************************************************\n')

        if String.get()!='0':
            textReceipt.insert(END,f'Roti Canai\t\t\t\t RM {int(String.get())*1}\n\n')
        if String1.get()!='0':
            textReceipt.insert(END,f'Capati\t\t\t\t RM {int(String1.get())*2}\n\n')
        if String2.get()!='0':
            textReceipt.insert(END,f'Mee Goreng\t\t\t\t RM {int(String2.get())*4}\n\n')
        if String3.get()!='0':
            textReceipt.insert(END,f'TomaYam\t\t\t\t RM {int(String3.get())*5}\n\n')
        if String4.get()!='0':
            textReceipt.insert(END,f'Naan Cheese\t\t\t\t RM {int(String4.get())*5}\n\n')
        if String5.get()!='0':
            textReceipt.insert(END,f'Laksa\t\t\t\t RM {int(String5.get())*3}\n\n')
        if String6.get()!='0':
            textReceipt.insert(END,f'Karipap\t\t\t\t RM {int(String6.get())*0.6}\n\n')
        if String7.get()!='0':
            textReceipt.insert(END,f'Onde-Onde\t\t\t\t RM {int(String7.get())*0.6}\n\n')
        if String8.get() != '0':
            textReceipt.insert(END, f'Coq Badak\t\t\t\t RM {int(String8.get())*0.6}\n\n')

        if String9.get()!='0':
            textReceipt.insert(END,f'Milo Ais\t\t\t\t RM {int(String9.get())*3}\n\n')
        if String10.get()!='0':
            textReceipt.insert(END,f'Teh Ais\t\t\t\t RM {int(String10.get())*3}\n\n')
        if String12.get()!='0':
            textReceipt.insert(END,f'Neslo Ais\t\t\t\t RM {int(String12.get())*3}\n\n')
        if String13.get()!='0':
            textReceipt.insert(END,f'ExtraJoss Anggur\t\t\t\t RM {int(String13.get())*3}\n\n')
        if String14.get()!='0':
            textReceipt.insert(END,f'Apple Juice\t\t\t\t RM {int(String14.get())*3}\n\n')
        if String15.get()!='0':
            textReceipt.insert(END,f'Ayaq Nyoq\t\t\t\t RM {int(String15.get())*3}\n\n')
        if String16.get()!='0':
            textReceipt.insert(END,f'Hazelnut Coffee\t\t\t\t RM {int(String16.get())*3}\n\n')
        if String17.get()!='0':
            textReceipt.insert(END,f'Orange Juice\t\t\t\t RM {int(String17.get())*3}\n\n')
        if String18.get() != '0':
            textReceipt.insert(END, f'Soda Bandung\t\t\t\t RM {int(String18.get())*3}\n\n')

        if String19.get()!='0':
            textReceipt.insert(END,f'Cheese Cake\t\t\t\t RM {int(String19.get())*5}\n\n')
        if String20.get()!='0':
            textReceipt.insert(END,f'Indulgence Cake\t\t\t\t RM {int(String20.get())*5}\n\n')
        if String22.get()!='0':
            textReceipt.insert(END,f'Croissasnt\t\t\t\t RM {int(String22.get())*5}\n\n')
        if String23.get()!='0':
            textReceipt.insert(END,f'Waffle\t\t\t\t RM {int(String23.get())*5}\n\n')
        if String24.get()!='0':
            textReceipt.insert(END,f'Chocolate Cake\t\t\t\t RM {int(String24.get())*5}\n\n')
        if String25.get()!='0':
            textReceipt.insert(END,f'Caramel Pudding\t\t\t\t RM {int(String25.get())*5}\n\n')
        if String26.get()!='0':
            textReceipt.insert(END,f'Crepe\t\t\t\t RM {int(String26.get())*5}\n\n')
        if String27.get()!='0':
            textReceipt.insert(END,f'Brownies\t\t\t\t RM {int(String27.get())*5}\n\n')
        if String28.get() != '0':
            textReceipt.insert(END, f'Muffin\t\t\t\t RM {int(String28.get())*5}\n\n')

        textReceipt.insert(END, '*******************************************************************\n')

        textReceipt.insert(END,f'Cost of food\t\t\t\t RM {round(priceFood,2)}\n\n')
        textReceipt.insert(END,f'Cost of drink\t\t\t\t RM {round(priceDrink,2)}\n\n')
        textReceipt.insert(END,f'Cost of dessert\t\t\t\t RM {round(priceDessert,2)}\n\n')
        textReceipt.insert(END, '*******************************************************************\n')
        textReceipt.insert(END, f'Subb-Total\t\t\t\t RM {round(subTotal,2)}\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t\t RM {round(servicesTax,2)}\n\n')
        textReceipt.insert(END, '*******************************************************************\n')
        textReceipt.insert(END, f'Total (include tax)\t\t\t\t RM {round(totalPrice,2)}\n\n')
    else:
        messagebox.showerror('Error','No item is selected')


def totalCost():
    global priceFood,priceDrink,priceDessert,totalPrice,servicesTax,subTotal

    if var0.get() != 0 or var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var12.get() != 0 or \
        var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or \
        var19.get() != 0 or var20.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or  var25.get() != 0 or \
        var26.get() != 0 or var27.get() != 0 or var28.get() != 0 :


        item = int(String.get())
        item1 = int(String1.get())
        item2 = int(String2.get())
        item3 = int(String3.get())
        item4 = int(String4.get())
        item5 = int(String5.get())
        item6 = int(String6.get())
        item7 = int(String7.get())
        item8 = int(String8.get())

        item9 = int(String9.get())
        item10 = int(String10.get())
        item12 = int(String12.get())
        item13 = int(String13.get())
        item14 = int(String14.get())
        item15 = int(String15.get())
        item16 = int(String16.get())
        item17 = int(String17.get())
        item18 = int(String18.get())

        item19 = int(String19.get())
        item20 = int(String20.get())
        item22 = int(String22.get())
        item23 = int(String23.get())
        item24 = int(String24.get())
        item25 = int(String25.get())
        item26 = int(String26.get())
        item27 = int(String27.get())
        item28 = int(String28.get())

        priceFood = (item*1)+(item1*2)+(item2*4)+(item3*5)+(item4*5)+(item5*3)+(item6*0.6)+(item7*0.6)+(item8*0.6)

        priceDrink = (item9*3.0)+(item10*3)+(item12*3)+(item13*3)+(item14*3)+(item15*3)+(item16*3)+(item17*3)+(item18*3)

        priceDessert = (item19*5.0)+(item20*5)+(item22*5)+(item23*5)+(item24*5)+(item25*5)+(item26*5)+(item27*5)+(item28*5)

        subTotal = priceFood + priceDrink + priceDessert
        servicesTax = (0.06*subTotal)
        totalPrice = (subTotal + servicesTax)

        costFoodvar.set('RM'+ str(round(priceFood,2)))
        costDrinkvar.set('RM'+ str(round(priceDrink,2)))
        costDessertvar.set('RM'+ str(round(priceDessert,2)))
        subTotalVar.set('RM'+ str(round(subTotal,2)))
        serviceTaxVar.set('RM'+ str(round(servicesTax,2)))
        totalvar.set('RM'+ str(round(totalPrice,2)))

    else:
        messagebox.showerror('Error','No item is selected')





#button
def calcualtorButton(numButton,numRow,numColumn):
    calculatorButton = Button(calculatorFrame, text=numButton, font=('arial',16,'bold'), fg='yellow', bg='red4',bd=4, width=6,
                              command=lambda:buttonClick(numButton))
    calculatorButton.grid(row=numRow,column=numColumn)

root.geometry('1360x690+0+0')
root.resizable(0,0)
root.title('Restaurant Management System by AniqSafr')
root.config(bg='firebrick4')

titleFrame = Frame(root,bg='firebrick4', bd=10,relief=RIDGE)
titleFrame.pack(side=TOP)
titleLabel = Label(titleFrame, text="Restaurant Management System", font=('arial',32,'bold'),bg='firebrick4', fg='yellow',width=51, bd=6)
titleLabel.grid(pady=10)

#frame

menuFrame = Frame(root,bd=10, relief=RIDGE, bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame,bd=4,relief=RIDGE, bg='firebrick4', pady=5)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame,text='Food', font=('arial',19,'bold'), bd=10, relief=RIDGE, fg='red4')
foodFrame.pack(side=LEFT)

drinkFrame = LabelFrame(menuFrame,text='Drink', font=('arial',19,'bold'), bd=10, relief=RIDGE, fg='red4')
drinkFrame.pack(side=LEFT)

dessertFrame = LabelFrame(menuFrame,text='Dessert', font=('arial',19,'bold'), bd=10, relief=RIDGE, fg='red4')
dessertFrame.pack(side=LEFT)

rightFrame = Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE)
calculatorFrame.pack()

receiptFrame = Frame(rightFrame, bd=4, relief=RIDGE)
receiptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE)
buttonFrame.pack()

#food frame

String = StringVar()
String.set('0')
rotiCanai = Checkbutton(foodFrame, text='Roti Canai', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var0, command=textRoti)
rotiCanai.grid(row=0, column=0,sticky=W)

rotiCanai = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String)
rotiCanai.grid(row=0,column=1)


String1 = StringVar()
String1.set('0')
capati = Checkbutton(foodFrame, text='Capati', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var1, command=textCapati)
capati.grid(row=1, column=0,sticky=W)

capati = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String1)
capati.grid(row=1,column=1)

String2 = StringVar()
String2.set('0')
meeGoreng = Checkbutton(foodFrame, text='Mee Goreng', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var2, command=textMeeGoreng)
meeGoreng.grid(row=2, column=0,sticky=W)

meeGoreng = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String2)
meeGoreng.grid(row=2,column=1)


String3 = StringVar()
String3.set('0')
tomYam = Checkbutton(foodFrame, text='TomYam', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var3, command=texttomYam)
tomYam.grid(row=3, column=0,sticky=W)

tomYam = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String3)
tomYam.grid(row=3,column=1)

String4 = StringVar()
String4.set('0')
naanCheese = Checkbutton(foodFrame, text='Naan Cheese', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var4, command=textNaanCheese)
naanCheese.grid(row=4, column=0,sticky=W)

naanCheese = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String4)
naanCheese.grid(row=4,column=1)

String5 = StringVar()
String5.set('0')
laksa = Checkbutton(foodFrame, text='Laksa', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var5, command=textLaksa)
laksa.grid(row=5, column=0,sticky=W)

laksa = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String5)
laksa.grid(row=5,column=1)

String6 = StringVar()
String6.set('0')
karipap = Checkbutton(foodFrame, text='Karipap', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var6, command=textKaripap)
karipap.grid(row=6, column=0,sticky=W)

karipap = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String6)
karipap.grid(row=6,column=1)

String7 = StringVar()
String7.set('0')
onde2 = Checkbutton(foodFrame, text='Onde-Onde', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var7, command=textOnde2)
onde2.grid(row=7, column=0,sticky=W)

onde2 = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String7)
onde2.grid(row=7,column=1)

String8 = StringVar()
String8.set('0')
coqBadak = Checkbutton(foodFrame, text='Coq Badak', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var8, command=textCoqBadak)
coqBadak.grid(row=8, column=0,sticky=W)

coqBadak = Entry(foodFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String8)
coqBadak.grid(row=8,column=1)


#drink

String9 = StringVar()
String9.set('0')
milo = Checkbutton(drinkFrame, text='Milo Ais', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var9, command=textMilo)
milo.grid(row=0, column=0,sticky=W)

milo = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String9)
milo.grid(row=0,column=1)

String10 = StringVar()
String10.set('0')
teh = Checkbutton(drinkFrame, text='Teh Ais', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var10, command=textTeh)
teh.grid(row=1, column=0,sticky=W)
teh = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String10)
teh.grid(row=1,column=1)

String12 = StringVar()
String12.set('0')
neslo = Checkbutton(drinkFrame, text='Neslo Ais', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var12, command=textneslo)
neslo.grid(row=2, column=0,sticky=W)

neslo = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String12)
neslo.grid(row=2,column=1)

String13 = StringVar()
String13.set('0')
extraJoss = Checkbutton(drinkFrame, text='Extrajoss Anggur', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var13, command=textextraJoss)
extraJoss.grid(row=3, column=0,sticky=W)

extraJoss = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String13)
extraJoss.grid(row=3,column=1)

String14 = StringVar()
String14.set('0')
appleJuice = Checkbutton(drinkFrame, text='Apple Juice', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var14, command=textappleJuice)
appleJuice.grid(row=4, column=0,sticky=W)

appleJuice = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String14)
appleJuice.grid(row=4,column=1)

String15 = StringVar()
String15.set('0')
ayaqNyoq = Checkbutton(drinkFrame, text='Ayaq Nyoq', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var15, command=textayaqNyoq)
ayaqNyoq.grid(row=5, column=0,sticky=W)

ayaqNyoq = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String15)
ayaqNyoq.grid(row=5,column=1)

String16 = StringVar()
String16.set('0')
hazelnut = Checkbutton(drinkFrame, text='Hazelnut Coffee', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var16, command=texthazelnut)
hazelnut.grid(row=6, column=0,sticky=W)

hazelnut = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String16)
hazelnut.grid(row=6,column=1)

String17 = StringVar()
String17.set('0')
orangeJuice = Checkbutton(drinkFrame, text='orange Juice', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var17, command=textorangeJuice)
orangeJuice.grid(row=7, column=0,sticky=W)

orangeJuice = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String17)
orangeJuice.grid(row=7,column=1)

String18 = StringVar()
String18.set('0')
soda = Checkbutton(drinkFrame, text='Soda Bandung', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var18, command=textsoda)
soda.grid(row=8, column=0,sticky=W)

soda = Entry(drinkFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String18)
soda.grid(row=8,column=1)

#dessert

String19 = StringVar()
String19.set('0')
cheeseCake = Checkbutton(dessertFrame, text='Cheese Cake', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var19, command=textcheeseCake)
cheeseCake.grid(row=0, column=0,sticky=W)

cheeseCake = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String19)
cheeseCake.grid(row=0,column=1)

String20 = StringVar()
String20.set('0')
indulgence = Checkbutton(dessertFrame, text='Indulgence Cake', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var20, command=textindulgence)
indulgence.grid(row=1, column=0,sticky=W)
indulgence = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String20)
indulgence.grid(row=1,column=1)

String22 = StringVar()
String22.set('0')
Croissant = Checkbutton(dessertFrame, text='Croissant', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var22, command=textCroissant)
Croissant.grid(row=2, column=0,sticky=W)

Croissant = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String22)
Croissant.grid(row=2,column=1)

String23 = StringVar()
String23.set('0')
waffle = Checkbutton(dessertFrame, text='Waffle', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var23, command=textwaffle)
waffle.grid(row=3, column=0,sticky=W)

waffle = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String23)
waffle.grid(row=3,column=1)

String24 = StringVar()
String24.set('0')
Chocolate = Checkbutton(dessertFrame, text='Chocolate Cake', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var24, command=textChocolate)
Chocolate.grid(row=4, column=0,sticky=W)

Chocolate = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String24)
Chocolate.grid(row=4,column=1)

String25 = StringVar()
String25.set('0')
Caramel = Checkbutton(dessertFrame, text='Caramel Pudding', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var25, command=textCaramel)
Caramel.grid(row=5, column=0,sticky=W)

Caramel = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String25)
Caramel.grid(row=5,column=1)

String26 = StringVar()
String26.set('0')
crepe = Checkbutton(dessertFrame, text='Crepe', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var26, command=textcrepe)
crepe.grid(row=6, column=0,sticky=W)

crepe = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String26)
crepe.grid(row=6,column=1)

String27 = StringVar()
String27.set('0')
Brownies = Checkbutton(dessertFrame, text='Brownies', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var27, command=textBrowniese)
Brownies.grid(row=7, column=0,sticky=W)

Brownies = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String27)
Brownies.grid(row=7,column=1)

String28 = StringVar()
String28.set('0')
muffin = Checkbutton(dessertFrame, text='Muffin', font=('Arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var28, command=textmuffin)
muffin.grid(row=8, column=0,sticky=W)

muffin = Entry(dessertFrame, font=('Arial', 18, 'bold'), bd=7, width=2, state=DISABLED, textvariable=String28)
muffin.grid(row=8, column=1)


#cost label & andtry fields
labelCostFood = Label(costFrame, text='Cost of Food',font=('arial',16,'bold'), bg='firebrick4', fg='white')
labelCostFood.grid(row=0,column=0)

textCostFood = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14, state='readonly', textvariable=costFoodvar)
textCostFood.grid(row=0,column=1,padx=89)

labelCostDrink = Label(costFrame, text='Cost of Drink',font=('arial',16,'bold'), bg='firebrick4', fg='white')
labelCostDrink.grid(row=1,column=0)

textCostDrink = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14, state='readonly', textvariable=costDrinkvar)
textCostDrink.grid(row=1,column=1,padx=89)

labelCostDessert = Label(costFrame, text='Cost of Dessert',font=('arial',16,'bold'), bg='firebrick4', fg='white')
labelCostDessert.grid(row=2,column=0)

textCostDessert = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14, state='readonly', textvariable=costDessertvar)
textCostDessert.grid(row=2,column=1,padx=87)

labelSubTotal = Label(costFrame, text='Sub Total',font=('arial',16,'bold'), bg='firebrick4', fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14, state='readonly', textvariable=subTotalVar)
textSubTotal.grid(row=0,column=3)

labelServicesTax = Label(costFrame, text='Service Tax',font=('arial',16,'bold'), bg='firebrick4', fg='white')
labelServicesTax.grid(row=1,column=2)

textServicesTax = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14, state='readonly', textvariable=serviceTaxVar)
textServicesTax.grid(row=1,column=3)

labelTotalCost = Label(costFrame, text='Total Cost',font=('arial',16,'bold'), bg='firebrick4', fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14, state='readonly', textvariable=totalvar)
textTotalCost.grid(row=2,column=3)

#button
totalButton = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=10, command=totalCost)
totalButton.grid(row=0, column=0)

totalReceipt = Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=10, command=receipt)
totalReceipt.grid(row=0, column=1)

totalSave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=10, command=save)
totalSave.grid(row=0, column=2)

totalReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=10,command=reset)
totalReset.grid(row=0, column=4)

#text area for reset

textReceipt = Text(receiptFrame, font=('arial',12,'bold'), bd=3, width=45, height=14)
textReceipt.grid(row=0,column=0)

#calculator
operator = ''
def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.config(state=NORMAL)
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0,END)

def ans():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0,result)
    operator = ''

calculatorField = Entry(calculatorFrame,font=('arial',16,'bold'),width=32, bd=4, state=DISABLED)
calculatorField.grid(row=0,column=0, columnspan=4)

#first layer
button7 = calcualtorButton('7',1,0)
button8 = calcualtorButton('8',1,1)
button9 = calcualtorButton('9',1,2)
buttonPlus = calcualtorButton('+',1,3)

#second layer
button4 = calcualtorButton('4',2,0)
button5 = calcualtorButton('5',2,1,)
button6 = calcualtorButton('6',2,2)
buttonMinus= calcualtorButton('-',2,3)

#third layer
button1 = calcualtorButton('1',3,0)
button2 = calcualtorButton('2',3,1)
button3 = calcualtorButton('3',3,2)
buttonMultiply = calcualtorButton('*',3,3)

#fourth layer
buttonAns = Button(calculatorFrame, text='Ans', font=('arial',16,'bold'), fg='yellow', bg='red4',bd=4, width=6, command=ans)
buttonAns.grid(row=4,column=0)
buttonClear = Button(calculatorFrame, text='Clear', font=('arial',16,'bold'), fg='yellow', bg='red4',bd=4, width=6, command=clear)
buttonClear.grid(row=4,column=1)
button0 = calcualtorButton('0',4,2)
buttonDivide = calcualtorButton('/',4,3)

root.mainloop()  # for the window



