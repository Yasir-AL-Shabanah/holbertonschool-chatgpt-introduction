#!/usr/bin/python3
# Tic-Tac-Toe 3x3 بسيط: تحقق فوز للصفوف/الأعمدة/الأقطار

def print_board(b):
    for r in range(3):
        print(" ".join(b[r]))

def winner(b):
    lines = []
    # صفوف وأعمدة
    lines.extend(b)
    lines.extend([[b[0][c], b[1][c], b[2][c]] for c in range(3)])
    # أقطار
    lines.append([b[0][0], b[1][1], b[2][2]])
    lines.append([b[0][2], b[1][1], b[2][0]])
    for line in lines:
        if line[0] != "." and line.count(line[0]) == 3:
            return line[0]
    return None

def demo():
    board = [
        ["X", "X", "X"],
        [".", "O", "."],
        ["O", ".", "."],
    ]
    print_board(board)
    w = winner(board)
    if w:
        print(f"{w} wins!")
    else:
        print("No winner yet.")

if __name__ == "__main__":
    demo()
