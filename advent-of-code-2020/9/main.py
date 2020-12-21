import time

def main():

    with open('input.txt') as f:
        data = f.readlines()

    data = [int(e.strip()) for e in data]

    print("\n[+] Solving part one...")

    invalid = find_invalid(data, 0, 25)

    print(f"[+] Invalid value found: {invalid}")
    print("\n[+] Solving part two...")

    for i in range(2,500):
        weakness = find_weakness(data, invalid, size=i)
        if weakness:
            print(f"[+] Weakness found: {weakness}\n")
            break

    return


def find_invalid(data, p_start, p_end):

    preamble = data[p_start:p_end]
    valid = False

    for x in preamble:
        for y in preamble:
            if x+y == data[p_end]:
                valid = True
                break

    if not valid: return data[p_end]
    else: return find_invalid(data, p_start+1, p_end+1)


def find_weakness(data, invalid, size=2):

    try:
        for start in range(0, len(data)-1):
            sum = 0
            for i in range(start, start+size):
                sum += data[i]

            if sum == invalid:
                sequence = [n for n in data[start:start+size]]
                return min(sequence)+max(sequence)

    except IndexError:
        pass

    return 0

if __name__ == '__main__':
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
