import time

def main():

    with open('input.txt') as f:
        data = f.readlines()
    c = 0
    bags = {}
    colors = []

    data = [e.strip() for e in data]

    for line in data:
        bags.update(rule_parser(line))

    print("\n[+] Solving part one...")

    for key in bags:
        out = check_bag(key, bags)
        if out: colors.append(out)

    print(f"[+] Number of bag colors found: {len(colors)}")



    return

def check_bag(key, dict):

    for bag in dict[key]:
        if bag == " other bag": return
        if bag == "shiny gold bag": return key
        if check_bag(bag, dict): return key


def rule_parser(data):
    data = data.replace('.', '').replace(' contain', ',').replace('bags', 'bag')
    data = data.split(',')

    return {data[0]:[e[3::] for e in data[1::]]}



if __name__ == '__main__':
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
