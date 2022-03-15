import os
import pandas as pd

dirpath_train_pos = './aclImdb/train/pos'
dirpath_train_neg = './aclImdb/train/neg'
dirpath_test_pos = './aclImdb/test/pos'
dirpath_test_neg = './aclImdb/test/neg'
output_train = './train.csv'
output_test = './test.csv'
col_names = ['review', 'label']
train = pd.DataFrame()
test = pd.DataFrame()
train_review_pos = []
train_review_pos_rating = []
train_review_neg = []
train_review_neg_rating = []
test_review_pos = []
test_review_pos_rating = []
test_review_neg = []
test_review_neg_rating = []
files_train_pos = [os.path.join(dirpath_train_pos, fname) for fname in os.listdir(dirpath_train_pos)]
files_train_neg = [os.path.join(dirpath_train_neg, fname) for fname in os.listdir(dirpath_train_neg)]
files_test_pos = [os.path.join(dirpath_test_pos, fname) for fname in os.listdir(dirpath_test_pos)]
files_test_neg = [os.path.join(dirpath_test_neg, fname) for fname in os.listdir(dirpath_test_neg)]

def get_rating(filename): 
    rating = ""
    flag = False
    for c in filename:
        if flag:
            rating = rating + c
        if c == '_':
            flag = True
        elif c == '.':
            flag = False
    return int(rating[:-1])
for filename in sorted(files_train_pos):
    file = open(filename, 'r')
    review = file.read()
    train_review_pos.append(review)
    train_review_pos_rating.append(get_rating(filename))
    file.close()

for filename in sorted(files_train_neg):
    file = open(filename, 'r')
    review = file.read()
    train_review_neg.append(review)
    train_review_neg_rating.append(get_rating(filename))
    file.close()

train['review'] = train_review_pos + train_review_neg
train['label'] = [1]*len(train_review_pos) + [0]*len(train_review_neg)
train['rating'] = train_review_pos_rating + train_review_neg_rating

for filename in sorted(files_test_pos):
    file = open(filename, 'r')
    review = file.read()
    test_review_pos.append(review)
    test_review_pos_rating.append(get_rating(filename))
    file.close()

for filename in sorted(files_test_neg):
    file = open(filename, 'r')
    review = file.read()
    test_review_neg.append(review)
    test_review_neg_rating.append(get_rating(filename))
    file.close()

test['review'] = test_review_pos + test_review_neg
test['label'] = [1]*len(test_review_pos) + [0]*len(test_review_neg)
test['rating'] = test_review_pos_rating + test_review_neg_rating

train.to_csv(output_train)
test.to_csv(output_test)
