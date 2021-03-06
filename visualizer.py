from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import main
from mergetest import mergesort

root = Tk()
root.title("Sorting visualisation")
root.maxsize(900, 600)
root.config(bg="black")

selected_alg = StringVar()
data = []


def draw_data(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600

    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10

    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340

        x1 = (i+1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def generate():

    global data
    data = []

    minVal = int(minEntry.get())
    maxVal = int(MaxEntry.get())
    size = int(sizeEntry.get())

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    draw_data(data, ["red" for x in range(len(data))])


def startAlgorithm():
    global data
    sorting = algMenu.get()
    time_taken = speedScale.get()
    if sorting == "Bubble sort":
        bubble_sort(data, draw_data, time_taken)
    elif sorting == "Quick sort":
        main(data, 0, len(data)-1, draw_data, time_taken)
    elif sorting == "Merge sort":
        mergesort(data, 0, len(data)-1, draw_data, time_taken)


UI_frame = Frame(root, width=600, height=200, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)


#row 0
Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=["Bubble sort", "Quick sort", "Merge sort"])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2,resolution=0.2, orient=HORIZONTAL, label="select speed")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=startAlgorithm,bg="red").grid(row=0, column=3, padx=5, pady=5)

#row1
sizeEntry = Scale(UI_frame, from_=3, to=30, length=200, digits=2,resolution=1, orient=HORIZONTAL, label="select size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)


minEntry = Scale(UI_frame, from_=0, to=10, length=200, digits=2,resolution=1, orient=HORIZONTAL, label="select min")
minEntry.grid(row=1, column=1, padx=5, pady=5)

MaxEntry = Scale(UI_frame, from_=10, to=100, length=200, digits=2,resolution=1, orient=HORIZONTAL, label="select max")
MaxEntry.grid(row=1, column=2, padx=5, pady=5)


Button(UI_frame, text="Generate", command=generate,bg="white").grid(row=1, column=3, padx=5, pady=5)


root.mainloop()
