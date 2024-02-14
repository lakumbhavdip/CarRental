# Write a Python Program to print random number without using Rand ().

import time

def print_random_number():
  ran_num = time.time()
  return ran_num

random_number = print_random_number()
print(random_number)