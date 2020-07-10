#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    # create cache
    cache = {}
    storage = [None] * length

    # loop thru our tickets
    for i in tickets:

        # if our ticket source is none
        if i.source == "NONE":

            #then we assign storage [0]
            storage[0] = i.destination
        cache[i.source] = i.destination

    # loop thru range starting at 1 and end at given length
    for x in range(1, length):
        storage[x] = cache[storage[x - 1]]

    return storage


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# Storage = ["NONE", "NONE", "NONE"]
# Storage["PDX", "NONE", "NONE"]

# cache {
#   None: PDX
#   PDX: DCA
#   DCA: NONE
# }

# Storage[1] = DCA
# Storage["PDX", "DCA", "NONE"]
