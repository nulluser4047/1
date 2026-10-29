"""Pradera pixelada. Ejecutar con: python3 minecraftmood.py."""
import math
import random
import time
import tkinter as tk

WIDTH, HEIGHT = 960, 600


def render(canvas, seed, sunset=False):
    """Dibuja una escena reproducible sin imágenes ni dependencias externas."""
    rng = random.Random(seed)
    canvas.delete('all')

    def block(x, y, w, h, color):
        canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline='')

    def polygon(points, color):
        canvas.create_polygon(points, fill=color, outline='')

    block(0, 0, WIDTH, HEIGHT, '#db9e93' if sunset else '#94d2df')
    block(0, 155, WIDTH, 160, '#edbd9b' if sunset else '#bce5df')
    block(770, 55, 48, 48, '#ffdb94' if sunset else '#fff1b5')
    for _ in range(12):
        x, y = rng.randrange(-60, WIDTH), rng.randrange(25, 150)
        color = '#f5d5ba' if sunset else '#f4f6e2'
        block(x, y, 80, 15, color)
        block(x + 16, y - 12, 42, 12, color)
        block(x + 52, y + 8, 48, 12, color)

    for x in range(-40, WIDTH, 65):
        h = rng.randrange(40, 100)
        polygon([x, 285, x, 230-h//2, x+18, 230-h//2,
                 x+18, 230-h, x+45, 230-h, x+45, 230-h//2,
                 x+65, 230-h//2, x+88, 285], '#86a6a3')
    for x in range(-20, WIDTH, 35):
        y = rng.randrange(235, 270)
        block(x, y, 45, 65, '#628d70')
        block(x+10, y-12, 25, 15, '#628d70')

    block(0, 280, WIDTH, HEIGHT-280, '#88ad54')
    for x, y, w in [(0, 365, 200), (200, 347, 240),
                    (440, 370, 240), (680, 340, 280)]:
        block(x, y, w, HEIGHT-y, '#729c46')
        block(x, y, w, 15, '#756344')
        block(x, y-7, w, 7, '#a0be60')
    polygon([490, 280, 505, 280, 505, 330, 535, 330, 535, 380,
             510, 380, 510, 440, 465, 440, 465, 510, 420, 510,
             420, 600, 340, 600, 340, 500, 400, 500, 400, 430,
             460, 430, 460, 370, 505, 370, 505, 340, 490, 340], '#cdb981')
    for _ in range(1800):
        x, y = rng.randrange(WIDTH), rng.randrange(288, HEIGHT)
        block(x, y, rng.randrange(2, 7), 2, rng.choice(['#648e3e', '#abc36c']))

    def tree(x, y, scale):
        def cube(a, b, w, h, c):
            block(x+a*scale, y+b*scale, w*scale, h*scale, c)
        polygon([x-20*scale, y, x+35*scale, y-8*scale,
                 x+65*scale, y+10*scale, x, y+18*scale], '#52783d')
        cube(-6, -65, 16, 68, '#755335')
        cube(4, -65, 6, 68, '#503c2b')
        cube(-2, -47, 3, 22, '#a27b47')
        for a, b, w, h, color in [(-38, -95, 72, 35, '#39703c'),
                                  (-48, -126, 90, 38, '#488643'),
                                  (-30, -151, 60, 32, '#609c48'),
                                  (-12, -164, 34, 22, '#78ab50')]:
            cube(a, b, w, h, color)
            cube(a+w-12, b, 12, h, '#34683a')
        for _ in range(30):
            cube(rng.randrange(-28, 26), rng.randrange(-135, -70),
                 6, 4, rng.choice(['#75a94d', '#3f7b3d']))

    for x, y, s in [(105, 320, .65), (700, 310, .6), (850, 355, .9),
                    (260, 355, .8), (90, 490, 1.2), (735, 485, 1.1),
                    (900, 565, 1.3)]:
        tree(x, y, s)

    flower_colors = ['#f2c94c', '#ed87b3', '#b79be2', '#f7efdb', '#f27c63', '#80b9ed']
    for _ in range(260):
        x, y = rng.randrange(15, WIDTH-15), rng.randrange(310, HEIGHT-5)
        if 335 < x < 540 or (x < 150 and y > 390) or (x > 700 and y > 420):
            continue
        size = 3 if y > 450 else 2
        block(x, y, size, size*5, '#3d7338')
        block(x+size, y+size*2, size*2, size, '#509044')
        color = rng.choice(flower_colors)
        block(x-size, y-size*2, size*3, size*3, color)
        block(x, y-size*3, size, size*5, color)
        block(x, y-size, size, size, '#ffe5a0')



class DrawingQueue:
    """Record drawing commands so Tk can display them progressively."""

    def __init__(self):
        self.commands = []

    def delete(self, *args):
        self.commands.clear()

    def create_rectangle(self, *args, **kwargs):
        self.commands.append(("rectangle", args, kwargs))

    def create_polygon(self, *args, **kwargs):
        self.commands.append(("polygon", args, kwargs))


class MinecraftMood:
    def __init__(self, root):
        self.root = root
        self.seed = random.randrange(100000)
        self.sunset = False
        self.drawing_job = None
        self.wind_job = None
        self.grass = []
        self.started = time.monotonic()
        root.title("Minecraft Mood · Un pequeño mundo")
        root.configure(bg="#14262b")
        root.resizable(False, False)
        tk.Label(root, text="MINECRAFT MOOD", font=("Courier", 22, "bold"),
                 bg="#14262b", fg="#eff0d4").pack(pady=(18, 8))
        tk.Label(root, text="Un campo de bloques y una brisa tranquila",
                 bg="#14262b", fg="#acc0b4").pack(pady=(0, 16))
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                                highlightthickness=0)
        self.canvas.pack(padx=20)
        controls = tk.Frame(root, bg="#14262b")
        controls.pack(pady=16)
        style = dict(bg="#dce9a7", fg="#203b2c", relief="flat",
                     padx=15, pady=9, cursor="hand2")
        tk.Button(controls, text="Nuevo paisaje", command=self.regenerate,
                  **style).pack(side="left", padx=8)
        self.light = tk.Button(controls, text="Ver atardecer",
                               command=self.toggle_time, **style)
        self.light.pack(side="left", padx=8)
        self.status = tk.Label(root, bg="#14262b", fg="#acc0b4")
        self.status.pack(pady=(0, 12))
        root.protocol("WM_DELETE_WINDOW", self.close)
        self.prepare()
        self.animate_wind()

    def prepare(self):
        if self.drawing_job is not None:
            self.root.after_cancel(self.drawing_job)
            self.drawing_job = None
        self.canvas.delete("all")
        self.canvas.configure(bg="#dc9a89" if self.sunset else "#91cdd5")
        self.grass = []
        queue = DrawingQueue()
        render(queue, self.seed, self.sunset)
        self.commands = queue.commands
        self.index = 0
        self.status.config(text="El mundo está apareciendo...")
        self.draw_next()

    def draw_next(self):
        self.drawing_job = None
        end = min(self.index + 12, len(self.commands))
        while self.index < end:
            kind, args, kwargs = self.commands[self.index]
            getattr(self.canvas, "create_" + kind)(*args, **kwargs)
            self.index += 1
        if self.index < len(self.commands):
            self.drawing_job = self.root.after(20, self.draw_next)
        else:
            self.add_grass()
            self.status.config(text="La brisa recorre la pradera...")

    @staticmethod
    def grass_shape(x, y, height, sway):
        middle = round(sway / 2)
        return (x-2, y, x-2, y-height//2,
                x+middle-2, y-height//2, x+middle-2, y-height+3,
                x+sway-1, y-height+3, x+sway-1, y-height,
                x+sway+2, y-height, x+sway+2, y-height+3,
                x+middle+2, y-height+3, x+middle+2, y-height//2,
                x+2, y-height//2, x+2, y)

    def add_grass(self):
        rng = random.Random(self.seed + 1)
        for _ in range(230):
            x, y = rng.randrange(15, WIDTH-15), rng.randrange(310, HEIGHT-8)
            if 310 < x < 545 or (x < 165 and y > 375) or (x > 660 and y > 380):
                continue
            height = rng.randrange(7, 15)
            phase = rng.random() * math.tau
            item = self.canvas.create_polygon(
                self.grass_shape(x, y, height, 0), outline="",
                fill=rng.choice(["#417537", "#54883b", "#bad371"]))
            self.grass.append((item, x, y, height, phase))

    def animate_wind(self):
        elapsed = time.monotonic() - self.started
        for item, x, y, height, phase in self.grass:
            sway = round(math.sin(elapsed*1.8-x*.012+phase*.25)*3
                         + math.sin(elapsed*2.7+phase)*.7)
            self.canvas.coords(item, *self.grass_shape(x, y, height, sway))
        self.wind_job = self.root.after(40, self.animate_wind)

    def regenerate(self):
        self.seed = random.randrange(100000)
        self.prepare()

    def toggle_time(self):
        self.sunset = not self.sunset
        self.light.config(text="Ver día" if self.sunset else "Ver atardecer")
        self.prepare()

    def close(self):
        for job in (self.drawing_job, self.wind_job):
            if job is not None:
                self.root.after_cancel(job)
        self.root.destroy()


def main():
    root = tk.Tk()
    MinecraftMood(root)
    root.mainloop()


if __name__ == "__main__":
    main()
