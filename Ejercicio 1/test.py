from ejercicio1 import es_palindromo
import sys
import os

def run_test(test_func, output_file):
    result = None
    try:
        result = test_func()
        test_result = f"Test passed: {result}"
    except AssertionError as e:
        test_result = f"AssertionError: {str(e)}"
    with open(output_file, 'w') as f:
        f.write(test_result)

def test_palindromo_1():
    return es_palindromo("radar")

def test_palindromo_2():
    return es_palindromo("melisa")

def test_palindromo_3(): 
    return es_palindromo("ana")

def test_palindromo_4(): 
    return es_palindromo("versatil")

def test_palindromo_5(): 
    return es_palindromo("lol")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(script_dir, "output")
    os.makedirs(output_path, exist_ok=True)

    run_test(test_palindromo_1, os.path.join(output_path, "test_palindromo1.txt"))
    run_test(test_palindromo_2, os.path.join(output_path, "test_palindromo2.txt"))
    run_test(test_palindromo_3, os.path.join(output_path, "test_palindromo3.txt"))
    run_test(test_palindromo_4, os.path.join(output_path, "test_palindromo4.txt"))
    run_test(test_palindromo_5, os.path.join(output_path, "test_palindromo5.txt"))
