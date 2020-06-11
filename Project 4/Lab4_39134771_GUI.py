import tkinter as tk
from Lab4_39134771 import MapQuest

m = MapQuest('cVFJvqGmXgGBAApVucLyj9ouoeTOuN6d')

root = tk.Tk()
root.title('Lab_4_39134771 GUI')
root.geometry('800x300')
root.resizable(True,True)
locationValue = tk.StringVar()
keywordValue = tk.StringVar()
result = tk.IntVar()

label1 = tk.Label(root, text = 'Location:')
label1.grid(row = 0, column = 0)
location = tk.Entry(root, textvariable = locationValue, width = 30)
location.grid(row = 0, column = 1)

label2 = tk.Label(root, text = "Keyword")
label2.grid(row = 0 , column = 2)
keyword = tk.Entry(root, textvariable = keywordValue, width = 15)
keyword.grid(row = 0 , column  = 3)

label3 = tk.Label(root, text = "Number of results:")
label3.grid( row = 0, column = 4)
results = tk.OptionMenu(root, result, 5, 10 , 15 , 20 , 25, 30).grid(row = 0, column = 5)

label4 = tk.Label(root, text= 'Results:')
label4.grid(row = 1, column = 0, sticky = 'W')

label5text=tk.StringVar()
label5 = tk.Label(root,textvariable=label5text)
label5.grid(row = 1, column = 1)


def display():
    #global location,keyword,result
    #global label5
    returnValue = m.pointOfInterest(locations=locationValue.get(),keyword=keywordValue.get(),result=result.get())
    tempStr = "\n\n"
    for i in returnValue:
        tempStr += i + '\n'
    label5text.set(tempStr)
    #label5.config(text = returnValue)

button = tk.Button(root, text = 'Search', command = display).grid(row = 0, column = 7)

root.mainloop()


