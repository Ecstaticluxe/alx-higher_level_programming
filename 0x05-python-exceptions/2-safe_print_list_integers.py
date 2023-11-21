#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    
    count = 0
    i = 0
    
    try:
        while count < x:
            value = my_list[i]
            try:
                print("{:d}".format(value), end=" ")
                count += 1
            except (ValueError, TypeError):
                pass
            i += 1
    except IndexError:
        pass

    finally:
        print()
    return (count)
