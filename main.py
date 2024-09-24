def recursive_sum(recursive, sum=0, recursions = 1, total_items = 0, depth = 0, max_depth = 0):
    if depth > max_depth:
        max_depth = depth
    for item in recursive:
        if type(item) == int:
            sum += item
            total_items += 1
        elif type(item) == list:
            recursions = recursions  + 1
            total_items += 1
            diving = recursive_sum(item, sum, recursions, total_items, depth+1, max_depth)
            sum = diving[0]
            recursions = diving[1]
            total_items = diving[2]
            max_depth = diving[4]
        else: #EXTRA CREDIT 
            total_items += 1
            print(type(item), " is in your list. It was skipped")
    return [sum, recursions, total_items, depth, max_depth]
def main():
    nested_list = [1, [2, 3], [[4], [5, [6, 7]]], 8] # Expected output: # (36, 6, 13, 0, 3)
    print(recursive_sum(nested_list))
    test_2 = [[[3, [4]], 6], 7, [10, True, 3], [4, [5, [2, 8]]], 8, "This will be skiped"] # Expected output: # (60, 8, 20, 0, 3])
    print(recursive_sum(test_2))

if __name__ == "__main__":
    main()