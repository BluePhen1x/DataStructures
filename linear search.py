def locate_cards(cards, query):
    position = 0

    while True:
        if cards[position]== query:
            return position
        
        position+= 1

        if position == len(cards):
            return -1

def main():
    length = int(input("Length of cards: "))
    cards = []
    while length>0:
        x = input("Number: ")
        cards.append(x)
        length -= 1
    query = input("Whats the number required to be found? ")
    position = locate_cards(cards, query)
    print(position+1) # The +1 is so that the user can get the correct position
main()