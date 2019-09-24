from tqdm import tqdm


all_concepts = list()
all_relations = list()
with open('conceptnet-assertions-5.6.0.csv.en', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split('\t')
        tmp_r = words[0]
        tmp_head = words[1]
        tmp_tail = words[2]
        all_concepts.append(tmp_head)
        all_concepts.append(tmp_tail)
        all_relations.append(tmp_r)

all_concepts = list(set(all_concepts))
all_relations = list(set(all_relations))

with open('concept.txt', 'w', encoding='utf-8') as f:
    for w in tqdm(all_concepts):
        f.write(w)
        f.write('\n')

with open('relation.txt', 'w', encoding='utf-8') as f:
    for w in tqdm(all_relations):
        f.write(w)
        f.write('\n')


print('end')
