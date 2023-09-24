class Computer:

 
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, id: str, price: float, operating_system: str, year_made:int):
        self.id = id
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.price = price
        self.operating_system = operating_system
        self.year_made = year_made
    # This is the constructor that creates the computer and passes self into all of the different attributes of the computer

    def refurbish (self, year_made: int, new_operating_system: str, operating_system: str, price: float):
        self.price = price
        self.operating_system = operating_system
        self.new_operating_system = new_operating_system
        if year_made < 2000:
            price = 0
            print ("Unfortunately, we cannot sell this computer")
        elif year_made <2012:
            price = 250
            print ("The updated price of this computer is $250.")
        elif year_made < 2018:
            price = 500
            print ("The updated price of this computer is $500.")
        else:
            price = 1000
            print ("The updated price of this computer is $1000.")
        operating_system = new_operating_system
    # This method is responsible for refurbishing the computer when it is called to do so in oo_resale_shop
    #depending on the year made, the computer's price is changed
    # the operating system takes of the str value of the new operating system
