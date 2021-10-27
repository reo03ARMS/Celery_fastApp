# import MeCab

# NEOLOGDIC = '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd'
# # tagger = MeCab.Tagger('-Owakati ' + NEOLOGDIC)
# tagger = MeCab.Tagger(NEOLOGDIC)
# tagger.parse('')  # workaround


# def tokenize(text):
#     keep = tagger.parse(text).strip().split(' ')
#     return keep


# # 取り出したい品詞
# select_conditions = ['動詞', '名詞']
# def wakati_text(text):
#     # 分けてノードごとにする
#     node = tagger.parseToNode(text)
#     terms = []
#     while node:
#         # 単語
#         term = node.surface
#         # 品詞
#         pos = node.feature.split(',')[0]
#         # もし品詞が条件と一致してたら
#         if pos in select_conditions:
#             terms.append(term)
#         node = node.next
#     return terms



# tokens = tokenize('スペイン料理を探して') 
# print(tokens)
# print(type(tokens))


#文章の重要なところ（目的）のみを取り出す
# test = wakati_text("僕は公園で遊んでいました")
# print(test)


class SearchMessage():
    
    def wakati_text(text):
        import MeCab
        NEOLOGDIC = '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd'
        tagger = MeCab.Tagger(NEOLOGDIC)
        tagger.parse('')  # workaround
        select_conditions1 = ['名詞']
        select_conditions2 = ["動詞"]


        # 分けてノードごとにする
        node = tagger.parseToNode(text)
        terms_main = []
        terms_sub = []
        while node:
            # 単語
            term = node.surface
            # 品詞
            pos = node.feature.split(',')[0]
            # もし品詞が条件と一致してたら
            if pos in select_conditions1:
                terms_main.append(term)
            if pos in select_conditions2:
                terms_sub.append(term)
            node = node.next
        return terms_main,terms_sub
    
        




