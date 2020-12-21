import time
import re

def main():

	with open('input.txt') as f:
		data = f.readlines()

	c = 0
	passports = parse_passport(data)
	valid_passports = []

	print("\n[+] Solving part one...")

	for passport in passports:
		if verify(passport):
			valid_passports.append(passport)
			c+=1

	print(f"[+] Valid passports found: {c}")
	print("\n[+] Solving part two...")

	c = 0

	for passport in valid_passports:
		if strong_verify(passport):
			c+=1

	print(f"[+] Valid passports found: {c}\n")


def parse_passport(data):

	passports = []
	data = [e.strip() for e in data]
	out = ""

	for line in data:

		if line == data[-1]:
			passports.append(line)
			break

		if line: out += f"{line} "
		else:
			passports.append(out)
			out = ""

	return passports


def verify(passport):
	fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	for field in fields:
		if field not in passport:
			return False

	return True


def strong_verify(passport):

	for fields in passport.split():

		fields = fields.split(":")
		field, value = fields[0], fields[1]

		if field == "byr" and not (1920 <= int(value) <= 2002): return False
		if field == "iyr" and not (2010 <= int(value) <= 2020): return False
		if field == "eyr" and not (2020 <= int(value) <= 2030): return False
		if field == "hgt":
			if value[-2::] == "cm" and not (150 <= int(value[0:value.find("cm")]) <= 193): return False
			if value[-2::] == "in" and not (59 <= int(value[0:value.find("in")]) <= 76): return False
		if field == "hcl" and not bool(re.match("^#[0-9a-f]{6}$", value)): return False
		if field == "ecl" and not bool(re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", value)): return False
		if field == "pid" and not bool(re.match("^[0-9]{9}$", value)): return False

	return True


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"\n[*] Executed in {round((time.time()-start),3)}s\n")
