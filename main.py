print("Welcome to the Weather Advice Giver [WAG]!")
print("Want to know what to wear tomorrow?")
weather = input("Temperature: ")
forecast = int(weather)
rain = input ("Will it rain [yes/no]: ")
umbrella = rain
if umbrella == "yes":
    print("Take your umbrella or get sick. Your choice!")
if forecast >= 20:
    print("Wear your favorite shirt and baggy jeans!")
elif forecast >= 10 and forecast < 20:
    print("Wear your favorite shirt and baggy jeans, but consider wearing your favorite windbreaker!")
elif forecast >= 5 and forecast < 10:
    print("Whatever you do, don't forget your jacket.")
else:
    print("Wear everything in your closet and prepare hot chocolate for when you get back.")
