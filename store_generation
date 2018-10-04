def search (product_names, product_costs, quantity):
    """searches for the desired product name to see if it's within the list"""
    product_names1 = product_names
    product_costs1 = product_costs
    quantity1 = quantity

    product = input("Enter a product name: ")

    if product in product_names1:
        place = product_names1.index(product)
        cost = product_costs1[place]
        product_q = quantity1[place]
        
        print("We sell"+" '"+ product+"'"+ " at "+ str(cost)+ " per unit" )
        print("We currently have", product_q, "in stock")
        print()

    else:
        print("Sorry, we don't sell"+" '"+product+"'")
        print()


def inventory(product_names, product_costs, quantity):
    """Prints out everything we have on hand"""
    product_names1 = product_names
    product_costs1 = product_costs
    quantity1 = quantity

    print(format("Product", "<15s"), format("Price", "<10s"), format("Quantity", "<10s"))
    
    for line in zip(product_names1, product_costs1, quantity1):
        print("{:10}{:10}{:10}".format(*line))
    print()

def add(product_names, product_costs, quantity):
    """adds whatever product the use wishes to input"""
    product_names1 = product_names
    product_costs1 = product_costs
    quantity1 = quantity  

    name= input("Enter a new product name: ")
    while name in product_names1:
        print("Sorry, we already sell that product. Try again")
        name= input("Enter a new product name: ")
    product_names1.append(name)
    cost = input("Enter a product cost: ")
    while float(cost) <= float(0):
            print("Invalid cost!")
            new_name = input("Enter a new cost: ")
    product_costs1.append(float(cost))
    q = input("How many of these products do we have: ")
    while int(q) <= int(0):
            print("Invalid quantity!")
            q = input("Enter a new quantity: ")
    quantity1.append(int(q))
    print("Product added!")
    print()


def remove(product_names, product_costs, quantity):
    product_names1 = product_names
    product_costs1 = product_costs
    quantity1 = quantity
    """removes whatever product the user wants to remove"""
    prompt= input("Enter a product name: ")

    if prompt not in product_names1:
        print("Product doesn't exist. Can't remove")
        print()

    elif prompt in product_names1:
        place = product_names1.index(prompt)
        cost = product_costs1[place]
        product_q = quantity1[place]

        product_names1.remove(prompt)
        product_costs1.remove(cost)
        quantity.remove(product_q)
        print("Product removed!")
        print()
    

def update(product_names, product_costs, quantity):
    product_names1 = product_names
    product_costs1 = product_costs
    quantity1 = quantity
    prompt= input("Enter a product name: ")
    """updates whatever product user desires"""
    if prompt not in product_names1:
        print("Product doesn't exist. Can't update")
        print()

    elif prompt in product_names:
        print("What would you like to update?")
        prompt2 = input("(n)ame, (c)ost or (q)uantity: ")

        if prompt2 == "n":
            new_name = input("Enter a new name: ")
            while new_name in product_names1:
                print("Duplicate name!")
                new_name = input("Enter a new name: ")
            place = product_names1.index(prompt)
            product_names1.remove(prompt)
            product_names1.insert(place, new_name)
            print("Product name has been updated.")
            print()
                
        elif prompt2 =="c":
            new_cost = float(input("Enter a new cost: "))
            while new_cost <= float(0):
                print("Invalid cost!")
                new_name = input("Enter a new cost: ")
            place = product_names1.index(prompt)
            cost = product_costs1[place]
            product_costs1.remove(cost)
            product_costs.insert(place, float(new_cost))
            print("Product cost has been updated.")
            print()

        elif prompt2 == "q":
            
            new_q = input("Enter a new quantity: ")
            while int(new_q) <= int(0):
                print("Invalid quantity!")
                new_q = input("Enter a new quantity: ")

            place = product_names1.index(prompt)
            q = quantity1[place]
            quantity1.remove(q)
            quantity1.insert(place, int(new_q))
            print("Product quantity has been updated.")
            print()
        else:
            print("Invalid option")
            print()

 

def report(product_names, product_costs, quantity):

    """reports max, min, total value of our products"""
    product_names1 = product_names
    product_costs1 = product_costs
    quantity1 = quantity

    max_cost = max(product_costs1)
    min_cost = min(product_costs1)

    place1 = product_costs1.index(max_cost)
    place2 = product_costs1.index(min_cost)

    name1 = product_names1[place1]
    name2 = product_names1[place2]

    multiplied = [i * j for i, j in zip(product_costs1, quantity1)]
    total = sum(multiplied)           

    print("Most expensive product:" + str(max_cost)+ "(" + name1 + ")")
    print("Least expensive product:" + str(min_cost)+ "(" + name2 + ")")
    print("Total value of all products:", total)
    print()
  
def main():

    product_names = ["burrito", "cronut", "chow mein"]
    product_costs= [5.29, 4.29, 7.29]
    quantity = [10, 5, 20]
                     
    while True:
        option = input("(s)earch for product, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
        print()

        if option == "s":
            result = search(product_names, product_costs, quantity)
          
        elif option =="l":

            inventory(product_names, product_costs, quantity)

        elif option =="a":
            updated_list = add (product_names, product_costs, quantity)
            
        elif option =="r":
            updated_list = remove (product_names, product_costs, quantity)

        elif option =="u":
            updated_list = update (product_names, product_costs, quantity)
        elif option =="e":
            updated_list = report (product_names, product_costs, quantity)

        elif option =="q":
            print("See you soon!")
            break

        else:
            print("Invalid option, try again.")


main()
