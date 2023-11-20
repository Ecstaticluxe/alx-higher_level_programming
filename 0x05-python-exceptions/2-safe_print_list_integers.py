#!/usr/bin/python3
def safe_print_list_integers(my_list, x=0):
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            try:
                print("{:d}".format(value), end=" ")
                count += 1
            except (ValueError, TypeError):
                pass
    except IndexError as e:
        print("{:s}".format(e))
        import traceback
        traceback.print_exc()
    finally:
        print("nb_print:" count)
    return count
