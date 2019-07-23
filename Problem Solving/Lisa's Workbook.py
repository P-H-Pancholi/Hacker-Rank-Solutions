n,k = map(int,input().split())

p = list(map(int,input().split()))

cnt = 0
offset = 1
for chapter in p:
	pages = (chapter + k -1)//k
	for idx in range(pages):
		if offset >= (idx * k)+1 and offset <= min((idx+1)*k, chapter):
			cnt += 1
		offset += 1

print(cnt)
