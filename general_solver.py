from Assignment import create_sudoku_csp, print_sudoku_solution

BOARDS = {
    "easy": "easy.txt",
    "medium": "medium.txt",
    "hard": "hard.txt",
    "veryhard": "veryhard.txt",
}


def main():

    for board in BOARDS.values():
        print(f"Solving {board}:")
        csp, n_backtrack, n_false = create_sudoku_csp(board).backtracking_search()
        print_sudoku_solution(csp)
        print(f"Nr. Backtracks: {n_backtrack}")
        print(f"Nr. False: {n_false}")
        print("\n")


if __name__ == "__main__":
    main()
