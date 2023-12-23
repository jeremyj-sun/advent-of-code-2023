from typing import Dict

# Returns the minimum number of red, green, and blue cubes needed to play the game.
def min_set(game: str) -> Dict[str, int]:
    subsets = game.split(':')[1].strip().split(';')
    max_red = 0
    max_green = 0
    max_blue = 0
    for s in subsets:
        colours = s.strip().split(',')
        num_red = 0
        num_green = 0
        num_blue = 0
        for c in colours:
            if 'red' in c:
                num_red = int(c.strip().split()[0])
                max_red = max(num_red, max_red)
            elif 'green' in c:
                num_green = int(c.strip().split()[0])
                max_green = max(num_green, max_green)
            elif 'blue' in c:
                num_blue = int(c.strip().split()[0])
                max_blue = max(num_blue, max_blue)
    return {'red': max_red, 'green': max_green, 'blue': max_blue}

def power_set(set: Dict[str, int]) -> int:
    return set['red'] * set['green'] * set['blue']

def main():
    with open('input.txt', 'r') as games:
        sum = 0
        for g in games:
            sum += power_set(min_set(g))
        print(sum)

if __name__ == "__main__":
    main()
