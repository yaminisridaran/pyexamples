def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

if __name__ == "__main__":
    for char in rev_str("hello"):
        print char
