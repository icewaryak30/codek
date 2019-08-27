#to count anagrams
def anagrams(t,w):
	c=0
	for i in range(len(t)-len(w)+1):
		x=t[i:i+len(w)]
		d=0
		for j in x:
			if x.count(j)==w.count(j):
				d+=1
		if d==len(w):
			c+=1
	if c>0:
		return c
	else:
		return -1
text=input()
word=input()
print(anagrams(text,word))
