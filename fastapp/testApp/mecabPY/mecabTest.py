import MeCab
from mecab_tokeninzer import SearchMessage

NEOLOGDIC = '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd'
wakati = MeCab.Tagger('-Owakati ' + NEOLOGDIC)
# wakati2 = MeCab.Tagger('-Ochasen'+NEOLOGDIC)


# txt_data = '僕はカレーが好き。彼は焼肉定食が食べたい。彼女は好きじゃない。叔父はサッカーが好き。スペイン料理を探して下さい。イタリア料理が食べたい。'
# txt_data = "何してたの？"
txt_data = "私は学校に行っていました。私は公園で遊んでました。私は学校から帰ってきました。私は図書館で勉強していました。私は公園を出ました。私は公園で遊んでいます。私は公園から帰ってきました。私は公園で走ってました。"
txt_data = wakati.parse(txt_data).replace('。 ', '。\n').rstrip()
print(txt_data)



#modelの作成
def make_1state_model(txt_data):
    model = {}
    txt_data = txt_data.split('\n')
    for sentence in txt_data:
        if not sentence:  # 空行などは処理しない
            break
        eos_mark = '。！？'
        if sentence[-1] not in eos_mark:  # 行末が。！？でなければ処理しない
            print('not process:', sentence)
            continue
        words = sentence.split(' ')
        previous_word = 'BoS'  # begin of sentence
        for word in words:
            if previous_word in model:
                model[previous_word].append(word)
            else:
                model[previous_word] = [word]
            previous_word = word
    

    return model

model = make_1state_model(txt_data)
# print(model)



from random import randint

keep1,keep2 = SearchMessage.wakati_text("公園で何をしていたの？")

def test_sentence(model,keep1,keep2):
    eos_mark = '。！？'
    key_list = model['BoS']
    key = key_list[randint(0, len(key_list)-1)]
    result = key
    while key not in eos_mark:
        key_list = model[key]
        #共通してる主語を取り出す
        check = set(key_list) & set(keep1)
        if(len(check)>=1):
            key = check.pop()
        else:
            key = key_list[randint(0, len(key_list)-1)]
        result += key
    return result


test_list = []
for _ in range(10):
    test_list.append(test_sentence(model,keep1,keep2))    
    # print(test_sentence(model,keep1,keep2))

# print(test_list)


#答え合わせ
def ans(test_list):
    Ans_text = "私は公園で遊んでました。"
    import difflib
    import Levenshtein

    for co in test_list:
        gestalt1 = difflib.SequenceMatcher(None, Ans_text, co).ratio()
        print([co,gestalt1])

ans(test_list)






