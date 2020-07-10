def get_indices_of_item_weights(weights, length, limit):
    # creat a cache
    cache = {}

    # loop through the len of weights list to extract each index value
    for i in range(len(weights)):

        # create a current variable to track weight index value
        current = weights[i]

        # if the weight index value is already in the cache...
        if current in cache:
            # then store that index in a variable that is to be returned as a tuple
            needed_weight = cache[current]

            # returning tuple using the found indecies
            return (i, needed_weight)

        # store info about this current weight
        # key: other weight needed to add up to the limit
        # value: the current weight's index
        cache[limit - current] = i
        
    # return none if we can not merge packages
    return None

    # l1 = [4, 6, 10, 15, 16]
    # Limit 21

    # cache
    #     17 = 0
    #     15 = 1
    #     11 = 2

    # found
    #     needed_weight = 1
    # return 
    #     (3, 1)
