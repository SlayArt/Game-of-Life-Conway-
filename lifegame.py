# importation des modules necessaires
import numpy as np
import tkinter as tk


# initialisation des variables
size = 100


def initial(size, alive_prob):
    return np.random.choice([0, 1], size=(size, size), p=[1-alive_prob, alive_prob])

tab = initial(size, 0)
temp_tab = np.copy(tab)

iterations = 0

root = tk.Tk()
root.title("Life game of Conway")

cell_size = 10
canvas = tk.Canvas(root, width=size * cell_size, height=size * cell_size)
canvas.pack()

running = True


# initialisation des fonctions
def verif():
    global count, tab, temp_tab

    if running:
        for cellx in range(size):
            for celly in range(size):

                count = 0

                for i in range(cellx - 1, cellx + 2):
                    for j in range(celly - 1, celly + 2):
                    
                        if i == cellx and j == celly:
                            continue

                        if 0 <= i < size and 0 <= j < size and tab[i][j]:
                            count += 1

                if count == 3:
                    temp_tab[cellx][celly] = True
                elif count < 2 or count > 3:
                    temp_tab[cellx][celly] = False 
                else:
                    temp_tab[cellx][celly] = tab[cellx][celly]


        tab = np.copy(temp_tab)

    grid()
    root.after(50, verif)

def grid():
    canvas.delete("all")
    for i in range(size):
        for j in range(size):
            color = 'green' if tab[i][j] == 1 else 'black'
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="grey")

def click_state(event):
    x, y = event.x // cell_size, event.y // cell_size
    if 0 <= x < size and 0 <= y < size :
        tab[y][x] = 1 - tab[y][x]
        grid()
canvas.bind("<Button-1>", click_state)

def toggle_sim(event):
    global running
    running = not running
root.bind("<space>", toggle_sim)


# main code
grid()
root.after(50, verif)
root.mainloop()