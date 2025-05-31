# Weather Recommendation System
# This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.
user = input(" What's the weather like today? (sunny/rainy/cold): ")
if user.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")  
