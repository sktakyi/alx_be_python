#assign & compute variables
weather = (input("What ’s the weather like today ? (sunny/rainy/cold): " ))

#display results 
if weather == ("sunny"):
    print ("Wear a t-shirt and sunglasses.")
elif weather == ("rainy"):
    print ("Don’t forget your umbrella and a raincoat.")
elif weather == ("cold"):
    print ("Sorry, I don’t have recommendations for this weather.")
else:
    print ("invalid input response")