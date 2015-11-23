from __future__ import print_function
import codecs

def load_file(filename, sep):
    instances = []
    for line in codecs.open(filename, 'r', 'utf8'):
        line = line.strip()
        if not line:
            continue
        components = line.split(sep)
        instances.append(tuple(components))
    instances = tuple(instances)
    # sanity check:
    if not instances:
        raise IOError('Empty file?')
    # assume first line has correct numbers of items:
    correct_nb = len(instances[0])
    for idx, instance in enumerate(instances):
        if len(instance) != correct_nb:
            raise IOError('Unequal nb of instances in line:', idx)
    return instances


# Ex. 2:
def print_stats(instances, class_idx = -1):
    print("::: Data statistics :::")
    print('\t>>> Nb items:', len(instances))
    print('\t>>> Nb features:', len(instances[0][:-1]))
    class_labels = [instance[class_idx] for instance in instances]
    sorted_unique_cls = sorted(set(class_labels))
    if len(sorted_unique_cls) <= 1:
        raise ValueError('Only 1 class label!')
    print('\t>>> Class labels:', sorted(sorted_unique_cls))
    cnt = {}
    for cl in class_labels:
        if cl not in cnt:
            cnt[cl] = 1.0
        else:
            cnt[cl] += 1.0
    # make relative frequencies:
    total = len(class_labels)
    print('\t>>> Label proportion:')
    for cl in sorted_unique_cls:
        print('\t\t+', cl, '>', cnt[cl] / total)

# Ex. 3:
def predict(train_items, test_items):
    print('Predicting! (This might take a while...)')
    predictions = []
    print(len(test_items))
    for test_item in test_items:
        test_feats = test_item[:-1]
        # initialize
        smallest_distance = None
        nearest_neighbour_class = None
        for train_item in train_items:
            current_distance = 0
            train_feats = train_item[:-1]
            for test_f, train_f in zip(test_feats, train_feats):
                if test_f != train_f:
                    current_distance += 1
            if smallest_distance == None:
                smallest_distance = current_distance
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                nearest_neighbour_class = train_item[-1]
        predictions.append(nearest_neighbour_class)
    return predictions


# Ex. 4:
def evaluate(test_instances, predictions):
    correct, total = 0.0, 0.0
    score_correct = {}
    score_total = {}
    x = set([i[-1] for i in test_instances])
    for f in x:
        score_total[f] = 0.0
        score_correct[f] = 0.0
    for item, pred in zip(test_instances, predictions):
        total += 1
        cor_pred = item[-1]
        score_total[cor_pred] += 1.0
        if cor_pred == pred:
            correct += 1
            score_correct[cor_pred] += 1.0
    for k in score_correct:
        print('Score for class:', k, '>', score_correct[k] / score_total[k])
    return correct / total

# Ex. 5 (advanced!):
def predict2(train_items, test_items, n=1):
    from collections import Counter
    predictions = []
    for test_item in test_items:
        test_feats = test_item[:-1]
        distances = []
        for train_item in train_items:
            train_feats = train_item[:-1]
            current_distance = 0
            for test_f, train_f in zip(test_feats, train_feats):
                if test_f != train_f:
                    current_distance += 1
            # add class label and distance to distances
            # for the current test item:
            distances.append((current_distance, train_item[-1]))
        neighbourhood = sorted(distances)[:n]
        cnt = Counter([i[1] for i in neighbourhood])
        cl = cnt.most_common(1)[0][0]
        predictions.append(cl)
    return predictions


##########################################################
print('Train data:')
train_instances = load_file('dimin.train', ',')
print_stats(train_instances)
print('Test data:')
test_instances = load_file('dimin.test', ',')
print_stats(test_instances)
predictions = predict(train_items=train_instances, test_items=test_instances)
print(predictions)
print('Result 1:', evaluate(test_instances, predictions))

##########################################################

predictions = predict2(train_instances, test_instances, n=6)
print(predictions)
print('Result 2:', evaluate(test_instances, predictions))


