# Created by : Sidney Kang
# Created on : 11 Nov. 2017
# Created for : ICS3UR
# Daily Assignment - Unit5-01
# This program generates 10 random numbers and calculates the average

import ui
from numpy import random
import time

my_numbers = []
    
def show_average_touch_up_inside(sender):   
	 
    calculate_average(my_numbers)
    
    print_average = str(calculate_average(my_numbers))
    view['average_label'].text = "The average is: " + print_average

def calculate_average(my_numbers): 
    total = 0

    for number, value in enumerate(my_numbers, 0):      
        total = total + value
        number = number + 1
                  
    average = float(total / 10)     
    return average    
	
view = ui.load_view()
view.present('sheet') 

def create_10_random_numbers():
    for random_number in range(10):
        random_number = random.randint(1,100)
        my_numbers.append(random_number)   
        time.sleep(0.08)      
        view['average_textview'].text = str(my_numbers)

create_10_random_numbers()

