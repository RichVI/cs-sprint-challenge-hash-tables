def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    # Storage all intergers in the cache
    for i in a:
        # print("I", i)
        if i not in cache:
            cache[i] = i

    # Look for the counter part of the integer
    for j in cache:
        if cache[j] < 0 and -cache[j] in cache:
            print(-cache[j])
            result.append(abs(cache[j]))
    return result

# cache {
#     -1: -1,
#     -2: -2,
#      1: 1,
#      2: 2,
#      3: 3,
#      4: 4,
#      -4: -4 
# }




if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
