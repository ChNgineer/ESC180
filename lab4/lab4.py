from utilities import *

def parse_story(file_name):
    file = open(file_name, 'r')
    F = file.read().lower().split()
    F1 = ' '.join(F).replace('(',"").replace(')',"").replace('{',"").replace('}',"").replace('"',"").replace('[',"").replace(']',"").replace('!'," ! ").replace('?'," ? ").replace('.'," . ").replace(','," , ").replace(':'," : ").replace(';'," ; ")
    F2 = F1.split()
    return F2

def get_prob_from_counts(counts):
    prob = []
    for i in counts:
        prob.append(i / sum(counts))
    return prob

def build_ngram_counts(words, n):
    dictionary = {}
    key = []
    info = []
    word_list = []
    word_list1 = []
    counts = []
    list_of_keys = []
    cut_list = words[n:]
    
    for i in range(len(words)-n):
        j = i
        while j < n+i:
            key.append(words[j])
            j += 1
        dictionary[tuple(key)] = []
        list_of_keys.append(key)
        key = []
    word_list = list(zip(list_of_keys,cut_list))
    #print(word_list)
    #print(range(len(list(dictionary.keys()))))
    #print(range(len(word_list)))
    for k in range(len(list(dictionary.keys()))):        
        for l in range(len(word_list)):
            if list(list(dictionary.keys())[k]) ==  word_list[l][0]:
                word_list1.append(word_list[l][1])
        #print(word_list1)
        #print(tuple(list(dictionary.keys())[k]))
        temp_count = {c:word_list1.count(c) for c in word_list1}
        counts = list(temp_count.values())
        #print(counts)
        word_list1 = list(dict.fromkeys(word_list1))        
        info.append(word_list1)
        info.append(counts)
        dictionary[tuple(list(dictionary.keys())[k])] = info
        word_list1 = []
        counts = []
        info = []
    return dictionary
        
def prune_ngram_counts(counts, prune_len):
    #print(counts)
    new_words = []
    del_prob = []
    for i in counts:
        prob = counts[i][1]
        words = counts[i][0]
        #print(prob)
        #print(words)

        test = sorted(zip(prob,words), reverse = True)[0:prune_len]
        #print(list(zip(prob,words))[len(prob)-1][0])
        partition = test[len(test)-1][0]
        #print(partition)
        k = 0
        while k < len(prob):
            #print(k)
            if prob[k] < partition:
                prob.remove(prob[k])
                words.remove(words[k])
                
            k += 1
        return counts            

def probify_ngram_counts(counts):
    info = []
    #print(range(len(counts)))
    for i in range(len(counts)):
        prob = list(counts.values())[i][1]
        words = list(counts.values())[i][0]
        prob = get_prob_from_counts(prob)
        info.append(words)
        info.append(prob)
        counts[tuple(list(counts.keys())[i])] = info
        info = []
    return counts
    
def build_ngram_model(words, n):
    dictionary = probify_ngram_counts(build_ngram_counts(words, n))
    #print(dictionary)
    new_list = list(dictionary.values())
    #print(new_list)
    for i in range(len(new_list)):
        zip(new_list[i][1],new_list[i][0])
        new_list[i][1].sort()
        if len(new_list[i][1]) > 15:
            new_list[i][1] = new_list[i][1][:14]
    return probify_ngram_counts(build_ngram_counts(words, n))

def gen_bot_list(ngram_model, seed, num_tokens=0):
    length = len(list(ngram_model.keys())[0])
    new_list = list(seed)[:]
    next_token = gen_next_token(seed[len(seed)-length:len(seed)],ngram_model)
    new_key = [new_list[len(new_list)-1],next_token]
    #new_key.append(new_list[len(new_list)-1])
    #new_key.append(next_token)
    #print(tuple(new_key))
    if (tuple(new_key) not in ngram_model) and (len(new_list) < num_tokens):
        new_list.append(next_token)
        #print('no')
        #print(new_list)
        return new_list
    if len(list(seed)) == num_tokens:
        #print('help')
        #print(new_list)
        return new_list
    elif len(new_list) < num_tokens:
        #print(seed[len(seed)-2:len(seed)])
        #print(next_token)
        new_list.append(next_token)
        #print(new_list)
        return gen_bot_list(ngram_model,tuple(new_list),num_tokens)
    elif len(new_list) > num_tokens:
        new_list.pop()
    

def gen_bot_text(token_list, bad_author):
    if bad_author == True:
        return ' '.join(token_list)
    else:
        for i in range(len(token_list)-1):
            if i == 0:
                token_list[0] = token_list[0].capitalize()
            if token_list[i] in BAD_CHARS:
                del token_list[i]
            elif token_list[i] in END_OF_SENTENCE_PUNCTUATION:
                token_list[i+1] = token_list[i+1].capitalize()
            elif token_list[i] in ALWAYS_CAPITALIZE:
                token_list[i] = token_list.capitalize()
        new_string = ' '.join(token_list)
        for i in range(len(new_string)-1):
            #print(new_string[i])
            if new_string[i] in VALID_PUNCTUATION:
                #print(new_string[i])
                new_string = new_string[:i-1] + new_string[i:]
                
        return new_string
    
'''
def write_story(file_name, text, title, student_name, author, year):'''

if __name__ == '__main__':

    #Test cases material
    token_list = ['this', 'is', 'a', 'string', 'of', 'text', '.', 'which', 'needs', 'to', 'be', 'created', '.']
    words1 = ['the', 'child', 'will', 'the', 'child', 'can', 'the', 'child', 'will', 'the', 'child', 'may', 'go', 'home', '.']
    ngram_counts= {('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]],('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],('toronto', 'is'): [['six', 'drake'], [2, 3]]}
    words = ['the', 'child', 'will', 'go', 'out', 'to', 'play', ',', 'and', 'the', 'child', 'can', 'not', 'be', 'sad', 'anymore', '.']
    ngram_model = {('the', 'child'): [['will', 'can','may'], [0.5, 0.25, 0.25]],
                   ('child', 'will'): [['the'], [1.0]],
                   ('will', 'the'): [['child'], [1.0]],
                   ('can', 'the'): [['child'], [1.0]],
                   ('child', 'may'): [['go'], [1.0]],
                   ('may', 'go'): [['home'], [1.0]],
                   ('go', 'home'): [['.'], [1.0]]}
    #Test cases
    parse_story('test_text_parsing.txt')
    get_prob_from_counts([10,20,40,30])
    build_ngram_counts(words, 2)
    prune_ngram_counts(ngram_counts,3)
    probify_ngram_counts(ngram_counts)
    build_ngram_model(words1,2)
    gen_bot_list(ngram_model,('the','child'),5)
    gen_bot_text(token_list, False)                                                                                                                                                                                                  
