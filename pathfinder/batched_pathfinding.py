import sys
import json
import random

path_csqa_train = "../datasets/csqa_new/train_rand_split.jsonl.statements"
path_csqa_dev = "../datasets/csqa_new/dev_rand_split.jsonl.statements"
path_csqa_test = "../datasets/csqa_new/test_rand_split.jsonl.statements" # rename test file first

PATH = path_csqa_train  # switch mannually
NUM_BATCHES = 100

def generate_bash():
    PATH = sys.argv[2]
    with open("cmd_1.sh", 'w') as f:
        for i in range(0,20):
            f.write("CUDA_VISIBLE_DEVICES=NONE python pathfinder.py %s %d &\n" % (PATH, i))
        f.write('wait')
    with open("cmd_2.sh", 'w') as f:
        for i in range(20,40):
            f.write("CUDA_VISIBLE_DEVICES=NONE python pathfinder.py %s %d &\n" % (PATH, i))
        f.write('wait')
    with open("cmd_3.sh", 'w') as f:
        for i in range(40,60):
            f.write("CUDA_VISIBLE_DEVICES=NONE python pathfinder.py %s %d &\n" % (PATH, i))
        f.write('wait')

    with open("cmd_4.sh", 'w') as f:
        for i in range(60,80):
            f.write("CUDA_VISIBLE_DEVICES=NONE python pathfinder.py %s %d &\n" % (PATH, i))
        f.write('wait')

    with open("cmd_5.sh", 'w') as f:
        for i in range(80,100):
            f.write("CUDA_VISIBLE_DEVICES=NONE python pathfinder.py %s %d &\n" % (PATH, i))
        f.write('wait')

def combine():
    final_json = []
    PATH = sys.argv[2]
    for i in range(NUM_BATCHES):
        with open(PATH + ".%d.pf"%i) as fp:
            tmp_list = json.load(fp)
        final_json += tmp_list

    with open(PATH + ".pf", 'w') as fp:
        json.dump(final_json, fp) # js beautify is too time-consuming now

if __name__ == '__main__':
    import sys
    globals()[sys.argv[1]]()
