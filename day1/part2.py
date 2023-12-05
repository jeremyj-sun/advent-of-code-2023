line_num = 1
DEBUG = False

def calibration_value(line: str):
    global line_num
    l_digit = ''
    r_digit = ''

    for i in range(len(line)):
        if line[i].isdigit():
            l_digit = line[i]
            break
        elif line[i] == 'o' and line[i:i+3] == 'one':
            l_digit = '1'
            break
        elif line[i] == 't':
            if line[i:i+3] == 'two':
                l_digit = '2'
                break
            elif line[i:i+5] == 'three':
                l_digit = '3'
                break
        elif line[i] == 'f':
            if line[i:i+4] == 'four':
                l_digit = '4'
                break
            elif line[i:i+4] == 'five':
                l_digit = '5'
                break
        elif line[i] == 's':
            if line[i:i+3] == 'six':
                l_digit = '6'
                break
            elif line[i:i+5] == 'seven':
                l_digit = '7'
                break
        elif line[i] == 'e' and line[i:i+5] == 'eight':
            l_digit = '8'
            break
        elif line[i] == 'n' and line[i:i+4] == 'nine':
            l_digit = '9'
            break

    r_line: str = line[::-1]
    if DEBUG:
        print(f"reversed line: {r_line}")
    for j in range(len(r_line)):
        if r_line[j].isdigit():
            r_digit = r_line[j]
            break
        elif r_line[j] == 'e':
            if r_line[j:j+3] == 'one'[::-1]:
                r_digit = '1'
                break
            elif r_line[j:j+4] == 'five'[::-1]:
                r_digit = '5'
                break
            elif r_line[j:j+4] == 'nine'[::-1]:
                r_digit = '9'
                break
            elif r_line[j:j+5] == 'three'[::-1]:
                r_digit = '3'
                break
        elif r_line[j] == 'o' and r_line[j:j+3] == 'two'[::-1]:
            r_digit = '2'
            break
        elif r_line[j] == 'r' and r_line[j:j+4] == 'four'[::-1]:
            r_digit = '4'
            break
        elif r_line[j] == 'x' and r_line[j:j+3] == 'six'[::-1]:
            r_digit = '6'
            break
        elif r_line[j] == 'n' and r_line[j:j+5] == 'seven'[::-1]:
            r_digit = '7'
            break
        elif r_line[j] == 't' and r_line[j:j+5] == 'eight'[::-1]:
            r_digit = '8'
            break

    retval = int(str(l_digit) + str(r_digit))
    if DEBUG:       
        print(f"Line {line_num}: {retval}")
    line_num += 1
    return retval

def main():
    with open('input.txt', 'r') as file:
        sum = 0
        for line in file:
            sum += calibration_value(line)
        print(sum)

if __name__ == "__main__":
    main()
