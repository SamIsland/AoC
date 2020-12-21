import time

def main():

    with open('input.txt') as f:
        data = f.readlines()
    ids = []

    print("\n[+] Solving part one...")

    for ticket in data:
        seat = ticket_parser(ticket)
        ids.append(seat[0]*8+seat[1])

    print(f"[+] Highest seat ID found: {max(ids)}")
    print("\n[+] Solving part two...")

    for i in range(min(ids), max(ids)+1):
        if i not in ids:
            print(f"[+] Own seat ID found: {i}\n")

    return


def ticket_parser(ticket):

    ticket = ticket.strip()
    row = {'min': 0, 'max': 127}
    col = {'min': 0, 'max': 7}

    for c in ticket[0:7]:
        if c == "F": row['max'] = (row['min']+row['max'])//2
        if c == "B": row['min'] = (row['max']+row['min']+1)//2

    for c in ticket[7::]:
        if c == "L": col['max'] = (col['min']+col['max'])//2
        if c == "R": col['min'] = (col['max']+col['min']+1)//2

    return (row['min'],col['min'])


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
