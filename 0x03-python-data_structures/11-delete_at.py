#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if __name__ == "__main__":
        in not my_list or idx < 0 or idx >= len(my_list):
            return my_list

        new_l = []
        for i, item in enumerate(my_list):
            if i != idx:
                new_l.append(item)

        return new_l
