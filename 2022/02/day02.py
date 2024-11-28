"""
Advent of Code besvarelser 2022 dag 2
"""


def opgave1(input_data):
    total_score = 0
    def get_outcome(line):
        outcome_dict = {
            "A X": "tie",
            "A Y": "win",
            "A Z": "loss",
            "B X": "loss",
            "B Y": "tie",
            "B Z": "win",
            "C X": "win",
            "C Y": "loss",
            "C Z": "tie",
        }
        return outcome_dict[line]
        
    for line in input_data:
        outcome_score = {
            "win": 6,
            "tie": 3,
            "loss": 0}
        score_for_choosing = {"X": 1, "Y": 2, "Z": 3}
        player1, player2 = line.strip().split(" ")
        line_score = outcome_score[get_outcome(line.strip())] + score_for_choosing[player2]
        total_score += line_score
    
    print(f"svaret på opgave 1 er: {total_score}")
    
def opgave2(input_data):
    """
    A => Rock 1points; B => Paper 2points ; C => scissors 3points
    x = Lose 0points; Y => Tie 3points ; Z => Win 6points
    """
    total_sum = 0
    
    outcome_dict = {
            "A X": 3, #3 for scissor + 0 for lose
            "A Y": 4, #3 for tie + 1 for rock
            "A Z": 8, #2 for paper + 6 for win
            "B X": 1, #1 for rock + 0 for lose
            "B Y": 5, #2 for paper + 3 for tie
            "B Z": 9, #3 for scissor + 6 for win
            "C X": 2, #2 for paper + 0 for lose
            "C Y": 6, #3 for scissor + 3 for tie
            "C Z": 7, #1 for rock + 6 for win
        }
    for line in input_data:
        total_sum += outcome_dict[line.strip()]
    
    print(f"svaret på opgave 2 er: {total_sum}")
    
if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.readlines()
    
    opgave1(lines)
    opgave2(lines)