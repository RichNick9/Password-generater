#Made by Nick Austin
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()_-+={]};:,.!@#$%^&*/?"

upper, lower, nums, syms = True, True, True, True  #If you dont want one of the items to be used in the password set the correspondent to false 

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20 #length of the password
amount = 10 #How many passwords are generated

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)