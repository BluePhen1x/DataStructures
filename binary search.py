def locate_card(cards, query):
    lo , hi = 0, len(cards) -1
    
    while lo <= hi:
        mid =( lo + hi) // 2 
        result = location(cards, query,mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid-1
        elif result == "right":
            lo = mid +1
    return -1

def location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif cards[mid] < query:
        return "left"
    else:
        return "right"



def main():
    length = int(input("Length of cards: "))
    cards = []
    while length>0:
        x = input("Number: ")
        cards.append(x)
        length -= 1
    query = input("Whats the number required to be found? ")
    position = locate_card(cards, query)
    print(position) # The +1 is so that the user can get the correct position
main()