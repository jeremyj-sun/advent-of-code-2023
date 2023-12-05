def calibration_value(line: str):
    l_digit = ''
    r_digit = ''
    for c in line:
        if c.isdigit():
            l_digit = c
            break
    for c in reversed(line):
        if c.isdigit():
            r_digit = c
            break
    return int(str(l_digit) + str(r_digit))

def main():
    with open('input.txt', 'r') as file:
        sum = 0
        for line in file:
            sum += calibration_value(line)
        print(sum)

if __name__ == "__main__":
    main()
