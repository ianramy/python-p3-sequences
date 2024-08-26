#!/usr/bin/env python3

def print_fibonacci(length):
    # print empty list and zero if length is 0/1
    if length <= 0:
        print([])
        return
    
    if length == 1:
        print([0])
        return

    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate Fibonacci numbers until the sequence has the desired length
    while len(fib_sequence) < length:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    # Print the sequence, each number on a new line
    print(fib_sequence)
