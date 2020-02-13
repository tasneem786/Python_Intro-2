s= " ATGTCGTACGTAGCTGACGTATAGGTCAAGGCTGCACCGTGTT"
k=l=m=n=0
for i in s :
    if i == "A":
        k+=1

    if i == "T":
        l+=1
    if i == "G":
        m+=1
    if i == "C":
        n+=1

print(k)
print(l)
print(m)
print(n)
