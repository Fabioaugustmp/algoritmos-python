hour: int #Hora

hour = int(input("Provide a hour of the day!"))

if hour < 12:
    print("Good Morning")
elif hour >= 13 | hour <= 18:
    print("Still work time!")
else:
    print("Good Afternoon")
