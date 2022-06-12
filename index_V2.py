import mpmath
from tkinter import *
from tkinter import ttk
from sympy.calculus.util import continuous_domain
import sympy

class signal_drawer():
    global sign
    sign = {"Call": {"bg": "#EB4635", "text": "C all"}, "C": {"bg": "#EB4635"}, "left": {"text": "<<"}, "right": {"text": ">>"}, "Sin": {"bg": "#DBD7AB"}, "Cos": {"bg": "#DBD7AB"},
            "Tan": {"bg": "#DBD7AB"}, "plus": {"bg": "#A9E8DD", "text": "+"}, "sub": {"bg": "#A9E8DD", "text": "-"}, "mul": {"bg": "#A9E8DD", "text": "*"},
            "div": {"bg": "#A9E8DD", "text": "/"}, "pow": {"bg": "#A9E8DD", "text": "^"}, "x": {"bg": "#BAF2B1"}, "y": {"bg": "#BAF2B1"},
            "pi": {"bg": "#DB95AD", "text": "π"}, "e": {"bg": "#DB95AD"}, "ln": {"bg": "#C1D6DB"}, "log": {"bg": "#C1D6DB"}, "ra": {"bg": "#2364DB", "text": "("},
            "la": {"bg": "#2364DB", "text": ")"}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {},
            "7": {}, "8": {}, "9": {}, ".": {}, "0": {}, "eq": {"bg": "#91BA34", "text": "="}
            }
    global btns
    btns = []

    def __init__(self) -> None:
        self.Main = Tk()
        self.Main.geometry("1200x600+50+50")
        self.Main.resizable(False, False)
        ####################################################################
        self.screen = Text(self.Main, width=42, height=6 , state=NORMAL, bg="#98A872", font=(30), insertunfocussed='solid')
        self.screen.insert(1.0, "y=|")
        self.screen.config(state=DISABLED)
        self.screen.place(x=810, y=10)
        ####################################################################
        self.frame_btns = Frame(self.Main, width=380, height=500)
        self.frame_btns.place(x=810, y=160)

        FirstQ = Button(self.Main, width=7, height=1, text="First Q", bg="#555DEB")
        FirstQ.place(x=810, y=130)

        SecondQ = Button(self.Main, width=7, height=1, text="Second Q", bg="#555DEB")
        SecondQ.place(x=870, y=130)

        ThirdQ = Button(self.Main, width=7, height=1, text="Third Q", bg="#555DEB")
        ThirdQ.place(x=930, y=130)

        FourthQ = Button(self.Main, width=7, height=1, text="Fourth Q", bg="#555DEB")
        FourthQ.place(x=990, y=130)

        Multi = Button(self.Main, width=7, height=1, text="Multi Sign", bg="#555DEB")
        Multi.place(x=1050, y=130)

        Cross = Button(self.Main, width=10, height=1, text="Cross Signals", bg="#555DEB")
        Cross.place(x=1110, y=130)
        ####################################################################
        self.mainF = Canvas(self.Main, width=780, height=580, bg="#032B25")
        self.mainF.place(x=10, y=10)
        ####################################################################
        self.signal_Function = "y=|"
        self.function_checker = "f=|"
        ####################################################################

        def default(key, constraint):
            defaults = {"bg": "#aaaaaa", "fg": "#000000", "font_size": 20, "text": key}
            try:
                need = sign[key][constraint]
            except:
                need = defaults[constraint]
            return str(need)
        
        def drawbuttons():
            xx = 0
            yy = 10
            for mark in list(sign.keys()):
                if(xx % 300 == xx):
                    globals()[f"btn_{mark}"] = Button(self.frame_btns, width=8, height=1, text=default(mark, "text"), bg=default(mark, "bg"), fg=default(mark, "fg"), font=default(mark, "font_size"),
                                                        command=the_fken_btn)
                    globals()[f"btn_{mark}"].place(x=xx, y=yy)
                    xx += 100
                else:
                    globals()[f"btn_{mark}"] = Button(self.frame_btns, width=8, height=1, text=default(mark, "text"), bg=default(mark, "bg"), fg=default(mark, "fg"),  font=default(mark, "font_size"),
                                                        command=the_fken_btn)
                    globals()[f"btn_{mark}"].place(x=xx, y=yy)
                    xx = 0
                    yy += 55
                btns.append(globals()[f"btn_{mark}"])
        def btn_function(mark):
            self.screen.configure(state='normal')
            poin_1 = f'1.{str(self.screen.get("1.0" , END).find("|"))}'
            poin_2 = f'1.{str(self.screen.get("1.0" , END).find("|")+1)}'
            self.screen.delete(poin_1, poin_2)

            if mark in ["Sin", "Cos", "Tan", "log", "ln"]:
                self.signal_Function=self.signal_Function.replace("|", f"mpmath.{mark}(|".lower())
                self.function_checker = self.function_checker.replace("|", f"sympy.{mark}(|".lower())
                mark = mark + "(|"
                self.screen.insert(self.screen.index('insert'), mark)
            elif mark == "π":
                self.screen.insert(self.screen.index('insert'), mark)
                self.signal_Function = self.signal_Function.replace("|", f"mpmath.pi|")
                self.function_checker = self.function_checker.replace("|", f"sympy.pi|")
                self.screen.insert(poin_2, "|")
            elif mark == "e":
                self.screen.insert(self.screen.index('insert'), mark)
                self.signal_Function = self.signal_Function.replace("|", f"mpmath.e|")
                self.function_checker = self.function_checker.replace("|", f"sympy.E|")
                self.screen.insert(poin_2, "|")
            elif mark == "^":
                self.screen.insert(self.screen.index('insert'), mark)
                self.signal_Function = self.signal_Function.replace("|", f"**|")
                self.function_checker = self.function_checker.replace("|", f"**|")
                self.screen.insert(poin_2, "|")
            else:
                self.screen.insert(self.screen.index('insert'), mark)
                self.function_checker = self.function_checker.replace("|", f"{mark}|")
                self.signal_Function = self.signal_Function.replace("|", f"{mark}|")
                self.screen.insert(poin_2, "|")
            self.screen.mark_set("insert", f'1.{str(self.screen.get("1.0", END).find("|"))}')
            self.screen.configure(state='disabled')

        def delet(n):
            self.screen.configure(state='normal')
            if n == 1:
                self.screen.delete(1.0, END)
                self.screen.insert(END, "y=|")
                self.signal_Function = "y=|"
                self.function_checker = "f=|"
            elif n == 2:
                postion = int(self.screen.get("1.0", END).find("|"))
                postionInsideSignal = int(self.signal_Function.find("|"))
                postionInsideChecker = int(self.function_checker.find("|"))
                if not chk():
                    self.screen.delete(f'1.{postion - 1}', f'1.{postion + 1}')
                    self.screen.insert(f"1.{postion - 1}", "|")
                    self.screen.mark_set("insert", f'1.{self.screen.get("1.0" , END).find("|")}')
                    self.signal_Function = self.signal_Function[:postionInsideSignal-1]+self.signal_Function[postionInsideSignal:]
                    self.function_checker = self.function_checker[:postionInsideChecker-1]+self.function_checker[postionInsideChecker:]
                elif chk() == 1:
                    self.screen.delete(f'1.{postion-4}', f'1.{postion+2}')
                    self.screen.insert(f"1.{postion-4}", "|")
                    self.screen.mark_set("insert", f'1.{self.screen.get("1.0" , END).find("|")}')
                    self.signal_Function = self.signal_Function[:postionInsideSignal-11]+self.signal_Function[postionInsideSignal:]
                    self.function_checker = self.function_checker[:postionInsideChecker-10]+self.function_checker[postionInsideChecker:]
                elif chk() == 2:
                    self.screen.delete(f'1.{postion-3}', f'1.{postion+2}')
                    self.screen.insert(f"1.{postion-3}", "|")
                    self.screen.mark_set("insert", f'1.{self.screen.get("1.0" , END).find("|")}')
                    self.signal_Function = self.signal_Function[:postionInsideSignal-10]+self.signal_Function[postionInsideSignal:]
                    self.function_checker = self.function_checker[:postionInsideChecker-9]+self.function_checker[postionInsideChecker:]
            self.screen.configure(state='disabled')

        def chk(n=""):
            if n == "":
                behind_1 = self.screen.get(f'1.{int(self.screen.index("insert")[2:])-4}', f'1.{int(self.screen.index("insert")[2:])+2}')
                behind_2 = self.screen.get(f'1.{int(self.screen.index("insert")[2:])-3}', f'1.{int(self.screen.index("insert")[2:])+2}')
                behind_3 = self.screen.get(f'1.{int(self.screen.index("insert")[2:])-4}', f'1.{int(self.screen.index("insert")[2:])}')
                behind_4 = self.screen.get(f'1.{int(self.screen.index("insert")[2:])-3}', f'1.{int(self.screen.index("insert")[2:])}')
                if behind_1 in ["Sin(|)", "Cos(|)", "Tan(|)", "log(|)"] or behind_3 in ["Sin(|", "Cos(|", "Tan(|", "log(|", "Sin()", "Cos()", "Tan()", "log()", "Sin(", "Cos(", "Tan(", "log("]:
                    return 1
                elif behind_4 in ["ln(|", "ln(", "ln()"] or behind_2 in ["ln(|)", "ln()"]:
                    return 2
                else:
                    return 0
            elif n == "1":
                forward_1 = self.screen.get(f'1.{int(self.screen.index("insert")[2:])+1}', f'1.{int(self.screen.index("insert")[2:])+5}')
                forward_2 = self.screen.get(f'1.{int(self.screen.index("insert")[2:])+1}', f'1.{int(self.screen.index("insert")[2:])+4}')
                if forward_1 in ["Sin(", "Cos(", "Tan(", "log("]:
                    return 1
                elif forward_2 in ["ln("]:
                    return 2
                else:
                    return 0
        
        def move_pointer(n):
            self.screen.config(state=NORMAL)
            postion = int(self.screen.get("1.0", END).find("|"))
            if n == 1:
                if not chk():
                    self.screen.delete(f'1.{postion}', f'1.{postion+1}')
                    self.screen.insert(f"1.{postion - 1}", "|")
                elif chk() == 1:
                    self.screen.delete(f'1.{postion}', f'1.{postion+1}')
                    self.screen.insert(f"1.{postion - 4}", "|")
                elif chk() == 2:
                    self.screen.delete(f'1.{postion}', f'1.{postion+1}')
                    self.screen.insert(f"1.{postion - 3}", "|")
            elif n == 2:
                if not chk("1"):
                    self.screen.delete(f'1.{postion}', f'1.{postion+1}')
                    self.screen.insert(f"1.{postion + 1}", "|")
                elif chk("1") == 1:
                    self.screen.delete(f'1.{postion}', f'1.{postion+1}')
                    self.screen.insert(f"1.{postion + 4}", "|")
                elif chk("1") == 2:
                    self.screen.delete(f'1.{postion}', f'1.{postion+1}')
                    self.screen.insert(f"1.{postion + 3}", "|")
            self.screen.mark_set("insert", f'1.{self.screen.get("1.0" , END).find("|")}')
            self.screen.config(state=DISABLED)

        the_sign = list(sign.keys())

        def the_fken_btn():
            btns[0].config(command=lambda: delet(1))
            btns[1].config(command=lambda: delet(2))
            btns[2].config(command=lambda: move_pointer(1))
            btns[3].config(command=lambda: move_pointer(2))
            btns[4].config(command=lambda: btn_function(default(the_sign[4], "text")))
            btns[5].config(command=lambda: btn_function(default(the_sign[5], "text")))
            btns[6].config(command=lambda: btn_function(default(the_sign[6], "text")))
            btns[7].config(command=lambda: btn_function(default(the_sign[7], "text")))
            btns[8].config(command=lambda: btn_function(default(the_sign[8], "text")))
            btns[9].config(command=lambda: btn_function(default(the_sign[9], "text")))
            btns[10].config(command=lambda: btn_function(default(the_sign[10], "text")))
            btns[11].config(command=lambda: btn_function(default(the_sign[11], "text")))
            btns[12].config(command=lambda: btn_function(default(the_sign[12], "text")))
            btns[13].config(command=lambda: btn_function(default(the_sign[13], "text")))
            btns[14].config(command=lambda: btn_function(default(the_sign[14], "text")))
            btns[15].config(command=lambda: btn_function(default(the_sign[15], "text")))
            btns[16].config(command=lambda: btn_function(default(the_sign[16], "text")))
            btns[17].config(command=lambda: btn_function(default(the_sign[17], "text")))
            btns[18].config(command=lambda: btn_function(default(the_sign[18], "text")))
            btns[19].config(command=lambda: btn_function(default(the_sign[19], "text")))
            btns[20].config(command=lambda: btn_function(default(the_sign[20], "text")))
            btns[21].config(command=lambda: btn_function(default(the_sign[21], "text")))
            btns[22].config(command=lambda: btn_function(default(the_sign[22], "text")))
            btns[23].config(command=lambda: btn_function(default(the_sign[23], "text")))
            btns[24].config(command=lambda: btn_function(default(the_sign[24], "text")))
            btns[25].config(command=lambda: btn_function(default(the_sign[25], "text")))
            btns[26].config(command=lambda: btn_function(default(the_sign[26], "text")))
            btns[27].config(command=lambda: btn_function(default(the_sign[27], "text")))
            btns[28].config(command=lambda: btn_function(default(the_sign[28], "text")))
            btns[29].config(command=lambda: btn_function(default(the_sign[29], "text")))
            btns[30].config(command=lambda: btn_function(default(the_sign[30], "text")))
            btns[31].config(command=lambda: drawer(self.mainF, 40))

        def drawQ(Quarter, Q , width, height):
            Quarter.create_rectangle(390, 290, 390+width, 290+height, fill="#A09CB8")
            i = 1
            while i*20 < 390:
                if Q == 1:
                        Quarter.create_text(width +i*20 , -height-14, text=i)                               #x
                        # Quarter.create_text(width + 10, -height- i*20 -10, text=i)                          #y
                elif Q == 2:   
                        # Quarter.create_text(-width - i*20 - 12, -height-14, text=i)                         #x
                        Quarter.create_text(-width - 14, -height - i*20 - 10, text=i)                       #y
                elif Q == 3:
                        Quarter.create_text(-width-i*20 -14, height+10, text=-i)                            #x
                        # Quarter.create_text(-width-15,height+ i*20, text=-i)                                #y
                elif Q == 4:
                        # Quarter.create_text(width + i*20 ,height+10, text=i)                                #x
                        Quarter.create_text(width + 10, height +i*20 , text=-i)                             #y    
                i += 1

        def drawPoints(access_name, start, end):
            start_opsite = start
            if access_name == "X":
                while start-20 < end:
                    if start == 389:
                        mark = Frame(self.mainF, width=1, height=1000, bg="white" , bd=-2)
                    else:
                        mark = Frame(self.mainF, width=1, height=1000, bg="gray", bd=-2)
                    start_opsite -= 20
                    mark_opsite = Frame(self.mainF, width=1, height=1000, bg="gray", bd=-2)
                    mark.place(x=start, y=0)
                    mark_opsite.place(x=start_opsite, y=0)
                    start += 20
            elif access_name == "Y":
                while start < end:
                    if start == 289:
                        mark = Frame(self.mainF, width=1000, height=1, bg="white", bd=-2)
                    else:
                        mark = Frame(self.mainF, width=1000, height=1, bg="gray", bd=-2)
                    start_opsite -= 20
                    mark_opsite = Frame(self.mainF, width=1000, height=1, bg="gray", bd=-2)
                    mark.place(x=0, y=start)
                    mark_opsite.place(x=0, y=start_opsite)
                    start += 20

        def drawer(Quarter, i):
            self.mainF.delete('square')
            x,q = 0,0
            g = sympy.symbols("x")
            self.signal_Function = self.signal_Function.replace("|" , "")    
            self.function_checker = self.function_checker.replace("x", "g")
            self.function_checker = self.function_checker.replace("|", "")
            exec(self.function_checker)
            exec("""
try:
    exec(self.signal_Function)
except:
    q += 0.1
    x += 0.1
if continuous_domain(f, g, sympy.Reals) == sympy.Reals:
    arr = [389+ q * 20, 289-float(y*20), 389 +q *20+1, 289-float(y*20+1)]
    self.mainF.create_line(arr , width=2, tags="square")
    while x < i/2:
        try:
            exec(self.signal_Function)
            arr.insert(0 , 289-float(y*20))
            arr.insert(0 , 389+ q * 20)
            x = -x
            try:
                exec(self.signal_Function)
                if not isinstance(y , complex):
                    arr.append(389- q * 20)
                    arr.append(289-float(y*20))
                    x = -x
                else:
                    x = -x
            except:
                x = -x
            self.mainF.delete("square")
            self.mainF.create_line(arr , width=2, tags="square")
        except:
            pass
        Quarter.update()
        q += 0.05
        x += 0.05
else:
    while x < i/2:
        try:
            try:
                exec(self.signal_Function)
                exec(f"Quarter.create_oval(389+ q * 20, 289-float(y*20), 389 +q *20+1, 289-float(y*20+1) ,tags='square')")
            except:
                pass
            x = -x
            try:
                try:
                    exec(self.signal_Function)
                    exec(f"Quarter.create_oval(389- q * 20, 289-float(y*20), 389 -q *20+1, 289-float(y*20+1) ,tags='square')")
                except:
                    pass
                x = -x
            except:
                x=-x
        except:
            pass
        Quarter.update()
        q += 0.01
        x += 0.01
            """)
            self.signal_Function = self.signal_Function + "|"
#####################################################################
        drawbuttons()
        drawQ(self.mainF, 1, 394, -294)
        drawQ(self.mainF, 2, -394, -294)
        drawQ(self.mainF, 3, -394, 294)
        drawQ(self.mainF, 4, 394, 294)

        # the center (x = 389 , y = 289)

        drawPoints("X", 389, 780)
        drawPoints("Y", 289, 580)

        self.Main.mainloop()

my_program = signal_drawer()

