
import ekor as g
import tkinter as tk
from tkinter import ttk

import bisectionMethod as bm
import regulaFalsiMethod as rf
import newtonRaphsonMethod as nrm
import secantMethod as  sm

class Test():
    def __init__(self):
        self.flag = True
        self.flag_btn_graph = True
        self.flag_txtlab = True
        self.root = tk.Tk()
        self.root.geometry("350x500")
        self.mylabel = tk.Label(self.root, text="Numerical Computing", background='green', foreground="white",font=("Times New Roman", 15))
        self.text = tk.StringVar()
        self.text.set("::::::::")
        self.label = tk.Label(self.root, textvariable=self.text)
        #self.txtlabel = tk.Label(self.root, textvariable='')
        self.n = tk.StringVar()

        selected = tk.StringVar()
        self.cb = ttk.Combobox(self.root, textvariable=selected)
        self.cb['values'] = (' Bisection Method',
                          ' Regula Falsi Method',
                          ' Newton Raphson Method',
                          ' Secant Method',)

        self.mylabel.pack()
        self.cb.pack(fill=tk.X, padx=5, pady=5)


        self.button = tk.Button(self.root,
                                text="Select Method",
                                command=self.changeText)
        self.button.pack()
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def runNewtonRaphson(self):
        if self.flag_btn_graph == False:
            self.btn_graph.pack_forget()
            self.flag_btn_graph = True

        if self.flag_txtlab == False:
            self.txtlabel.pack_forget()
            self.flag_txtlab = True
        x0 = float(self.input_x.get().strip())
        print(x0)

        nrm.startnewtonRaphson(x0)
        print(nrm.temp)
        self.flag_txtlab = False
        print(self.flag_txtlab)

        self.txtlabel = tk.Label(self.root, textvariable='')
        self.txtlabel.config(text=("\n".join(nrm.temp)))
        self.txtlabel.pack()

        self.flag_btn_graph = False
        xis =nrm.myx[0]
        yxis =nrm.valone[0]
        self.btn_graph = tk.Button(self.root,text="View Graph",command=lambda:g.plot_my_graph(xis, yxis))
        self.btn_graph.pack()
        nrm.temp = []
        nrm.myx = []
        nrm.valone =[]


    def runSecant(self):
        if self.flag_btn_graph == False:
            self.btn_graph.pack_forget()
            self.flag_btn_graph = True

        if self.flag_txtlab == False:
            self.txtlabel.pack_forget()
            self.flag_txtlab = True
        x0 = float(self.input_x.get().strip())
        x1 = float(self.input_y.get().strip())
        print(x0)
        print(x1)

        sm.startsecant(x0, x1)
        print(sm.temp)
        self.flag_txtlab = False
        print(self.flag_txtlab)

        self.txtlabel = tk.Label(self.root, textvariable='')
        self.txtlabel.config(text=("\n".join(sm.temp)))
        self.txtlabel.pack()

        self.flag_btn_graph = False
        xis =sm.myx[0]
        yxis =sm.valone[0]
        self.btn_graph = tk.Button(self.root,text="View Graph",command=lambda:g.plot_my_graph(xis, yxis))
        self.btn_graph.pack()
        sm.temp = []
        sm.myx = []
        sm.valone =[]


    def runRuglafalsi(self):
        if self.flag_btn_graph == False:
            self.btn_graph.pack_forget()
            self.flag_btn_graph = True

        if self.flag_txtlab == False:
            self.txtlabel.pack_forget()
            self.flag_txtlab = True
        x0 = float(self.input_x.get().strip())
        x1 = float(self.input_y.get().strip())
        print(x0)
        print(x1)

        rf.startfalsePosition(x0, x1)
        print(bm.temp)
        self.flag_txtlab = False
        print(self.flag_txtlab)

        self.txtlabel = tk.Label(self.root, textvariable='')
        self.txtlabel.config(text=("\n".join(rf.temp)))
        self.txtlabel.pack()

        self.flag_btn_graph = False
        xis =rf.myx[0]
        yxis =rf.valone[0]
        self.btn_graph = tk.Button(self.root,text="View Graph",command=lambda:g.plot_my_graph(xis, yxis))
        self.btn_graph.pack()
        rf.temp = []
        rf.myx = []
        rf.valone =[]



    def runBisection(self):

        if self.flag_btn_graph == False:
            self.btn_graph.pack_forget()
            self.flag_btn_graph = True

        if self.flag_txtlab == False:
            self.txtlabel.pack_forget()
            self.flag_txtlab = True

        x0 = float(self.input_x.get().strip())
        x1 = float(self.input_y.get().strip())
        print(x0)
        print(x1)

        bm.Startbisection(x0, x1)
        print(bm.temp)
        self.flag_txtlab = False
        print(self.flag_txtlab)

        self.txtlabel = tk.Label(self.root, textvariable='')
        self.txtlabel.config(text=("\n".join(bm.temp)))
        self.txtlabel.pack()

        self.flag_btn_graph = False
        xis =bm.myx[0]
        yxis =bm.valone[0]
        self.btn_graph = tk.Button(self.root,text="View Graph",command=lambda:g.plot_my_graph(xis, yxis))
        self.btn_graph.pack()
        bm.temp = []
        bm.myx = []
        bm.valone =[]





    def changeText(self):
        t = self.cb.get()
        self.text.set(t)
        if self.flag_btn_graph == False:
            self.btn_graph.pack_forget()
            self.flag_btn_graph = True

        if self.flag_txtlab == False:
            self.txtlabel.pack_forget()
            self.flag_txtlab = True

        if self.flag and t.strip() != '':
            self.flag = False
            self.x = tk.Label(self.root, text="value 1")
            self.input_x = tk.Entry(self.root, width=30)
            self.x.pack()
            self.input_x.pack()

            self.y = tk.Label(self.root, text="Value 2")
            self.input_y = tk.Entry(self.root, width=30)
            self.y.pack()
            self.input_y.pack()
        else:
            self.button1.destroy()

        if t.strip() == 'Bisection Method':

            self.button1 = tk.Button(self.root,
                                    text="Run",
                                    command=self.runBisection)
            self.button1.pack()

        if t.strip() == 'Regula Falsi Method':

            self.button1 = tk.Button(self.root,
                                    text="Run",
                                    command=self.runRuglafalsi)
            self.button1.pack()
        if t.strip() == 'Secant Method':

            self.button1 = tk.Button(self.root,
                                    text="Run",
                                    command=self.runSecant)
            self.button1.pack()

        if t.strip() == 'Newton Raphson Method':

            self.button1 = tk.Button(self.root,
                                    text="Run",
                                    command=self.runNewtonRaphson)
            self.button1.pack()




app=Test()

