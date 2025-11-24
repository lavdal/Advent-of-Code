import hashlib

KEY = 'iwrupvqb'

def solve1():
	i = 0
	done = False
	while not done:
		m=hashlib.md5()
		key = f'{KEY}{i}'
		m.update(key.encode('utf-8'))
		hex = m.hexdigest()
		if hex[:6] == '000000':
			return i
		else:
			i+=1
			
print(solve1())