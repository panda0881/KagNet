with open('conceptnet-assertions-5.6.0.csv.en', 'r') as f:
    for line in f:
        words = line.split('\t')
        tmp_r = words[0]
        tmp_head = words[1]
        tmp_tail = words[2]
        print(line)
        break
print('end')
