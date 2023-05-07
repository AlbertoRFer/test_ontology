import os
import subprocess

def latex2image(latex_code, output_file):
    with open(output_file + ".tex", "w") as f:
        f.write("\\documentclass[border=1pt]{standalone}\n")
        f.write("\\usepackage{amsmath}\n")
        f.write("\\begin{document}\n")
        f.write(latex_code)
        f.write("\\end{document}\n")

    subprocess.run(["latex", "-interaction=nonstopmode", output_file + ".tex"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["dvipng", "-D", "150", "-T", "tight", "-z", "9",
                    "-bg", "Transparent", "-o", output_file + ".png", output_file + ".dvi"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.remove(output_file + ".tex")
    os.remove(output_file + ".aux")
    os.remove(output_file + ".log")
    os.remove(output_file + ".dvi")
    
variable_dict = {}
with open("variables.txt", "r") as f:
    for i, line in enumerate(f):
        key = "V_" + str(i+1)
        value = line.strip()
        variable_dict[key] = value

with open("equations.txt", "r") as f:
    for i, line in enumerate(f):
        key = "E_" + str(i+1)
        value = line.strip()
        variable_dict[key] = value

variable_dict["no_eq"] = "No equation"        
for output, code in variable_dict.items():
    latex2image(code, output)
