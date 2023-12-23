MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Returns 0 if the game was not valid.
# Otherwise, returns the game ID (a positive integer)
def isValid(game: str) -> int:
    split_colon = game.split(':')
    game_id = int(split_colon[0].split()[1]) # Game ID

    split_subsets = split_colon[1].strip().split(';')
    for subset in split_subsets:
        split_colours = subset.strip().split(',')
        num_red = 0
        num_green = 0
        num_blue = 0

        for c in split_colours:
            if 'red' in c:
                num_red = int(c.strip().split()[0])
            elif 'green' in c:
                num_green = int(c.strip().split()[0])
            elif 'blue' in c:
                num_blue = int(c.strip().split()[0])

        if num_red > MAX_RED or num_green > MAX_GREEN or num_blue > MAX_BLUE:
            return 0
        
    return game_id

def main():
    with open('input.txt', 'r') as games:
        sum = 0
        for g in games:
            sum += isValid(g)
        print(sum)

if __name__ == "__main__":
    main()
