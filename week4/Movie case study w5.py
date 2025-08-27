
# Starter
movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}
user="continue"

purchases = []  # list of (title, qty, price_each)
while(user=="continue"):
    movie=input("enter the mmovie title").lower()
    if(movie!=movies):
        print("we dont have that movie in our theatre")
    seats=int(input("how many seats"))
    purchases.append(seats)
    purchases.append(movie)
    user=input("continue or done")
    
    
    


        
    
    
           

# TODO: use a while loop that continues until the user enters 'done'
# 1) ask for movie title (case sensitive is fine)
# 2) if title not in movies, print the available keys and continue
# 3) ask for quantity (int)
# 4) append (title, qty, movies[title]) to purchases
# 5) optional: track running subtotal
