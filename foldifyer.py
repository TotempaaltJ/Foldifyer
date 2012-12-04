import time, decimal
import turtle
from math import sqrt

def fold_once(line, instr):
    switch = True if instr == 'r' else False
    yield switch
    for i in line:
        switch = not switch
        yield i
        yield switch

def nice(line):
    for i in line:
        if i: yield 'R'
        else: yield 'L'

def fold(instr, nice=True):
    if instr.replace('r', '').replace('l', '') != '':
        raise ValueError("Please use 'r' and 'l' only.")
    line = []
    for step in instr:
        # the first time this happens, line becomes a generator
        line = fold_once(line, step)

    if nice:
        return nice(line)
    else:
        return line

class Drawer(object):
    def __init__(self, instr, length=30, angle=90, rounding=0, t=None):
        self.instr = instr
        self.length = length
        self.angle = angle
        self.rounding = rounding
        
        self.t = t if t is not None else turtle
        self.t.reset()
        self.t.hideturtle()
        self.steps = decimal.Decimal(2**len(instr)-1)
        self.step_n = 0
        # These are all timestamps since epoch (convert with time.ctime)
        self.start = 0
        self.time_diff = 0
        self.eta = 0

    def draw(self):
        line = fold(self.instr, False)
        self.start = decimal.Decimal(time.time())
        for step in line:
            self.step(step)

        self.t.forward(self.length)

    def step(self, step):
        self.t.forward(self.length-self.rounding)
        direction = self.t.right if step else self.t.left
        
        direction(self.angle/2)
        self.t.forward(sqrt(2*self.rounding**2))
        direction(self.angle/2)

        self.step_n += decimal.Decimal(1)
        self.time_diff = decimal.Decimal(time.time()) - self.start
        self.eta = self.start + (self.time_diff/self.step_n) * self.steps
        

def draw_fold(instr, length=30, angle=90, rounding=0, t=None):
    if t is None:
        t = turtle
    t.reset()
    t.hideturtle()
    line = fold(instr, False)
    for step in line:
        t.forward(length-rounding)
        direction = t.right if step else t.left
        
        direction(angle/2)
        t.forward(sqrt(2*rounding^2))
        direction(angle/2)

    t.forward(length)


from Tkinter import *

class TKDrawer(Drawer):
    def __init__(self, instr, stringvar, length=30, angle=90, rounding=0, t=None):
        super(TKDrawer, self).__init__(instr, length, angle, rounding, t)
        self.stringvar = stringvar

    def step(self, step):
        super(TKDrawer, self).step(step)
        try:
            self.stringvar.set('ETA: ' + time.ctime(float(self.eta)))
        except ValueError:
            from_now = self.eta - decimal.Decimal(time.time())
            self.stringvar.set('ETA: ' + str(from_now) + ' seconds from now')

class Settings(Frame):
    def create_widgets(self):
        self.length = Scale(self, label='Length', from_=0, to=50, orient=HORIZONTAL)
        self.length.set(20)
        self.length.pack()
        
        self.angle = Scale(self, label='Angle', from_=0, to=180, orient=HORIZONTAL)
        self.angle.set(90)
        self.angle.pack()

        self.rounding = Scale(self, label='Rounding', from_=0, to=10, orient=HORIZONTAL)
        self.rounding.set(4)
        self.rounding.pack()

        self.stringvar = StringVar(value='Eta: ...')
        self.eta = Label(self, textvariable=self.stringvar)
        self.eta.pack()
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


class Instructions(Frame):
    def create_widgets(self):
        self.instr = Entry(self, width=60)
        self.instr.pack(side='left', expand=1)

        self.draw = Button(self)
        self.draw['text'] = 'Draw'
        self.draw['command'] = self.master.master.draw_cv
        self.draw.pack(side='right')

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

class Application(Frame):
    def draw_cv(self):
        settings = self.left
        instr = self.f_instr.instr.get()
        length = settings.length.get()
        angle = settings.angle.get()
        rouding = settings.rounding.get()

        drw = TKDrawer(instr, self.left.stringvar, length, angle, rouding, t=self.turtle)
        drw.draw()
    
    def create_widgets(self):
        self.left = Settings(self)
        self.right = Frame(self)
        
        self.cv = Canvas(self.right, width=1440, height=850)
        self.cv.pack(side=TOP)
        self.init_turtle()

        self.f_instr = Instructions(self.right)
        self.f_instr.pack(side='bottom')

        self.left.pack(side='left')
        self.right.pack(side='right')

    def init_turtle(self):
        self.turtle = turtle.RawTurtle(self.cv)
        self.turtle.hideturtle()
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title('Foldifyer')
    app.mainloop()
    root.destroy()
