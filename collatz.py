past_numbers_dict = {}


def get_step(x):
    if x % 2 == 0:
        return x / 2
    return (x * 3) + 1


def get_path(entry):
    entries = [entry, ]
    while entries[-1] != 1:
        step = get_step(entries[-1])
        if step in past_numbers_dict.keys():
            entries = entries + past_numbers_dict[step]
        else:
            entries.append(step)
    return entries


x = 1
while x <= 10000:
    past_numbers_dict[x] = get_path(x)
    x += 1
for k,v in past_numbers_dict.items():
    print(f'{k}: {v}')
