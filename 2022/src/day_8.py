from src.util import read_input, result_print
import numpy as np

def solve(day_num, input_file_name):
    grid_a = build_grid_a(input_file_name)
    visible_loc_count = get_visible_locations_count(grid_a)
    best_scenic_score = get_best_scenic_score(grid_a)
    result_print(
        day_num,
        "Number of trees visible from outside the grid",
        visible_loc_count,
        "The highest scenic score possible for any tree on the grid",
        best_scenic_score
    )

def build_grid_a(f_name):
    input_str_lst = read_input(f_name)
    grid_lst = []
    for line in input_str_lst:
        grid_lst.append([ int(digit) for digit in line.strip() ])
    return np.array(grid_lst)

def get_visible_locations_count(grid_a: np.ndarray):
    top_vis_bool_a   = _get_visible_bool_a(grid_a,          range(grid_a.shape[0]),  along_rows=True)
    bot_vis_bool_a   = _get_visible_bool_a(grid_a, reversed(range(grid_a.shape[0])), along_rows=True)
    left_vis_bool_a  = _get_visible_bool_a(grid_a,          range(grid_a.shape[1]),  along_rows=False)
    right_vis_bool_a = _get_visible_bool_a(grid_a, reversed(range(grid_a.shape[1])), along_rows=False)
    vis_bool_a = np.logical_or.reduce(np.stack((top_vis_bool_a, bot_vis_bool_a, left_vis_bool_a, right_vis_bool_a), axis=0), axis=0)
    return np.sum(vis_bool_a)

def _get_visible_bool_a(grid_a: np.ndarray, iter_range, along_rows=True):
    max_along_axis = np.full(grid_a.shape[0], -1)
    vis_bool_a = np.zeros(grid_a.shape, dtype=np.bool8)
    if along_rows:
        for i in iter_range:
            vis_bool_a[i] = grid_a[i] > max_along_axis
            max_along_axis = np.maximum(grid_a[i], max_along_axis)
    else:
        for i in iter_range:
            vis_bool_a[:, i] = grid_a[:, i] > max_along_axis
            max_along_axis = np.maximum(grid_a[:, i], max_along_axis)
    return (vis_bool_a)

def get_best_scenic_score(grid_a: np.ndarray):
    scores_a = np.zeros(grid_a.shape, dtype=np.int_)
    for r in range(grid_a.shape[0]):
        for c in range(grid_a.shape[1]):
            if r == 0 or r == grid_a.shape[0]-1 or c == 0 or c == grid_a.shape[1]-1:
                scores_a[r][c] = 0
            else:
                up_dist = 1
                while r-up_dist > 0:
                    if grid_a[r-up_dist][c] >= grid_a[r][c]:
                        break
                    else:
                        up_dist += 1

                down_dist = 1
                while r+down_dist < grid_a.shape[0]-1:
                    if grid_a[r+down_dist][c] >= grid_a[r][c]:
                        break
                    else:
                        down_dist += 1

                left_dist = 1
                while c-left_dist > 0:
                    if grid_a[r][c-left_dist] >= grid_a[r][c]:
                        break
                    else:
                        left_dist += 1

                right_dist = 1
                while c+right_dist < grid_a.shape[1]-1:
                    if grid_a[r][c+right_dist] >= grid_a[r][c]:
                        break
                    else:
                        right_dist += 1

                scores_a[r][c] = up_dist * down_dist * left_dist * right_dist
    return np.max(scores_a)