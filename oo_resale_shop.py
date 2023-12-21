from computer import *
class ResaleShop:
    
    def __init__(self):
        self.inventory = ()
    # establish the inventory as an empty list
    # made sure to pass self into inventory


    def sell (self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, id: str, price: float, operating_system: str, year_made:int):
        computer = Computer(description, processor_type, hard_drive_capacity, memory, id, price, operating_system, year_made)
        if self.inventory == ():
            print ("Sorry! We are out of stock.")
        else:
            self.inventory.remove(computer)
    # Create a function that allows a customer to buy a computer
    #If there are no computers in the inventory, a statement will be printed to inform the customer of that
    #all of the information for each computer must be passed in

        
    def buy (self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, id: str, price: float, operating_system: str, year_made:int):
        computer = Computer(description, processor_type, hard_drive_capacity, memory, id, price, operating_system, year_made)
        self.inventory.append(computer)
    # Create a function that allows a customer to sell a computer to the store
    # all of the information for the computer is passed in

    def printInventory(inventory):
        if inventory:
        # For each item
            for item_id in inventory:
            # Print its details
                print(f'Item ID: {item_id} : {inventory[item_id]}')

    def call_refurbish (computer):
        refurbish = input("Do you want to refurbish this computer? (yes/no)")
        if refurbish.lower() == "yes":
            print ("Will refurbish.")
            refurbish(computer)
        elif refurbish.lower() == "no":
            print ("Will not refurbish.")
        else:
            print ("Please enter 'yes' or 'no'.")
    #if the customer wants to refurbish the computer they can say y/n
    # if they do want to refurbish the computer, it calls the function refurbish() from computer.py 