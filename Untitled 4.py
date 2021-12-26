alpha = ["e", "f", "h"]
bucket = []

l = len(alpha)
height = 0
width = 0

r = 0

for x in range(0, l):
    bucket.append(alpha[x])
    bbb = ''.join(bucket)
    print(bbb)
    #	print(f'base = {x} height = {height},width = {width}	 {bbb}  ')
    r += 1
    #	while x + 1 # max type
    #	height = x+1
    height = x + 1
    while height != l:
        bucket.append(alpha[height])
        bbb = ''.join(bucket)
        print(bbb)
        #		print(f'height base = {x} height = {height},width = {width}	 {bbb}  ')
        r += 1
        width = height + 1
        while width != l:
            bucket.append(alpha[width])
            bbb = ''.join(bucket)
            print(bbb)
            #			print(f'width base = {x} height = {height},width = {width}	 {bbb}  ')
            r += 1
            width += 1
        bucket.clear()

        break

#	print(f'r = {r}')
