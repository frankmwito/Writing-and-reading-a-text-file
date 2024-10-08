# write first 100 prime numbers in a text file
import os


file_path = "prime_numbers.txt"

for i in range(100):
    if i > 1 and i % 1 == 0:
        if i % i == 0:
            print(i)
            with open(file_path, "w") as file:
                file.write(str(i) + "\n")
            print(f"prime number text {file_path} file was created")