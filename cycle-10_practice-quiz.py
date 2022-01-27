# Ryan Lugo: RJL 1/27/22

# Question 1
def food_costs(groceries,costs):
    grocerie_mod = groceries
    i = 0 # Counter for costs list 

    for index,grocerie in enumerate(grocerie_mod): # Using enumerate to later use the indexing var to edit the list specific list
        for ind,v in enumerate(grocerie): # again using the enumerate to use for editing the list
            grocerie_mod[index][ind] = v+": "+"$"+str(costs[i]) # Editing the specific list inside the lists to the vale
            i += 1 # Adding for the cost list counter
    
    return grocerie_mod

print(food_costs([['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt',]],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == 
[['apple: $1.99','pear: $2.99','banana: $0.99',],['salmon: $9.99','tuna: $10.99','cod: $6.99',],['milk: $3.49','eggs: $2.49','yogurt: $1.49',]])

# Quesiton 2
def factorial(numb):
    number  = 0
    numbers_to_add = []

    while number < numb:
            if number %2 == 0:
                numbers_to_add.append(number)
                
            number = 0 
            for n in numbers_to_add:
                number += n
            break
    return number

print(factorial(5))