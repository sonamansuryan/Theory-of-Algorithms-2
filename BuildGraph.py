import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class GrafKarutsich:
    def __init__(self):
        self.patuhan = tk.Tk()
        self.patuhan.title("Գրաֆի կառուցում")
        
        self.hanguytsner = {}  
        self.kaper = []       
        self.hamar = 1        
        
        self.stexcel_kochakner()
        
        self.stexcel_nkarelu_tarack()
        
    def stexcel_kochakner(self):
        kochakner = tk.Frame(self.patuhan)
        kochakner.pack(side=tk.LEFT, padx=10, pady=10)
        
        tk.Button(kochakner, text="Նոր հանգույց", command=self.nor_hanguyt).pack(pady=5)
        tk.Button(kochakner, text="Նոր կապ", command=self.nor_kap).pack(pady=5)
        tk.Button(kochakner, text="Մաքրել ամբողջը", command=self.makrel).pack(pady=5)
    
    def stexcel_nkarelu_tarack(self):
        self.nkar, self.nkarelu_tarack = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.nkar, master=self.patuhan)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, padx=10, pady=10)
    
    def nor_hanguyt(self):
        if len(self.hanguytsner) >= 10:  
            messagebox.showwarning("Ուշադրություն", "Առավելագույնը 10 հանգույց")
            return
        
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        
        self.hanguytsner[self.hamar] = (x, y)
        self.hamar += 1
        self.tarmatsnel_nkar()
    
    def nor_kap(self):
        if len(self.hanguytsner) < 2:
            messagebox.showwarning("Պետք են առնվազն 2 հանգույց")
            return
        
        kapi_patuhan = tk.Toplevel(self.patuhan)
        kapi_patuhan.title("Նոր կապ")
        
        tk.Label(kapi_patuhan, text="Սկիզբ:").pack()
        skizb = tk.Entry(kapi_patuhan)
        skizb.pack()
        
        tk.Label(kapi_patuhan, text="Վերջ:").pack()
        verj = tk.Entry(kapi_patuhan)
        verj.pack()
        
        def stexcel_kap():
            try:
                s = int(skizb.get())
                v = int(verj.get())
                if s in self.hanguytsner and v in self.hanguytsner:
                    self.kaper.append((s, v))
                    kapi_patuhan.destroy()
                    self.tarmatsnel_nkar()
                else:
                    messagebox.showerror("Սխալ", "Նման հանգույց չկա")
            except ValueError:
                messagebox.showerror("Սխալ", "Մուտքագրեք թվեր")
        
        tk.Button(kapi_patuhan, text="Ավելացնել", command=stexcel_kap).pack(pady=5)
    
    def makrel(self):
        self.hanguytsner.clear()
        self.kaper.clear()
        self.hamar = 1
        self.tarmatsnel_nkar()
    
    def tarmatsnel_nkar(self):        
        for hanguyt, dirk in self.hanguytsner.items():
            self.nkarelu_tarack.plot(dirk[0], dirk[1], 'o', markersize=20, color='pink')
            self.nkarelu_tarack.text(dirk[0], dirk[1], str(hanguyt), ha='center', va='center')
        
        for skizb, verj in self.kaper:
            skizb_dirk = self.hanguytsner[skizb]
            verj_dirk = self.hanguytsner[verj]
            self.nkarelu_tarack.annotate("", xy=verj_dirk, xytext=skizb_dirk,
                                       arrowprops=dict(arrowstyle="->"))
        
        self.nkarelu_tarack.set_xlim(-6, 6)
        self.nkarelu_tarack.set_ylim(-6, 6)
        self.nkarelu_tarack.set_aspect('equal')
        
        self.canvas.draw()

graf = GrafKarutsich()
graf.patuhan.mainloop()
