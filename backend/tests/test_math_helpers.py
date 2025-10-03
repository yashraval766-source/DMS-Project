# test_helpers.py
from helpers.math_helpers import *
from helpers.file_helpers import *
from helpers.security_helpers import hash_password

def test_math():
    print("===== Math Helper Functions Test =====")
    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))
    print("Factorial of 5:", factorial(5))
    print("Square root of 16:", square_root(16))
    print("2^3 =", power(2, 3))
    print("Absolute value of -10:", absolute(-10))
    print("Sine 30°:", sine(30))
    print("Cosine 60°:", cosine(60))
    print("Tangent 45°:", tangent(45))
    print("Random integer between 1 and 10:", random_int(1, 10))
    print("Average of [1,2,3]:", average([1,2,3]))
    print("Is 17 prime?:", is_prime(17))
    print()

def test_file_and_security():
    print("===== File Helper Functions Test =====")
    fname = "test_file.txt"
    create_file(fname, "Hello World!\n")
    print("File content after create:")
    print(read_file(fname))
    append_file(fname, "Ye ek aur line add ho gayi!\n")
    print("File content after append:")
    print(read_file(fname))
    write_file(fname, "Ye purana content replace kar diya.\n")
    print("File content after write:")
    print(read_file(fname))
    delete_file(fname)
    print("File content after delete (should give message):")
    print(read_file(fname))
    print()
    print("===== Security Test =====")
    print("Hashed 'secret':", hash_password("secret"))

if __name__ == "__main__":
    test_math()
    test_file_and_security()

