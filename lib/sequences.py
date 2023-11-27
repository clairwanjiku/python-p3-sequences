#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    
    fibonacci_sequence = [0]
    a, b = 0, 1
    for _ in range(length - 1):
        fibonacci_sequence.append(b)
        a, b = b, a + b
    
    print(fibonacci_sequence)
