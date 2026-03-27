f = open("blocks_info.txt", "r")
n = int(f.readline())

total = [0] * 26  # for a–z

for _ in range(n):
    w1, w2 = f.readline().split()
    
    count1 = [0] * 26
    count2 = [0] * 26
    
    for c in w1:
        count1[ord(c) - ord('a')] += 1
    
    for c in w2:
        count2[ord(c) - ord('a')] += 1
    
    for i in range(26):
        total[i] += max(count1[i], count2[i])

f.close()

# output
for x in total:
    print(x)