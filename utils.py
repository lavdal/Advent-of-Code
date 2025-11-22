from pathlib import Path

class Grid:
    def __init__(self, file: Path):
        self.grid = []
        try:
            with open(file, "r") as fin:
                lines = fin.readlines()
                for line in lines:
                    self.grid.append([char for char in line.strip()])
        except Exception as e:
            print(f"Error reading grid from {file}: {e}")
    