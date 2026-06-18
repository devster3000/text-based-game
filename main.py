import time as t
import matplotlib.pyplot as plt


def main():
    print(f"{'*'*7} Welcome to this Game!!! {'*'*7}")
    
    while True:
        try:
            username = str(input("What's your name, brave adventurer?\n>>> "))
        except:
            if len(username) < 3:
                print("Sorry, your name must be longer than 3 characters.")
                continue
            else:
                print(f"Welcome, {username}!")
                break
