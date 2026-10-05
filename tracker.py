
from datetime import date

def daily_checkin():
    print("=== SMP Daily Tracker ===")
    print(f"Date: {date.today()}")

    name = input("Enter your name: ")
    sleep = float(input("Hours of sleep: "))

    water = int(input("Glasses of water: "))
    steps = int(input("Number of steps: "))

    hit_goal = steps >= 10000

    print("\n=== Daily Report ===")
    print(f"Name: {name}")
    print(f"Sleep: {sleep} hours")
    print(f"Water: {water} glasses")
    print(f"Steps: {steps}")
    print(f"Goal achieved: {'Yes' if hit_goal else 'No'}")

if __name__ == "__main__":
    daily_checkin()