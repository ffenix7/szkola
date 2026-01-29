import bisect

lines = []
num_of_lines = int(input())

for i in range(num_of_lines):
    line = input()
    lines.append(line)

rank = []
out = []
i = 0

while i < len(lines):
    token = lines[i]
    if token == '^':
        if rank:
            rank.pop(0)
        i += 1
    elif token == '?':
        if len(rank) >= 3:
            out.append(rank[2][1])
        else:
            out.append('')
        i += 1
    else:
        name = token.split()[0]
        if len(token.split()) == 2:
            salary = int(token.split()[1])
            bisect.insort(rank, (-salary, name))
            i += 1
        else:
            if i+1 < len(lines):
                salary = int(lines[i+1])
                bisect.insort(rank, (-salary, name))
            i += 2

print('\n'.join(out))
