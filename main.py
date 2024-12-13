d1 = {'id1': 101, 'id2': 102, 'id3': 102, 'id4': 102}

counter = 0

for c in d1.values():
    if c == 102:
        counter +=1

print("102 is repeated: ", counter, 'times')