weather_options = ["sunny", "rainy", "cold"]  # Predefined weather conditions
weather = input("What's the weather like today? (sunny/rainy/cold): ")
if weather in weather_options:
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses!")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    else: 
        print("Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for '{weather}' weather.")
