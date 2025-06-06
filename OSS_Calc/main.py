import tkinter as tk
from calc import Calculator


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

    
from calc import calculate_root
import tkinter as tk
from calc import Calculator


def run_tests():
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("[제곱근 계산기 테스트]\n")
        f.write("144 -> " + str(calculate_root(144)) + "\n")
        f.write("-36 -> " + str(calculate_root(-36)) + "\n")
        f.write("문자 -> " + str(calculate_root("abc")) + "\n")
        
if __name__ == "__main__":
    run_tests()  
    
