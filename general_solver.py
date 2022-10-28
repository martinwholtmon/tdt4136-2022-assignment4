from Assignment import create_map_coloring_csp, create_sudoku_csp, print_sudoku_solution

BOARDS = {
    "easy": "easy.txt",
    "medium": "medium.txt",
    "hard": "hard.txt",
    "veryhard": "veryhard.txt",
}


def main():

    for board in BOARDS.values():
        print(f"Solving {board}:")
        csp = create_sudoku_csp(board).backtracking_search()
        print_sudoku_solution(csp)
        print("\n")


if __name__ == "__main__":
    main()
