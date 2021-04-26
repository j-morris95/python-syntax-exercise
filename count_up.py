def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    step = 1
    if stop < start:
        step = -1
    for num in range(start, stop+step, step):
        print(num)


count_up(5, 7)
count_up(2, 20)
count_up(20, 2)
