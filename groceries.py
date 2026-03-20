from collections import Counter
import requests
import random

# https://www.mit.edu/~ecprice/wordlist.10000 list of 10000 words.
def word_lib():
    source = "https://raw.githubusercontent.com/pi-co/List-of-all-Foods/refs/heads/master/FOOD.txt"
    result = requests.get(source)
    
    words = result.text.splitlines()
    return words

def is_edible(item, edible_items):
    if item in edible_items:
        return True
    
    if item.endswith('s') and item[:-1] in edible_items:
        return True
    
    if not item.endswith('s') and (item + 's') in edible_items:
        return True
    return False

def groceries(itinerary, item, quantity, edible_items):
    if not is_edible(item, edible_items):
        print("Please enter something that is edible.")
        return

    if quantity > 1:
        itinerary.extend([item] * quantity)
        print(f"Added {quantity} {item}(s) to the list.")
    elif quantity == 1:
        itinerary.append(item)
        print(f"Added {quantity} {item} to the list.")
    else:
        print("I guess you changed your mind.")

def skimp(itinerary, item, quantity):
    if item in itinerary and quantity == 1:
        itinerary.remove(item)
        print(f"Removed {item} from the list.")
    elif item in itinerary and quantity > 1:
        count = 0
        for _ in range(quantity):
            try:
                itinerary.remove(item)
                count +=1
            except ValueError:
                break
    else:
        print("I guess you changed your mind.")

def the_list(itinerary):
    print("\nGrocery List:")
    for k, v in Counter(itinerary).items():
        if v > 1:
            print(f"{k}: {v}")
        else:
            print(f"{k}")
# can also be formatted as print(f"{k({v})}" if v > 1 else str(k) for k, v in Counter(a).items())

def shopping():
    edible_items = word_lib()
    itinerary = random.sample(edible_items, 10)

    while True:
        the_list(itinerary)

        x = input("Do you want to 'add', 'remove' or do 'nothing'? ")
        if x == 'add':
            item = input("Add a food item to the list: ").casefold().strip()
            quantity = int(input("How many of said item do you want to add? "))
            groceries(itinerary, item, quantity, edible_items)
        elif x == 'remove':
            item = input("Remove a food item from the list: ").casefold()
            quantity = int(input("How many of said item do you want to remove? "))
            skimp(itinerary, item, quantity)
        elif x == 'nothing':
            print("Final grocery list:")
            the_list(itinerary)
            break
        else:
            print("I don't understand what you're saying.")
            continue
shopping()





