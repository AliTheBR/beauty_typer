import time


def type_beauty(text):
    for char in str(text):
        print(char, end='', flush=True)
        time.sleep(0.05)  # change it as you like


test_text = "Success is not the key to happiness; happiness is the key to success."

type_beauty(test_text)
