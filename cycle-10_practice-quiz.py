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
            number += 1
                

    number = 0 
    for n in numbers_to_add:
        number += n

    return number

print(factorial(5))

# Question 3
def fib_nums(numb):

    number = 0
    add_numbers = 0

    num_table = [0]

    while number < numb:
        if number == 0:
            number += 1
            num_table.append(1)

        for numbers in num_table[-2:]:
            add_numbers += numbers
        # Check if it will reach the final numb
        if add_numbers == numb:
            return num_table 

        num_table.append(add_numbers)
        number += 1
        add_numbers = 0

print(fib_nums(5) == [0,1,1,2,3])
print(fib_nums(10) == [0,1,1,2,3,5,8,13,21,34])