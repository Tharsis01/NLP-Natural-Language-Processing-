# import MeCab
# from konlpy.tag import MeCab
# m = MeCab.Tagger()
# out = m.parse("아빠가가방에들어가신다.")
# out1 = m.pos("품사 태깅을 지원합니다")
# out2 = m.morphs("형태소 분리를 지원합니다")
# out3 = m.nouns("명사에 해당하는 형태소만 추출합니다")
# print(out)
# print(out1)
# print(out2)
# print(out3)



with open("example.txt", "r", encoding='UTF8') as f:
    example = f.read()
print(example.replace(" ",""))
ex=example.replace(" ","")

from konlpy.tag import Mecab

mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")

nouns = mecab.nouns(ex)
print('명사 단위:',nouns)
pos = mecab.pos(ex)
print('품사 태깅:',pos)
morphs = mecab.morphs(ex)
print('형태소 단위:',morphs)

