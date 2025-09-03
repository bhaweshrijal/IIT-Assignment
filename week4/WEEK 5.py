'''
def name(name):
    name=input("name?")
    return name
print("hello", name(name))

def add(a,b):#parameter
    return a+b
print(add(2,3)) #here 2,3 are argument
def add(a,b):
   return mysum
print(add(2,3))

def power(base,exp=2):
    return base**exp
print(power(5)) #25
print(power(5,exp=3)) #125

def power():
    base=int(input("enter the base"))
    exp=int(input("enter the exp"))
    return base**exp
print(power())

def square():
    n=int(input(("enter any num")))
    return n**2
print(square())

def even(n):
    if (n%2==0):
        return True
    else:
        return False
print(even(2))


def full_name(first, last):
   return last+" "+ first
     
print(full_name("sam", "black"))


# --- Student Starter ---
# Save as drone_helper.py and run in IDLE/terminal

def is_voltage_safe(v):
    """Return True if voltage is in the safe range [3.5, 4.2]."""
    return 3.5 <= v <= 4.2


def estimate_minutes(v):
    """Estimate remaining minutes (linear from 3.5V=0 to 4.2V=10)."""
    if v < 3.5:
        return 0
    if v > 4.2:
        v = 4.2
    minutes = (v - 3.5) * (10 / 0.7)
    return round(minutes, 1)


def format_status(v):
    """Return a friendly string with safety + minutes."""
    safe = is_voltage_safe(v)
    mins = estimate_minutes(v)
    if not safe:
        return f"Voltage {v}V is UNSAFE. Land now. Est. {mins} min."
    else:
        return f"Voltage {v}V is safe. Est. {mins} min remaining."


# --- Simple I/O ---
reading_str = input("Enter voltage reading (e.g., 3.9): ")
voltage = float(reading_str)
print(format_status(voltage))

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
        charge=new+0.15*old
    return charge
main()
'''
def main():
    
 Planets = [('Mercury', 75, 1), ('Venus', 460, 2), ('Mars', 140, 4), ('Earth', 510, 3), ('Jupiter', 62000, 5), ('Neptune', 7640, 8), ('Saturn', 42700, 6 ), ('Uranus',8100, 7)]
 Planets.sort(key=sortbyplanets(yo), reverse=True)
 for state in Planets:
    print(state[0])
def sortbyplanets(state):
     return state[2]
main()    

    
                
    

