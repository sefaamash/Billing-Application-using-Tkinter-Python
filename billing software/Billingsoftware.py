from tkinter import *
"for styling purpose"
from tkinter import ttk
from PIL import Image,ImageTk
"FOR MESAGE BOX"
from tkinter import messagebox
'TO GENERATE RANDOM BILL NUMBER'
import random,os
'To print bill'
import tempfile



class Bill_App:
    def __init__(self,root):
        self.root=root


        """ TITLE"""
        self.root.title("BILLIING SOFTWARE")
        "BACKEND"

        "................variables.........................."
        self.customername=StringVar()
        self.customerphone=StringVar()
        self.billno=StringVar()
        z=random.randint(1000,9999)
        self.billno.set(z)
        self.customeremail=StringVar()
        self.searchbill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.subtotal=StringVar()
        self.taxinp=StringVar()
        self.totaly=StringVar()
        self.qty=IntVar()










        '....................CATEGORIES LIST OF PRODUCTS..............................'
        self.Category=['Select Option',"Clothing",'Lifestyle','Mobiles']


        "CLOTHING SUBCATEGORY"
        self.subcatcloth=['Pant','Shirt','T-shirt']
        'Pant'
        self.pant=['Levis','Denim','Denizen']
        'Levis Price'
        self.levispant_price=5000
        'Denim Price'
        self.denimpant_price = 6000
        'Denizen Price'
        self.denizenpant_price = 3500

        'shirt'
        self.Shirt = ['Levis' , 'Denim' , 'Denizen']
        'Levis Price'
        self.levis_Shirtprice = 2000
        'Denim Price'
        self.denimShirt_price = 3000
        'Denizen Price'
        self.denizenShirt_price = 3500

        'T-shirt'
        self.Tshirt = ['Levis' , 'Denim' , 'Denizen']
        'Levis Price'
        self.levisT_price = 2000
        'Denim Price'
        self.denimT_price = 2500
        'Denizen Price'
        self.denizenT_price = 3500


        'SUBCAT LIFESTYLE'
        self.subcatlifesty=['Bath Soap','Face Cream','Hair wax']

        'Bath Soap'
        self.bathsoap = ['Lux' , 'Lifeboy' , 'Safeguard']
        'Lux Price'
        self.lux_price = 150
        'Lifeboy Price'
        self.lifeboy_price = 100
        'safeguard Price'
        self.safeguard_price = 155

        'Face cream'
        self.facecream = ['Ponds' , 'Tibet']
        'Ponds Price'
        self.ponds_price = 110
        'tibet Price'
        self.tibet_price = 90

        'Hairwax'
        self.gatsby = ['hairwax' , 'hairgel']
        'hairwax Price'
        self.wax_price = 190
        'gell Price'
        self.gell_price = 280



        'SUBCATMOBILES'
        self.subcatmob=['Iphone','Samsung','Xiomi']

        "IPHONE"
        self.iphone=['seven','eight','X','eleven']

        self.sevenprice=80000
        self.eightprice=90000
        self.Xprice=120000
        self.elevenprice=200000

        'SAMSUNG'
        self.SAMSUNG = ['S10' , 'S12' , 'S20' ]

        self.S10price = 80000
        self.S12price = 90000
        self.S20price = 120000

        'XIOMI'
        self.xiomi = ['MI9' , 'MI10' , 'MI11']

        self.MI9price = 80000
        self.MI10price = 90000
        self.MI11price = 120000











        "IMAGE 1 "
        img=Image.open("image/img/b1.jpg")
        "IMAGE.ANTIALIAS CONVERT HIGH LEVEL IMG TO LOW LEVEL"
        img=img.resize((450,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        "to show img with label"
        lbl_img=Label(self.root,image=self.photoimg)
        "sticky to fix at corner"
        lbl_img.place(x=0,y=0,width=430,height=100)

        "IMAGE 2"
        img2= Image.open ( "image/img/girl1.jpg" )
        "IMAGE.ANTIALIAS CONVERT HIGH LEVEL IMG TO LOW LEVEL"
        img2 = img2.resize ( (550 , 100) , Image.ANTIALIAS )
        self.photoimg2 = ImageTk.PhotoImage ( img2 )
        "to show img with label"
        lbl_img2 = Label ( self.root , image=self.photoimg2 )
        "sticky to fix at corner"
        lbl_img2.place(x=420,width=550,height=100)

        "IMAGE 3"
        img3 = Image.open ( "image/img/mall.jpg" )
        "IMAGE.ANTIALIAS CONVERT HIGH LEVEL IMG TO LOW LEVEL"
        img3 = img3.resize ( (520 , 100) , Image.ANTIALIAS )
        self.photoimg3 = ImageTk.PhotoImage ( img3 )
        "to show img with label"
        lbl_img3 = Label ( self.root , image=self.photoimg3 )
        "sticky to fix at corner"
        lbl_img3.place(x=900,y=0,width=480,height=100)


        "TITLE"
        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=100,width=1400,height=45)


        "FRAMES"


        "MAINFRAME"
        "relief-groove is used for styling of frames it has many options"
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg='white')
        Main_Frame.place(x=0,y=150,width=1530,height=620)

        "CUSTOMER LabelFRAME"
        "we use mainframe inside label because we have to make inside label"
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg='white',fg='red')
        'we use y-5 beacuse we r now seting inside frame not in window '
        Cust_Frame.place(x=10,y=2,width=350,height=140)
        "inside custframe so thats we we write Cust_Frame"
        self.lbl_mob=Label(Cust_Frame,text="Mobile no",font=("times new roman",12,"bold"),bg='white')
        self.lbl_mob.grid(row=0,column=0,stick='w',padx=5,pady=2)
        self.lbl_mob_entry=ttk.Entry(Cust_Frame,textvariable=self.customerphone,font=("times new roman",12,'bold'),width=24)
        self.lbl_mob_entry.grid(row=0,column=1)

        self.cust_name = Label ( Cust_Frame , text="Customer name" , font=("times new roman" , 12 , "bold") , bg='white' )
        self.cust_name.grid ( row=1 , column=0 , stick='w' , padx=5 , pady=2 )
        self.cust_name_entry = ttk.Entry ( Cust_Frame ,textvariable=self.customername, font=("times new roman" , 12 , 'bold') , width=24 )
        self.cust_name_entry.grid ( row=1 , column=1 )

        self.lbl_email= Label ( Cust_Frame , text="Email" , font=("times new roman" , 12 , "bold") , bg='white' )
        self.lbl_email.grid ( row=2  , column=0 , stick='w' , padx=5 , pady=2 )
        self.lbl_email_entry = ttk.Entry ( Cust_Frame ,textvariable=self.customeremail, font=("times new roman" , 12 , 'bold') , width=24 )
        self.lbl_email_entry.grid ( row=2 , column=1 )



        "PRODUCT FRAME"

        Product_Frame = LabelFrame ( Main_Frame , text="Product" , font=("times new roman" , 12 , "bold") , bg='white' ,
                                  fg='red' )
        Product_Frame.place ( x=370 , y=2 , width=600 , height=140 )

        "category label"
        self.lbl_cat = Label ( Product_Frame , text="Select Categories" , font=("times new roman" , 12 , "bold") , bg='white' )
        self.lbl_cat.grid ( row=0 , column=0 , stick='w' , padx=5 , pady=2)
        'COMBO BOX FOR CATEGORY state is set to readonly we cannot write'
        self.Combo_category=ttk.Combobox(Product_Frame,value=self.Category, font=("times new roman" , 12 , "bold")
                                         ,width='24',state="readonly")
        'It will show the intial value which is set to 0 index(Select option on combobox'
        self.Combo_category.current(0)
        self.Combo_category.grid(row=0,column=1,stick='w',padx=5,pady=2)
        'the category we select in category it will bind it in sub category as we set in our function'
        self.Combo_category.bind("<<ComboboxSelected>>",self.Categories)

        'SUB CATEGORIES'
        self.lbl_subcat = Label ( Product_Frame , text="Select Sub-Categories" , font=("times new roman" , 12 , "bold") ,
                               bg='white', )
        self.lbl_subcat.grid ( row=1 , column=0 , stick='w' , padx=5 , pady=2 )
        'COMBO BOX FOR CATEGORY state is set to readonly we cannot write we gave empty list in value because it (in subcat each cat is opening a list means list generated from list bit in category it is not gnerating from list but with our selection)'
        self.Combo_subcategory = ttk.Combobox ( Product_Frame ,value=[], font=("times new roman" , 12 , "bold") , width='24' ,
                                             state="readonly", )
        self.Combo_subcategory.grid ( row=1 , column=1 , stick='w' , padx=5 , pady=2 )
        self.Combo_subcategory.bind("<<ComboboxSelected>>",self.add)

        'PRODUCT NAME'
        self.lbl_PRO = Label ( Product_Frame , text="Product" , font=("times new roman" , 12 , "bold") ,
                                  bg='white', )
        self.lbl_PRO.grid ( row=2 , column=0 , stick='w' , padx=5 , pady=2 )
        'COMBO BOX FOR CATEGORY state is set to readonly we cannot write'
        self.Combo_PRO = ttk.Combobox ( Product_Frame ,textvariable=self.product, font=("times new roman" , 12 , "bold") , width='24' ,
                                                state="readonly", )
        self.Combo_PRO.grid ( row=2 , column=1 , stick='w' , padx=5 , pady=2 )
        self.Combo_PRO.bind("<<ComboboxSelected>>",self.price)

        'PRICE'
        self.lbl_PRICE = Label ( Product_Frame , text="Price" , font=("times new roman" , 12 , "bold") ,
                               bg='white' )
        self.lbl_PRICE.grid ( row=0 , column=2 , stick='w' , padx=5 , pady=2 )
        'COMBO BOX FOR price  is set to readonly we cannot write'
        self.Combo_PRICE = ttk.Combobox ( Product_Frame ,textvariable=self.prices, font=("times new roman" , 12 , "bold") , width='10' ,
                                        state="readonly" )
        self.Combo_PRICE.grid ( row=0 , column=3 , stick='w' , padx=5 , pady=2 )

        'QUANTITY'
        self.lbl_QUAN = Label( Product_Frame , text="Quantity" , font=("times new roman" , 12 , "bold") ,
                                 bg='white' )
        self.lbl_QUAN.grid ( row=1 , column=2 , stick='w' , padx=5 , pady=2 )
        self.lbl_QUAN_entry = ttk.Entry ( Product_Frame ,textvariable=self.qty, font=("times new roman" , 12 , 'bold') , width=10 )
        self.lbl_QUAN_entry.grid ( row=1 , column=3,stick='w' , padx=5 , pady=2  )

        "MIDDILE FRAME FOR PICRYRES"
        middleFrame=Frame(Main_Frame)
        middleFrame.place(x=0,y=145,width=980,height=340)

        "IMAGE 4 "
        img4 = Image.open ( "image/img/good.jpg" )
        "IMAGE.ANTIALIAS CONVERT HIGH LEVEL IMG TO LOW LEVEL"
        img4 = img4.resize ( (490 , 300) , Image.ANTIALIAS )
        self.photoimg4 = ImageTk.PhotoImage ( img4 )
        "to show img with label"
        lbl_img4 = Label ( middleFrame, image=self.photoimg4 )
        "sticky to fix at corner"
        lbl_img4.place(x=0,y=0,width=490,height=300)

        "IMAGE 5"
        img5 = Image.open ( "image/img/girls.jpg" )
        "IMAGE.ANTIALIAS CONVERT HIGH LEVEL IMG TO LOW LEVEL"
        img5 = img5.resize ( (490 , 340) , Image.ANTIALIAS )
        self.photoimg5 = ImageTk.PhotoImage ( img5 )
        "to show img with label"
        lbl_img5 = Label ( middleFrame , image=self.photoimg5 )
        "sticky to fix at corner"
        lbl_img5.place(x=490,y=0,width=490,height=320)

        "searchframe"
        search_frame=LabelFrame(Main_Frame,bg='white',)
        search_frame.place(x=972,y=10,width=500,height=40)

        'bill number label'
        billnum_lbl=Label(search_frame,text='BillNumber',bg='red',fg='white',font=('arial',12,'bold'))
        billnum_lbl.grid(row=0,column=0,sticky='w',padx=1,pady=3)

        'Entry fill'
        fill_entry = ttk.Entry (search_frame ,textvariable=self.searchbill, font=("arial" , 12 , 'bold') , width=15)
        fill_entry.grid ( row=0 , column=1,padx=2,pady=2 )

        'search button'
        btn_search = Button ( search_frame ,command=self.findbill, text="search" , font=("arial" , 10 , 'bold') ,
                            bg='orangered' , fg='white' , width=15 , cursor='hand2' )
        btn_search.grid ( row=0 , column=2  )

        'RIGHT FRAME BILL AREA'

        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman" , 12 , 'bold'),fg="red",bg="white",bd=4)
        RightLabelFrame.place(x=972,y=50,width=390,height=400)
        "scrollbar(TO SCROLL THE BILL AREA)"
        scroll_y = Scrollbar ( RightLabelFrame , orient=VERTICAL )
        'scroll_y.set is a function to set scroll command Y IS BASICALLY OUR BILL WILL BE WRRITEN IN Y AXIS UP TO DOWN'
        self.textarea = Text ( RightLabelFrame , yscrollcommand=scroll_y.set , bg="white" , fg="blue" ,
                          font=("times new roman" , 12 , 'bold') )
        scroll_y.pack ( side=RIGHT , fill=Y )
        'for y view we set texarea to y view up to down'
        scroll_y.config ( command=self.textarea.yview )
        "to fill text area from both sides and thecontnent should be inside whoioe text area we use expand=1 and fill(both)"
        self.textarea.pack ( fill=BOTH , expand=1 )

        'BILL COUNTER LABEL FRAME'

        BottomLabelFrame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman" , 12 , 'bold'),fg="red",bg="white",bd=4)
        BottomLabelFrame.place(x=0,y=430,width=1520,height=250)

        "SUBTOTAL"
        self.SUBtotal = Label ( BottomLabelFrame , text="Sub-Total" , font=("times new roman" , 12 , "bold") ,
                                 bg='white' )
        self.SUBtotal.grid ( row=0 , column=0 , stick='w' , padx=5 , pady=2 )
        self.SUBtotal_entry = ttk.Entry ( BottomLabelFrame ,textvariable=self.subtotal, font=("times new roman" , 12 , 'bold') , width=24 )
        self.SUBtotal_entry.grid ( row=0 , column=1 )
        'TOTAL'
        self.total = Label ( BottomLabelFrame , text="Total" , font=("times new roman" , 12 , "bold") ,
                             bg='white' )
        self.total.grid ( row=1 , column=0 , stick='w' , padx=5 , pady=2 )
        self.total_entry = ttk.Entry ( BottomLabelFrame , textvariable=self.totaly ,
                                       font=("times new roman" , 12 , 'bold') , width=24 )
        self.total_entry.grid ( row=1 , column=1 )

        'Taxes'
        self.tax = Label ( BottomLabelFrame , text="Taxes" , font=("times new roman" , 12 , "bold") ,
                             bg='white' )
        self.tax.grid ( row=2 , column=0 , stick='w' , padx=5 , pady=2 )
        self.tax_entry = ttk.Entry ( BottomLabelFrame ,textvariable=self.taxinp, font=("times new roman" , 12 , 'bold') , width=24 )
        self.tax_entry.grid ( row=2 , column=1 )




        'Button Frame'
        Button_Frame=Frame(BottomLabelFrame,bd=2,bg='white')
        Button_Frame.place(x=320,y=0)

        btn_addtocart=Button(Button_Frame,height=2,text="add to cart",font=("arial" , 10 , 'bold'),bg='orangered',
                             fg='white',command=self.Additems,width=19,cursor='hand2')
        btn_addtocart.grid(row=0,column=0,pady=20)

        'generate bill'
        btn_genbill = Button ( Button_Frame ,command=self.genbill, height=2 , text="generate bill" , font=("arial" , 10 , 'bold') ,
                                 bg='orangered' , fg='white',width=19,cursor='hand2' )
        btn_genbill.grid ( row=0 , column=1,pady=20 )

        'save'
        btn_save= Button ( Button_Frame ,command=self.savebill, height=2 , text="save" , font=("arial" , 10 , 'bold') ,
                                 bg='orangered' , fg='white',width=19,cursor='hand2' )
        btn_save.grid ( row=0 , column=2,pady=20 )

        'print'
        btn_print = Button ( Button_Frame , height=2 ,command=self.printbill, text="print" , font=("arial" , 10 , 'bold') ,
                                 bg='orangered' , fg='white',width=19,cursor='hand2' )
        btn_print.grid ( row=0 , column=3,pady=20 )

        'clear'
        btn_clear = Button ( Button_Frame , height=2 ,command=self.clear, text="clear" , font=("arial" , 10 , 'bold') ,
                                 bg='orangered' , fg='white',width=19,cursor='hand2' )
        btn_clear.grid ( row=0 , column=4 ,pady=20)

        'exit'
        'clear'
        btn_exit = Button ( Button_Frame ,command=self.root.destroy, height=2 , text="exit" , font=("arial" , 10 , 'bold') ,
                             bg='orangered' , fg='white',width=15,cursor='hand2')
        btn_exit.grid ( row=0 , column=5,pady=20 )

        "WELCOME FUNC CALL"
        self.Welcome ( )


        '===============================FUNCTION DECLAERATION========================================='

        'to save price according to quan inside list'
        self.l = []

    "WELCOME TEXT IN BILL AREA"

    def Welcome(self):
        'TO INSERT'
        self.textarea.delete ( 1.0 , END )
        self.textarea.insert ( END , '==========Welcome to Mini Mart=============' )
        self.textarea.insert ( END , f"\n Bill Number:{self.billno.get ( )}" )
        self.textarea.insert ( END , f"\n Bill Number:{self.billno.get ( )}" )
        self.textarea.insert ( END , f"\n Customer Name:{self.customername.get ( )}" )
        self.textarea.insert ( END , f"\n Phone No:{self.customerphone.get ( )}" )
        self.textarea.insert ( END , f"\n Email:{self.customeremail.get ( )}" )
        self.textarea.insert ( END , "\n========================================" )
        self.textarea.insert ( END , f"\n Products\t\tQTN\t\tPrice" )
        self.textarea.insert ( END , "\n========================================" )

    def Additems(self):


        'for tax'
        tax=1
        'for price'
        'for eg if quan is 2 so it will mul the quan to price which is '
        self.m=int(self.qty.get()*self.prices.get())
        'now append taht price inside self.l list above'
        self.l.append(self.m)
        'if product is empty show error message'

        if self.product.get()==" ":
            messagebox.showerror("ERROR","PLEASE SELECT THE PRODUCT NAME")
        else:
            'following will first print product name then its quan the its price save in self.m'

            self.textarea.insert(END,f"\n{str(self.product.get())}\t\t{int(self.qty.get())}\t\t{int(self.m)}")
            self.subtotal.set ( str ( 'Rs.%.2f' % (sum ( self.l )) ) )
            self.taxinp.set ( str ( 'Rs.%.2f' % ((((sum ( self.l )) - (self.prices.get ( ))) * tax / 100)) ) )
            self.totaly.set ( str ( 'Rs.%.2f' % (((sum ( self.l )) + ((((sum ( self.l )) - (self.prices.get ( ))) *tax/100)))) ) )
    "TO GENERATE BILL"
    def genbill(self):
            if self.product.get()==" ":
                  messagebox.showerror("ERROR","PLEASE SELECT THE PRODUCT NAME")
            else:
                text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                self.Welcome()
                self.textarea.insert(END,text)
                self.textarea.insert ( END , "\n=======================================" )
                'TO INSERT SUB TOTAL,taxes,amount'
                self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.subtotal.get()}")
                self.textarea.insert ( END , f"\n Tax Amount:\t\t\t{self.taxinp.get ( )}" )
                self.textarea.insert ( END , f"\n Total Amount:\t\t\t{self.totaly.get ( )}" )
                self.textarea.insert ( END , "\n=======================================" )
    'TO SAVE BILL'
    def savebill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.billdata=self.textarea.get(1.0,END)
            f1=open('BILLS/'+str(self.billno.get())+".txt",'w')
            f1.write(self.billdata)
            op = messagebox.showinfo ( "Saved" , f"Billno:{self.billno.get()} saved successfully" )
            f1.close()
    'PRINT BILL'
    def printbill(self):
        pb=self.textarea.get(1.0,"end-1c")
        'to print'
        filename=tempfile.mktemp('.txt')
        'open file then write pb means text area content'
        open(filename,'w').write(pb)
        "to start file"
        os.startfile(filename,"print")
    'to search bill'
    def findbill(self):
        found="no"
        "to start loop inside the folder where bills are saved it will be split by . and take only folder name which is BILLS"

        for i in os.listdir("BILLS/"):
            if i.split('.')[0]==self.searchbill.get():
                'OPEN FILE'
                f1=open(f"BILLS/{i}",'r')
                'delete text area'
                self.textarea.delete(1.0,END)
                "NOW ITERATE FILE"
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found='yes'
        if found=="no":
                messagebox.showerror("ERROR","THERE IS A ERROR")
    "CLEAR FUNC"
    def clear(self):
        self.textarea.delete(1.0,END)
        self.customername.set("")
        self.customerphone.set("")
        self.customeremail.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.taxinp.set("")
        self.totaly.set("")
        self.subtotal.set("")
        self.Welcome()
        X=random.randint(1000,10000)
        self.billno.set(str(X))
        self.searchbill.set("")






    def Categories(self,event=''):
             'if self.combo category equal to(we select clothing category) clothing'
             if self.Combo_category.get()=="Clothing":
                   'then clothing comes inside self.category box through config'
                   self.Combo_subcategory.config(value=self.subcatcloth)
                   self.Combo_subcategory.current(0)
             if self.Combo_category.get ( ) == "Lifestyle":
                 self.Combo_subcategory.config ( value=self.subcatlifesty )
                 self.Combo_subcategory.current ( 0 )
             if self.Combo_category.get ( ) == "Mobiles":
                 self.Combo_subcategory.config ( value=self.subcatmob )
                 self.Combo_subcategory.current ( 0 )

    def add(self,event=''):
        'IN ABOVE WE SELECTED CLOTHING SO IT WILL CONFIG CLOTHING LIST INSIDE SUBCATEGORY THAN IN SUBCAT IF WE SELECT PANT THEN IT WILL CONFIG THAT PANT AS PRODUCTNAME INSIDE PRODUCTR NAME'
        if self.Combo_subcategory.get()=="Pant":
            self.Combo_PRO.config(value=self.pant)
            self.Combo_PRO.current(0)
        if self.Combo_subcategory.get()=="Shirt":
            self.Combo_PRO.config(value=self.Shirt)
            self.Combo_PRO.current(0)
        if self.Combo_subcategory.get()=="T-shirt":
            self.Combo_PRO.config(value=self.Tshirt)
            self.Combo_PRO.current(0)
        'LIFESTYLE'

        if self.Combo_subcategory.get()=="Bath Soap":
            self.Combo_PRO.config(value=self.bathsoap)
            self.Combo_PRO.current(0)
        if self.Combo_subcategory.get()=="Face Cream":
            self.Combo_PRO.config(value=self.facecream)
            self.Combo_PRO.current(0)
        if self.Combo_subcategory.get()=="Hair wax":
            self.Combo_PRO.config(value=self.gatsby)
            self.Combo_PRO.current(0)


        'Mobiles'
        if self.Combo_subcategory.get()=="Iphone":
            self.Combo_PRO.config(value=self.iphone)
            self.Combo_PRO.current(0)
        if self.Combo_subcategory.get()=="Samsung":
            self.Combo_PRO.config(value=self.SAMSUNG)
            self.Combo_PRO.current(0)
        if self.Combo_subcategory.get()=="Xiomi":
            self.Combo_PRO.config(value=self.xiomi)
            self.Combo_PRO.current(0)
    def price(self,event=""):
        'pant'
        if self.Combo_PRO.get()=="Levis":
            self.Combo_PRICE.config(value=int(self.levispant_price))
            'by default producr will be set to 0'
            self.Combo_PRICE.current(0)
            'by default quantity will be set to 1'
            self.qty.set(1)
        if self.Combo_PRO.get()=="Denim":
            self.Combo_PRICE.config(value=int(self.denimpant_price))
            self.Combo_PRICE.current(0)
            self.qty.set(1)
        if self.Combo_PRO.get ( ) == "Denizen":
            self.Combo_PRICE.config ( value=int ( self.denizenpant_price ) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )

        'SHIRT'
        if self.Combo_PRO.get ( ) == "Levis":
            self.Combo_PRICE.config ( value=int ( self.levis_Shirtprice ) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "Denim":
            self.Combo_PRICE.config ( value=int ( self.denimShirt_price ) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "Denizen":
            self.Combo_PRICE.config ( value=int ( self.denizenShirt_price ) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )

        'Tshirt'
        if self.Combo_PRO.get ( ) == "Levis":
            self.Combo_PRICE.config ( value=int ( self.levisT_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "Denim":
            self.Combo_PRICE.config ( value=int ( self.denimT_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "Denizen":
            self.Combo_PRICE.config ( value=int ( self.denizenT_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )

        'LIFESTYLE'
        'BATHSOAP'
        if self.Combo_PRO.get ( ) == "Lux":
            self.Combo_PRICE.config ( value=int ( self.lux_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "Lifeboy":
            self.Combo_PRICE.config ( value=int ( self.lifeboy_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "Safeguard":
            self.Combo_PRICE.config ( value=int ( self.safeguard_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )

        'FACECREAM'
        if self.Combo_PRO.get ( ) == "Ponds":
            self.Combo_PRICE.config ( value=int ( self.ponds_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "Tibet":
            self.Combo_PRICE.config ( value=int ( self.tibet_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        'HAIRWAX'

        if self.Combo_PRO.get ( ) == "hairwax":
            self.Combo_PRICE.config ( value=int ( self.wax_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "hairgel":
            self.Combo_PRICE.config ( value=int( self.gell_price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )



        'Mobiles'
        'IPHONE'
        if self.Combo_PRO.get ( ) == "seven":
            self.Combo_PRICE.config ( value=int ( self.sevenprice) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "eight":
            self.Combo_PRICE.config ( value=int ( self.eightprice) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "X":
            self.Combo_PRICE.config ( value=int ( self.Xprice) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "eleven":
            self.Combo_PRICE.config ( value=int ( self.elevenprice) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )

        "SAMSUNG"
        if self.Combo_PRO.get ( ) == "S10":
            self.Combo_PRICE.config ( value=int ( self.S10price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "S12":
            self.Combo_PRICE.config ( value=int ( self.S12price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "S20":
            self.Combo_PRICE.config ( value=int ( self.S20price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )

        "XIOMI"
        if self.Combo_PRO.get ( ) == "MI9":
            self.Combo_PRICE.config ( value=int ( self.MI9price ) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "MI10":
            self.Combo_PRICE.config ( value=int ( self.MI10price) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )
        if self.Combo_PRO.get ( ) == "MI11":
            self.Combo_PRICE.config ( value=int ( self.MI11price ) )
            self.Combo_PRICE.current ( 0 )
            self.qty.set ( 1 )



























if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

