def array_test():
    ar = [1,4,25,543,74,86,3,2,6,7,8]
    print(ar, "is initial array.")

    ar.pop() # move one from the end
    print(ar)

    ar.append(3) # increase from the end
    print(ar)
    print("Index of 4: ", ar.index(4)) # index of given value

    ar.remove(4) # remove the first occurence of item with given value
    print("Remove 4: ", ar)

    ar.reverse() # reverse array
    print("reverse: ", ar)
    print("sorted return: ", sorted(ar)) # list array from mix to max

    ar.sort()
    print("sorted in place: ", ar)

def main():
    array_test()


if __name__ == '__main__' :
    main()
