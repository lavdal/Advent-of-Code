TEST = 0

class Part1:
	def __init__(self):
		self.keypad = {(0,0): 1,
			(1,0): 2,
			(2,0): 3,
			(0,1): 4,
			(1,1): 5,
			(2,1): 6,
			(0,2): 7,
			(1,2): 8,
			(2,2): 9,
			}
		self.current_loc = (1,1)

	def get_key(self, line: str) -> int:
#		print(list(line.strip()))
		for direction in list(line):
			x, y = self.current_loc
			match direction:
				case "U":
					new_loc = (x, y-1)
				case "D":
					new_loc = (x, y+1)
				case "L":
					new_loc = (x-1, y)
				case "R":
					new_loc = (x+1, y)
			if new_loc in self.keypad:
#				print(f"{direction}: fra {self.keypad[self.current_loc]} til {self.keypad[new_loc]}")
				self.current_loc = new_loc
#				print(f" now at {self.current_loc}")
#			else:
#				print(f"{direction} bliver på {self.keypad[self.current_loc]}")
				# print(f"{self.keypad[self.current_loc]}")
		return self.keypad[self.current_loc]



def main(fin):
	solver = Part1()

	# Read file
	ans = ""
	lines = fin.readlines()
	for line in lines:
		# print(line)
		ans += str(solver.get_key(line))
	print("#### PART 1 ####")
	print(f"the door code is {ans}")

	print("#### PART 2 ####")
	ans=""
	solver = Part1()
	solver.keypad = {(2,0):1,
		(1,1): 2,
		(2,1): 3,
		(3,1): 4,
		(0,2): 5,
		(1,2): 6,
		(2,2): 7,
		(3,2): 8,
		(4,2): 9,
		(1,3): "A",
		(2,3): "B",
		(3,3): "C",
		(2,4): "D",
		}
	solver.current_loc = (0,2)
	for line in lines:
		ans += str(solver.get_key(line))
	print(f"the door code is {ans}")


if __name__ ==  "__main__":
	inputfile = "testdata.txt" if TEST else "inputdata.txt"
	with open(inputfile) as fin:
		main(fin)