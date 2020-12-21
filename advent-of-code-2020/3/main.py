import time

def main():

    with open('input.txt') as f:
        data = f.readlines()

    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    mul = 1

    print("\n[+] Solving part one..")
    print(f"[+] Number of trees found: {count_trees(data, 3, 1)}")

    print("\n[+] Solving part two..")

    for slope in slopes:
        mul *= count_trees(data, slope[0], slope[1])

    print(f"[+] Number of trees calculated: {mul}\n")

    return

def count_trees(data, slope_x, slope_y):

    x,y,c = 0,0,0
    WIDTH, HEIGHT= len(data[0])-1, len(data)

    while y < HEIGHT-1:
        x += slope_x
        y += slope_y
        x %= WIDTH

        if data[y][x] == '#': c+=1

    return c


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
