TEST = False

class Walker:
	def __init__(self, start_x: int = 0,
			start_y: int = 0,
			facing: str ="N") -> None:
		self.current_facing = facing
		self.current_x = start_x
		self.current_y = start_y
		self.path = [(start_x, start_y)]
		self.dir_dict = {"N":{"R":"E", "L":"W"},
			"E":{"R":"S", "L":"N"},
			"S":{"R":"W", "L":"E"},
			"W":{"R":"N", "L":"S"}}

	def take_step(self, direction:str, distance: int) -> None:
		# print(f"Old dir {self.current_facing} turning {direction}")
		self.current_facing = self.dir_dict[self.current_facing][direction]
		self.current_location = self.path[-1]

		match self.current_facing:
			case "N":
				for i in range(1, distance+1):
					self.path.append((self.current_location[0], self.current_location[1]+i))
			case "S":
				for i in range(1, distance+1):
					self.path.append((self.current_location[0], self.current_location[1]-i))
			case "E":
				for i in range(1, distance+1):
					self.path.append((self.current_location[0]+i, self.current_location[1]))
			case "W":
				for i in range(1, distance+1):
					self.path.append((self.current_location[0]-i, self.current_location[1]))
		# print(self.path)
		#print(f"now positioned at {current_location}")


	def get_distance(self) -> int:
		x, y = self.path[-1]
		return abs(x) + abs(y)

	def find_first_duplicate(self) -> int:
		# print(self.path)
		for idx in range(len(self.path)):
			if self.path[idx] in self.path[idx+1:]:
				x,y = self.path[idx]
				return abs(x) + abs(y)

def main(fin):
	# read file
	directions = [elem.strip() for elem in fin.readlines()[0].split(", ")]
	horizontal = 0
	vertical = 0

	# create walker
	walker = Walker()

	# Walk Path
	for step in directions:
		print(step)
		direction = step[0]
		distance = int(step[1:])
		walker.take_step(direction, distance)

	# get answer for part 1
	print("#### PART 1 ####")
	print(f"Final distance is: {walker.get_distance()}")

	# get answer for part 1
	print("#### PART 2 ####")
	print(f"First location to appear twice: {walker.find_first_duplicate()}")

if __name__ ==  "__main__":
	inputfile = "testdata.txt" if TEST else "inputdata.txt"
	with open(inputfile) as fin:
		main(fin)