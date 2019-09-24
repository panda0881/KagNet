from tqdm import tqdm


all_words = list()
with open('conceptnet-assertions-5.6.0.csv.en', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split('\t')
        tmp_r = words[0]
        tmp_head = words[1]
        tmp_tail = words[2]
        for w in tmp_head.split(' '):
            all_words.append(w)
        for w in tmp_tail.split(' '):
            all_words.append(w)

all_words = list(set(all_words))

with open('concept.txt', 'w', encoding='utf-8') as f:
    for w in tqdm(all_words):
        f.write(w)
        f.write('\n')

print('end')
