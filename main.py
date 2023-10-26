from tkinter import *

myWindows = Tk()
myWindows.minsize(width=450, height=300)

myLabel = Label(text="enter your Weight(kg)")
myLabel.pack()

myResultLabel = Label()

myWeightEntry = Entry()
myWeightEntry.config(width=10)
myWeightEntry.pack()

myLabel2 = Label(text="enter your Height(m)")
myLabel2.pack()

# weight entry
myHeightEntry = Entry()
myHeightEntry.config(width=10)
myHeightEntry.pack()


def calculatorBMI():
    height = myHeightEntry.get()
    weight = myWeightEntry.get()
    weightINT = int(weight)
    heightINT = float(height)
    result = weightINT / heightINT ** 2
    print(result)

    if result < 18.5:
        myResultLabel.config(text=f"Your BMI is:{result} = Underweight")
    elif 18.5 < result < 24.9:
        myResultLabel.config(text=f"Your BMI is:{result} = Normal Range")
    elif 25 < result < 29.9:
        myResultLabel.config(text=f"Your BMI is:{result} = Overweight")
    else:
        myResultLabel.config(text=f"Your BMI is:{result} = Obese")


myButton = Button(text="Calculate", command=calculatorBMI)
myButton.config(width=10)
myButton.pack()
myResultLabel.pack()
myWindows.mainloop()
