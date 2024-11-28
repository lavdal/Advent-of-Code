from argparse import ArgumentParser
from pathlib import Path
from datetime import date
from shutil import copy

TEMPLATE = Path(r".\template.py")


#læs argumenterne
ap = ArgumentParser()
ap.add_argument("day", type= int, help="Dagen som en int")
ap.add_argument("-y", "--year")

args = ap.parse_args()


#find det rigtige år og dato
today = date.today()
current_year = today.year if today.month == 12 else today.year -1

year = args.year if args.year else current_year
day = args.day


#spørg om der skal fortsættes
choice = input(f"Vil du oprette følgende dag {year} | {day}?\n")


if choice.lower() == "j" or choice.lower() == "y":
    testfil = Path(fr".\{year}\{day:02}\test_data.txt")
    inputfil = Path(fr".\{year}\{day:02}\input.txt")
    
    # hvis ikke mappen findes oprettes den
    testfil.parent.mkdir(exist_ok=True, parents=True)
    
    #opret tomme inputfiler
    if not testfil.exists():
        print(f"opretter {testfil}")
        with open(testfil, "w") as file:
            pass
    if not inputfil.exists():
        print(f"opretter {inputfil}")
        with open(inputfil, "w") as file:
            pass
    
    # opret dagens fil
    py_file = Path(fr".\{year}\{day:02}\{day}.py")
    if not py_file.exists():
        print(f"opretter {py_file}")
        copy(TEMPLATE, py_file)
        
        # rediger DocString'en
        with open(py_file, "r", encoding="utf-8") as fin:
            lines = fin.readlines()
        lines[1]= f"Advent of Code besvarelser {year} dag {day}"
        with open(py_file, "w", encoding="utf-8") as fout:
            fout.writelines(lines)
    
else:    
    print("afbrudt")