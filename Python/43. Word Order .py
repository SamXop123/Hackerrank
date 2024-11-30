n = int(input().strip())
word_counts = {}
order = []

for _ in range(n):
    word = input().strip()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        order.append(word)

print(len(order))
print(' '.join(str(word_counts[word]) for word in order))
