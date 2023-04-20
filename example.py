with open('/home/evgvac/Git/test-1.txt', 'r') as file1:
    with open('/home/evgvac/Git/test-2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('/home/evgvac/Git/test-out.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)