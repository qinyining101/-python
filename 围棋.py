import tkinter as tk
from error import Qin_TooBig_TooSmall_input_check
from tkinter import messagebox, simpledialog
import random

class GoGame:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'B'  # 默认黑棋先手
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.last_captured_stone = None  # 记录上一次被提掉的棋子位置
        self.create_ui()

    def create_ui(self):
        self.root = tk.Tk()
        self.root.title("围棋")
        self.root.geometry("800x800")  # 设置初始窗口大小
        self.root.bind("<Configure>", self.resize_board)
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.frame, text='', width=2, height=1, command=lambda i=i, j=j: self.place_stone(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
        count_button = tk.Button(self.root, text="数子", command=self.count_stones)
        count_button.pack()

        self.root.mainloop()

    def resize_board(self, event):
        new_size = min(event.width, event.height)
        self.frame.config(width=new_size, height=new_size)
        for i in range(self.size):
            self.frame.rowconfigure(i, weight=1)
        for j in range(self.size):
            self.frame.columnconfigure(j, weight=1)

    def place_stone(self, i, j):
        if 0 <= i < self.size and 0 <= j < self.size:  # 检查边界
            if self.board[i][j] == ' ':
                # 检查落子位置是否有气
                self.board[i][j] = self.current_player
                captured_stones = self.check_captured_stones(i, j)
                if not self.has_liberty(i, j) and not captured_stones:
                    self.board[i][j] = ' '  # 恢复空点
                    messagebox.showwarning("警告", "此处无气，不能落子")
                    return

                # 检查打劫规则
                if self.last_captured_stone and len(captured_stones) == 1 and captured_stones[0] == self.last_captured_stone:
                    self.board[i][j] = ' '  # 恢复空点
                    messagebox.showwarning("警告", "打劫，不能立即提回")
                    return

                self.buttons[i][j].config(text=self.current_player)

                # 检查并吃掉对方的棋子
                if captured_stones:
                    self.last_captured_stone = captured_stones[0] if len(captured_stones) == 1 else None
                    for stone in captured_stones:
                        x, y = stone
                        self.board[x][y] = ' '
                        self.buttons[x][y].config(text='')

                self.current_player = 'B' if self.current_player == 'W' else 'W'  # 修正棋子颜色切换逻辑
            else:
                messagebox.showwarning("警告", "此处已有棋子，不能落子")

    def check_captured_stones(self, i, j):
        captured_stones = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < self.size and 0 <= y < self.size:
                if self.board[x][y] != self.current_player and self.board[x][y] != ' ':
                    if not self.has_liberty(x, y):
                        captured_stones.extend(self.find_group(x, y))
        return captured_stones

    def has_liberty(self, i, j):
        visited = set()
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if self.board[nx][ny] == ' ':
                            return True
                        elif self.board[nx][ny] == self.board[i][j]:
                            stack.append((nx, ny))
        return False

    def find_group(self, i, j):
        visited = set()
        stack = [(i, j)]
        group = []
        while stack:
            x, y = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                group.append((x, y))
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if self.board[nx][ny] == self.board[i][j]:
                            stack.append((nx, ny))
        return group

    def count_stones(self):
        black_count = 0
        white_count = 0
        visited = set()
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'B':
                    black_count += 1
                elif self.board[i][j] == 'W':
                    white_count += 1
                elif self.board[i][j] == ' ' and (i, j) not in visited:
                    territory, owner = self.count_territory(i, j)
                    if owner == 'B':
                        black_count += len(territory)
                    elif owner == 'W':
                        white_count += len(territory)
                    visited.update(territory)
        if black_count > size*size/2:
            messagebox.showinfo("结果", "黑胜")
        else:
            messagebox.showinfo("结果", "白胜")

    def count_territory(self, i, j):
        visited = set()
        stack = [(i, j)]
        territory = []
        owner = None
        while stack:
            x, y = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                territory.append((x, y))
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if self.board[nx][ny] == ' ':
                            stack.append((nx, ny))
                        elif self.board[nx][ny] == 'B':
                            if owner is None:
                                owner = 'B'
                            elif owner != 'B':
                                return territory, ' '
                        elif self.board[nx][ny] == 'W':
                            if owner is None:
                                owner = 'W'
                            elif owner != 'W':
                                return territory, ' '
        return territory, owner

    def ai_battle(self):
        if self.current_player == 'W':
            best_move = self.find_best_move()
            if best_move:
                i, j = best_move
                self.place_stone(i, j)

    def find_best_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'W'
                    score = self.evaluate_board()
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def evaluate_board(self):
        score = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'W':
                    score += 1
                elif self.board[i][j] == 'B':
                    score -= 1
        return score

size = simpledialog.askinteger("输入棋盘大小", "请输入棋盘大小（例如 19 表示 19x19 的棋盘）")
if __name__ == "__main__":
   
    @Qin_TooBig_TooSmall_input_check({'sizes':2},{'sizes':19})
    def main(sizes):
        if(sizes):
            game=GoGame(sizes)
    main(size)