import time

def main():

    with open('input.txt') as f:
        data = f.readlines()

    print("\n[+] Solving part one...")
    print(f"[+] Number of compatible entries found: {part_one(data)}")

    print("\n[+] Solving part two...")
    print(f"[+] Number of compatible entries found: {part_two(data)}\n")

    return


def part_one(data):

    c = 0

    for r in data:
        r = r.split()

        min, max = int(r[0][0:r[0].find('-')]), int(r[0][r[0].find('-')+1::])
        char = r[1][0]
        passw = r[2]

        if min <= passw.count(char) <= max: c += 1

    return c


def part_two(data):

    c = 0

    for r in data:
        r = r.split()

        idx1, idx2 = int(r[0][0:r[0].find('-')]), int(r[0][r[0].find('-')+1::])
        char = r[1][0]
        passw = r[2]

        if (passw[idx1-1]==char) != (passw[idx2-1] == char):
            c+=1

    return c


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
