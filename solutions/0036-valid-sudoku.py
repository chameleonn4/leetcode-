# 36. Valid Sudoku / 有效的数独
# 难度：中等    语言：Python3    日期：2026-10-20
# 链接：https://leetcode.cn/problems/valid-sudoku/
# 思路：一遍遍历 + 三个哈希表。给每一行、每一列、每一个 3×3 宫各开一个 dict 记录「这个数字出现过没有」；
#       扫到非空格子时算出它属于哪个宫 box_index = (i // 3) * 3 + j // 3，
#       只要行、列、宫任一已经出现过这个数字，就说明违反了规则；否则把三处都标记上。
#       注意：只需要判断已填数字是否合法，不要求数独可解。
# 复杂度：时间 O(81) = O(1)，空间 O(81) = O(1)

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_map = [{} for _ in range(9)]
        cols_map = [{} for _ in range(9)]
        boxes_map = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                box_index = (i // 3) * 3 + j // 3
                row_num = rows_map[i].get(num, 0)
                col_num = cols_map[j].get(num, 0)
                box_num = boxes_map[box_index].get(num, 0)
                if row_num > 0 or col_num > 0 or box_num > 0:
                    return False
                rows_map[i][num] = 1
                cols_map[j][num] = 1
                boxes_map[box_index][num] = 1
        return True
