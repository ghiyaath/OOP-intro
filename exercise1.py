from tkinter import messagebox

td = datetime.datetime.today()
for i in range(10):
    answer = td + datetime.timedelta(days=7)
    td = answer
    print(answer.date())
