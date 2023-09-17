#################################################################
# FILE : puzzle_solver.py
# WRITER : israel_nankencki , israelnan , 305702334
# EXERCISE : intro2cs2 ex8 2022
# DESCRIPTION: backtracking solution for nonogram-like game.
# STUDENTS I DISCUSSED THE EXERCISE WITH: none.
# WEB PAGES I USED: none
# NOTES:
#################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from typing import List, Tuple, Set, Optional

# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    this function counts the number of non-definitely seen cells from a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of non-definitely seen cells from the given cell.
    """
    if picture[row][col] == 0:
        return 0
    all_counter = 1
    if col > 0:
        all_counter += look_left_max(picture, row, col)
    if col < len(picture[row]) - 1:
        all_counter += look_right_max(picture, row, col)
    if row > 0:
        all_counter += look_up_max(picture, row, col)
    if row < len(picture) - 1:
        all_counter += look_down_max(picture, row, col)
    return all_counter


def look_left_max(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'max_seen_cells' to count the non-definitely seen cells to the left from a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of non-definitely seen cells to the left from the given cell.
    """
    left_max_counter = 0
    for i in range(col - 1, -1, -1):
        if picture[row][i] == 0:
            return left_max_counter
        else:
            left_max_counter += 1
    return left_max_counter


def look_right_max(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'max_seen_cells' to count the non-definitely seen cells to the right from a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of non-definitely seen cells to the right from the given cell.
    """
    right_max_counter = 0
    for i in range(col + 1, len(picture[row])):
        if picture[row][i] == 0:
            return right_max_counter
        else:
            right_max_counter += 1
    return right_max_counter


def look_up_max(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'max_seen_cells' to count the non-definitely seen cells above a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of non-definitely seen cells above the given cell.
    """
    up_max_counter = 0
    for i in range(row - 1, -1, -1):
        if picture[i][col] == 0:
            return up_max_counter
        else:
            up_max_counter += 1
    return up_max_counter


def look_down_max(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'max_seen_cells' to count the non-definitely seen cells below a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of non-definitely seen cells below the given cell.
    """
    down_max_counter = 0
    for i in range(row + 1, len(picture)):
        if picture[i][col] == 0:
            return down_max_counter
        else:
            down_max_counter += 1
    return down_max_counter


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    this function counts the number of definitely seen cells from a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of definitely seen cells from the given cell.
    """
    if picture[row][col] < 1:
        return 0
    all_counter = 1
    if col > 0:
        all_counter += look_left_min(picture, row, col)
    if col < len(picture[row]) - 1:
        all_counter += look_right_min(picture, row, col)
    if row > 0:
        all_counter += look_up_min(picture, row, col)
    if row < len(picture) - 1:
        all_counter += look_down_min(picture, row, col)
    return all_counter


def look_left_min(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'min_seen_cells' to count the definitely seen cells to the left from a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of definitely seen cells to the left from the given cell.
    """
    left_min_counter = 0
    for i in range(col - 1, -1, -1):
        if picture[row][i] < 1:
            return left_min_counter
        else:
            left_min_counter += 1
    return left_min_counter


def look_right_min(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'min_seen_cells' to count the definitely seen cells to the right from a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of definitely seen cells to the right from the given cell.
    """
    right_min_counter = 0
    for i in range(col + 1, len(picture[row])):
        if picture[row][i] < 1:
            return right_min_counter
        else:
            right_min_counter += 1
    return right_min_counter


def look_up_min(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'min_seen_cells' to count the definitely seen cells above a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of definitely seen cells above the given cell.
    """
    up_min_counter = 0
    for i in range(row - 1, -1, -1):
        if picture[i][col] < 1:
            return up_min_counter
        else:
            up_min_counter += 1
    return up_min_counter


def look_down_min(picture: Picture, row: int, col: int) -> int:
    """
    this function helps 'min_seen_cells' to count the definitely seen cells below a given cell.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row ind of the given cell.
    :param col: the col ind of the given cell.
    :return: the number of definitely seen cells below the given cell.
    """
    down_min_counter = 0
    for i in range(row + 1, len(picture)):
        if picture[i][col] < 1:
            return down_min_counter
        else:
            down_min_counter += 1
    return down_min_counter


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """
    this function checks whether the picture is obeyed to a given set of constraints
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param constraints_set: A set with tuples contains coordinates to each cell and the number of required cells
            to be seen from it.
    :return: 1 if all the constraints are applied exactly in the picture, 0 if at least one of them is violated,
            and 2 if at least one isn't applied exactly bot not violated.
    """
    accuracy = 1
    if not constraints_set:
        return accuracy
    for constraint in constraints_set:
        cur_max_seen = max_seen_cells(picture, constraint[0], constraint[1])
        cur_min_seen = min_seen_cells(picture, constraint[0], constraint[1])
        if constraint[2] > cur_max_seen or constraint[2] < cur_min_seen:
            return 0
        elif cur_min_seen == constraint[2] == cur_max_seen:
            continue
        elif cur_min_seen <= constraint[2] <= cur_max_seen:
            accuracy = 2
    return accuracy


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """
    this function is managing the search fo possible solution to a given set of constrains.
    :param constraints_set: A set with tuples contains coordinates to each cell and the number of required cells
            to be seen from it.
    :param n: the required number of rows in the picture.
    :param m: the required number of columns in the picture.
    :return: A 2D list represents the first solution if there is at least one, None if there isn't.
    """
    picture = prep_initial_picture(n, m, constraints_set)
    solutions = []
    solve_puzzle_helper(picture, constraints_set, 0, solutions)
    if not solutions:
        return
    return solutions[0]


def prep_initial_picture(n: int, m: int, constraints_set: Set[Constraint]) -> Picture:
    """
    this function helps 'solve_puzzle' to create an initial picture to work on.
    :param n: the required number of rows in the picture.
    :param m: the required number of columns in the picture.
    :param constraints_set: A set with tuples contains coordinates to each cell and the number of required cells
            to be seen from it.
    :return: A 2D list with the number of required cells to be seen from each constraint and -1 in all the other cells.
    """
    picture = [[-1 for _ in range(m)] for _ in range(n)]
    for constraint in constraints_set:
        picture[constraint[0]][constraint[1]] = constraint[2]
    return picture


def solve_puzzle_helper(picture: Picture, constraints_set: Set[Constraint], idx: int, sols_list: List[Picture]) -> None:
    """
    this is a recursive helper function to 'solve_puzzle' that conducts the search after possible solutions to a given
    constraints set, using backtracking method.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param constraints_set: A set with tuples contains coordinates to each cell and the number of required cells
            to be seen from it.
    :param idx: the serial number of the current cells to work on.
    :param sols_list: A list suppose to contain all the 2D lists of legal solutions if there are any.
    :return: A list contains all the 2D lists of legal solutions if there are any.
    """
    cur_sol_check = check_constraints(picture, constraints_set)
    if idx == len(picture) * len(picture[0]):
        if cur_sol_check == 1:
            sols_list.append(single_final_solution(picture))
        return
    row, col = idx // len(picture[0]), idx % len(picture[0])
    if picture[row][col] != -1:
        solve_puzzle_helper(picture, constraints_set, idx + 1, sols_list)
        return
    for color in (0, 1):
        if cur_sol_check == 0:
            return
        picture[row][col] = color
        solve_puzzle_helper(picture, constraints_set, idx + 1, sols_list)
    picture[row][col] = -1


def single_final_solution(picture: Picture) -> Picture:
    """
    this function helps 'solve_puzzle_helper' to create the 2D list of possible solution if it's found to be legal one.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :return: A 2D list with only ones and zeros represents the picture with the given solution.
    """
    final_picture = []
    for row in range(len(picture)):
        final_row = []
        for col in range(len(picture[0])):
            if picture[row][col] == 0:
                final_row.append(0)
            else:
                final_row.append(1)
        final_picture.append(final_row)
    return final_picture


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    """
    this function is managing the search fo all possible solution to a given set of constrains.
    :param constraints_set: A set with tuples contains coordinates to each cell and the number of required cells
            to be seen from it.
    :param n: the required number of rows in the picture.
    :param m: the required number of columns in the picture.
    :return: the number of legal solutions to the given set of constraints.
    """
    picture = prep_initial_picture(n, m, constraints_set)
    solutions = []
    solve_puzzle_helper(picture, constraints_set, 0, solutions)
    return len(solutions)


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    """
    this function finds one of the possible sets of constraints that the given picture is the only solution for it.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :return: one of the possible sets of constraints that the given picture is the only solution for it.
    """
    constraints_set = set()
    picture_clone = copy_prep_picture(picture)
    for row in range(len(picture)):
        for col in range(len(picture[row])):
            if picture_clone[row][col] == -1:
                constraints_set.add((row, col, max_seen_cells(picture_clone, row, col)))
                change_seen_cells(picture_clone, row, col)
            elif picture_clone[row][col] == 0:
                constraints_set.add((row, col, 0))
    return constraints_set


def copy_prep_picture(picture: Picture) -> Picture:
    """
    this function helps 'generate_puzzle' to create a suitable copy for the given picture, so it can be changed during
    the search for possible set of constraints.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :return: A 2D list with suitable copy for the given picture.
    """
    new_picture = []
    for row in range(len(picture)):
        new_row = []
        for col in range(len(picture[row])):
            if picture[row][col] == 1:
                new_row.append(-1)
            else:
                new_row.append(picture[row][col])
        new_picture.append(new_row)
    return new_picture


def change_seen_cells(picture: Picture, row: int, col: int) -> None:
    """
    this functon helps 'generate_puzzle' to change cells after it found a constraint, so it wouldn't be searched again.
    :param picture: 2D list with all black cells as 0, white cells as 1, and non-decided yet as -1.
    :param row: the row index of found cell.
    :param col: the col index of found cell.
    :return: None.
    """
    picture[row][col] = 1
    for r in range(col + 1, len(picture[row])):
        if picture[row][r] == 0:
            break
        picture[row][r] = 1
    for l in range(col - 1, -1, -1):
        if picture[row][l] == 0:
            break
        picture[row][l] = 1
    for u in range(row - 1, -1, -1):
        if picture[u][col] == 0:
            break
        picture[u][col] = 1
    for d in range(row + 1, len(picture)):
        if picture[d][col] == 0:
            break
        picture[d][col] = 1
