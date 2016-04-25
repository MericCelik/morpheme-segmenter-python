from __future__ import unicode_literals
from gensim import models as md
import codecs

f = codecs.open('datas/titresim.txt', encoding='utf-8')
for line in f:
    words = f.read().splitlines()

model = md.Word2Vec.load_word2vec_format('datas/tvec.bin', binary=True)

g_suffixes = []
results = []
g_stem = []
for word in words:
    suffixes = []
    stem = word
    count = 0
    for idx in range(len(word)):
        try:
            if model.similarity(stem[:-count], stem) > 0.3:
                suffixes.append(stem[-count:])
                g_suffixes.append(stem[-count:])
                stem = stem[:-count]
                count = 0
        except:
            pass
        count += 1

    g_stem.append(stem)
    result = stem;
    for s in range(len(suffixes)):
        result = result + '-' + suffixes.pop()
    results.append(result)


#    if stem in g_stem:
#        g_stem = stem


# print g_stem

# for result in results:
#     print result

suffixes = list(set(g_suffixes))
with codecs.open('results/suffixes.txt', 'w', 'utf-8') as suf_file:
    for item in suffixes:
        suf_file.write("%s\n" % item)

stems = list(set(g_stem))
with codecs.open('results/stems.txt', 'w', 'utf-8') as stem_file:
    for item in stems:
        stem_file.write("%s\n" % item)

with codecs.open('results/segments.txt', 'w', 'utf-8') as steg_file:
    for item in results:
        steg_file.write("%s\n" % item)
