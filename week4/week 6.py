import tkinter as tk

root = tk.Tk()                 # Create the main window
root.title("My First GUI")     # Window title
root.geometry("320x200")       # Optional: width x height
root.mainloop()                # Start the event loop9


def main():
    old, new=input_balance()
    charge=finance_charge(old, new)
    print(charge)

def input_balance():
    old_balance=int(input("enter the old balance"))
    new_balance=int(input("enter the new balance"))
    return old_balance, new_balance

def finance_charge(old, new):
    if new<=20:
        charge=new+0.012*old
    return charge
main()

def main():
    
 Planets = [('Mercury', 75, 1), ('Venus', 460, 2), ('Mars', 140, 4), ('Earth', 510, 3), ('Jupiter', 62000, 5), ('Neptune', 7640, 8), ('Saturn', 42700, 6 ), ('Uranus',8100, 7)]
 Planets.sort(key=sortbyplanets, reverse=True)
 for state in Planets:
    print(state[0])
def sortbyplanets(state):
     return state[2]
main()
