def print_lines(n):
    for j in range(n):
        if j == 0:
            print("\t_____|", end="")
        elif j > 0 and j < n - 1:
            print("_____|", end="")
        else:
            print("_____", end="")
    print()

def print_row(values, n, i):
    for j in range(n):
        if j == 0:
            print("\t  {}  |".format(values[i][j]), end="")
        elif j > 0 and j < n - 1:
            print("  {}  |".format(values[i][j]), end="")
        else:
            print("  {}  ".format(values[i][j]), end="")
    print()

def print_margin(n):
    for j in range(n):
        if j == 0:
            print("\t     |", end="")
        elif j > 0 and j < n - 1:
            print("     |", end="")
        else:
            print("     ", end="")
    print()

def print_tic_tac_toe(values, n):
    print()
    print_margin(n)
    for i in range(n):
        print_row(values, n, i)
        if i < n - 1:
            print_lines(n)
    print_margin(n)
    print()
    
def print_board_states(self):
    print("\t\trows:", self.rows)
    print("\t\tcols: ", self.cols, "\n\n", sep="")