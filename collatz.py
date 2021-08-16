past_numbers_dict = {}


def get_step(x):
    if x % 2 == 0:
        return int(x / 2)
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


def update_past_numbers_dict(x, path):
    past_numbers_dict[x] = path
    for index, number in enumerate(path):
        if number not in past_numbers_dict.keys():
            past_numbers_dict[number] = path[index:]


x = 1
while x <= 100:
    path = get_path(x)
    update_past_numbers_dict(x, path)
    x += 1

for key in sorted(past_numbers_dict.keys()):
    print(f'{key}: {past_numbers_dict[key]}')

print(f'Total entries: {len(past_numbers_dict.keys())}')
