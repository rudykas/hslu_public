def my_sum(a: list):
    """

    :type a: object
    """
    r = 0
    for x in a:
        r += x
    return r

print(my_sum((8, 2, 3, 0, 7)))

def main():
    print(my_sum((8, 2, 3, 100, 7)))


if __name__ == '__main__':
    main()

