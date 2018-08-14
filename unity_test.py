import collections
x = ('a','b','a','a','c','c')
counter = collections.Counter(x)
print(*counter.items())
count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
print(count_pairs)
words, _ = list(zip(*count_pairs))
print(words) #para que tanta maricada ??? si se puede hacer directamente con la instruccion de abajo?
word_to_id = dict(zip(words, range(len(words))))
print(word_to_id)
