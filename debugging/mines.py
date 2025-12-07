#!/usr/bin/python3
# لعبة Mines مبسطة مع شرط فوز واضح

from typing import Set, Tuple

Coord = Tuple[int, int]

class Board:
    def __init__(self, rows: int, cols: int, mines: Set[Coord]):
        self.rows = rows
        self.cols = cols
        self.mines = set(mines)
        self.revealed: Set[Coord] = set()

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors(self, r: int, c: int):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if self.in_bounds(nr, nc):
                    yield (nr, nc)

    def adj_mines(self, r: int, c: int) -> int:
        return sum(((nr, nc) in self.mines) for nr, nc in self.neighbors(r, c))

    def reveal(self, r: int, c: int):
        if (r, c) in self.mines or (r, c) in self.revealed:
            return
        self.revealed.add((r, c))
        # في حال كان العدد صفرًا، افتح الجيران (كشف بسيط)
        if self.adj_mines(r, c) == 0:
            for nr, nc in self.neighbors(r, c):
                if (nr, nc) not in self.revealed and (nr, nc) not in self.mines:
                    self.reveal(nr, nc)

    def has_won(self) -> bool:
        total_cells = self.rows * self.cols
        return len(self.revealed) == total_cells - len(self.mines)

def demo():
    # لوحة صغيرة تجريبية
    mines = {(0, 2), (2, 0)}
    b = Board(3, 3, mines)
    # اكشف عدة خلايا غير ألغام لضمان الفوز
    for r in range(3):
        for c in range(3):
            if (r, c) not in mines:
                b.reveal(r, c)
    if b.has_won():
        print("You win!")
    else:
        print("Keep playing.")

if __name__ == "__main__":
    demo()
