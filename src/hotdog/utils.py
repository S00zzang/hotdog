def get_max_label(p):
    max_score = 0 
    max_label = ""
    for item in p:
        if item['score'] > max_score:
            max_score = item['score']
            max_label = item['label']

        return max_label

def get_score(item):
    return item['score']

def get_max_label2(p):
    max_p = max(p, key = get_score)

    return max_p['label']

def get_max_label3(p):
    max_p = max(p, key = lambda x: x['score'])

    print(max_p)

    return max_p['label']
