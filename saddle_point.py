def saddle_points(matrix):
    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError("irregular matrix")
    if len(matrix) == 0:
        return []
    return detect_points([max(row) for row in matrix], [min(col) for col in zip(*matrix)])
    
def detect_points(row_nums, col_nums):
    saddle_points = []
    for i, row in enumerate(row_nums):
        for index in [j for j, col in enumerate(col_nums) if col == row]:
            saddle_points.append({"row": i + 1, "column": index + 1})
    return saddle_points