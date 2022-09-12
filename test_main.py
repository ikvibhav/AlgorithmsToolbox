import random
import sys
import os

# Number of Tests
tests = int(sys.argv[1])

# Array Size Parameter
n = int(sys.argv[2])

for i in range(tests):
    print(f'Test #{i}')
    os.system(f'python3 test_generator_seed.py {n} {i} > input_{i}.txt')

    # Run the model to be tested
    #os.system(f'python3 model.py < input_{i}.txt > model_output_{i}.txt')

    # Run the main solution
    #os.system(f'python3 main.py < input_{i}.txt > main_output_{i}.txt')

    # Read output of main and model solutions and compare
    with open('model_output_{i}.txt') as f:
        model = f.read()
    print("model:", model)

    with open('main_output_{i}.txt') as f:
        main = f.read()
    print("main:", main)

    if model != main:
        break