import time

def main():

    with open('input.txt') as f:
        data = f.readlines()

    print("\n[+] Solving part one...")
    print(f"[*] Number found: {part_one(data)}")

    print("\n[+] Solving part two...")
    print(f"[*] Number found: {part_two(data)}\n")

    return

def part_one(data):
    for x in data:
        for y in data:
            x = int(x)
            y = int(y)

            if x+y == 2020: return x*y


def part_two(data):

    for x in data:
        for y in data:
            for z in data:
                x = int(x)
                y = int(y)
                z = int(z)

                if x+y+z == 2020: return x*y*z


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
