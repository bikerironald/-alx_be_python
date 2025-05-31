# # Weather Recommendation System
# # This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.
# Weather = input(" What's the weather like today? (sunny/rainy/cold): ")
# if Weather == "sunny":
#     print("Wear a t-shirt and sunglasses.")
# elif Weather == "rainy":
#     print("Don't forget your umbrella and a raincoat.")
# elif Weather == "cold":
#     print("Make sure to wear a warm coat and a scarf.")
# else:
#     print("Sorry, I don't have recommendations for this weather.")  




# Weather Recommendation System
# This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.
Weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
if Weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif Weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif Weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")