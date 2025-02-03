import time


def type_beauty(text):
    for char in str(text):
        print(char, end='', flush=True)
        time.sleep(0.05)  # change it as you like


test_text = "Hello, World! 1.\nHello, World! 2"

type_beauty(test_text)
