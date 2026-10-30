TEST = False

class Walker:
	def __init__(self, start_x: int = 0,
			start_y: int = 0,
			facing: str ="N") -> None:
		self.current_facing = facing
		self.current_x = start_x
		self.current_y = start_y
		self.path = []
		self.dir_dict = {"N":{"R":"E", "L":"W"},
			"E":{"R":"S", "L":"N"},
			"S":{"R":"W", "L":"E"},
			"W":{"R":"N", "L":"S"}}

	def take_step(self, direction:str, distance: int) -> None:
		# print(f"Old dir {self.current_facing} turning {direction}")
		self.current_facing = self.dir_dict[self.current_facing][direction]
		# print(f"New dir {self.current_facing}")
		match self.current_facing:
			case "N":
				self.current_y += distance
			case "S":
				self.current_y -= distance
			case "E":
				self.current_x += distance
			case "W":
				self.current_x -= distance
		current_location = (self.current_x, self.current_y)
		self.path.append(current_location)
		#print(f"now positioned at {current_location}")

	def get_distance(self) -> int:
		return abs(self.current_x) + abs(self.current_y)

	def find_first_duplicate(self) -> int:
		print(self.path)
		for idx in range(len(self.path)):
			if self.path[idx] in self.path[idx+1:]:
				print(self.path[idx])
				return abs(self.path[idx][0])+abs(self.path[idx][1])

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