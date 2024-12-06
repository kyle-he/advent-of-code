from collections import defaultdict, Counter

def count_occurrences(data):
    return dict(Counter(data))

def group_by(data, key_func):
    groups = defaultdict(list)
    for item in data:
        groups[key_func(item)].append(item)
    return dict(groups)

def index_by(data, key_func):
    return {key_func(item): item for item in data}

def map_to_values(data, value_func):
    return {item: value_func(item) for item in data}