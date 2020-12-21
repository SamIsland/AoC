import time

def main():

    with open('input.txt') as f:
        data = f.readlines()

    data = [e.strip() for e in data]
    groups = []
    out = ""
    c = 0

    for line in data:
        if line: out += f" {line}"
        else:
            groups.append(out)
            out = ""

    groups.append(out)

    print("\n[+] Solving part one...")

    for group in groups:
        c += count_answer(group)

    print(f"[+] Number of answers found: {c}")
    print("\n[+] Solving part two...")

    c=0
    for group in groups:
        c += count_common(group)

    print(f"[+] Number of common answers found: {c}\n")

    return


def count_answer(group):
    counted = []
    for ans in group:
        if ans != " " and ans not in counted:
            counted.append(ans)

    return len(counted)


def count_common(group):
    group = group.split()
    c, common = 0,1

    if len(group) == 1: return len(group[0])

    for ans in group[0]:
        common = 1
        for chr in group[1::]:
            if ans in chr:
                common += 1

        if common == len(group): c +=1

    return c


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
