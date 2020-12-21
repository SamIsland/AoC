import time

def main():

    with open('input.txt') as f:
        data = f.readlines()

    data = [e.strip() for e in data]
    program = []
    err_index = []

    for i in range(len(data)):
        line = data[i].split()
        program.append({line[0]:int(line[1])})


    print("\n[+] Solving part one...")
    print(f"[+] Value of accumulator found: {_exec(program)[1]}")

    print("\n[+] Solving part two...")

    for i in range(len(program)):
        for key, value in program[i].items():
            if key == "nop" or key == "jmp":
                err_index.append(i)



    for n in err_index:
        fixed = [e for e in program]

        for key, value in fixed[n].items():

            if key == "jmp": fixed[n] = {"nop":value}
            else: fixed[n] = {"jmp":value}

            exit_code = _exec(fixed)

            if exit_code[0] == "END_OF_STREAM":
                print(f"[+] Value of accumulator found: {exit_code[1]}\n")

    return


def _exec(program, pc=0, acc=0, executed=[]):

    if pc == len(program):
        executed.clear()
        return ("END_OF_STREAM", acc)

    for key, value in program[pc].items():
        opcode = key
        operator = value

    if pc in executed:
        executed.clear()
        return ("LOOPED", acc)

    executed.append(pc)

    if opcode == "jmp":
        if operator != 0:
            pc += operator
        else:
            return ("SI_LOOP", acc)
    elif opcode == "acc":
        acc += operator
        pc += 1
    else:
        pc += 1

    return _exec(program, pc, acc)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
