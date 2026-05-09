from collections import defaultdict, Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudokuBoardDimension = 9
        columnEntries = defaultdict(list)
        subBoxEntries = defaultdict(list)
        for i in range(sudokuBoardDimension):
            rowEntry = set()
            for j in range(sudokuBoardDimension):
                # traverse row
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowEntry:
                    return False
                rowEntry.add(board[i][j])

                # capture column entries
                columnEntries[j].append(board[i][j])
                possible_subboxentries_indices = [3 * (i // 3) + x for x in range(3)]
                subBoxEntries_idx = [idx for idx in possible_subboxentries_indices if idx % 3 == j // 3][0]
                subBoxEntries[subBoxEntries_idx].append(board[i][j])
        for idx in range(sudokuBoardDimension):
            if len([value for value in Counter(columnEntries[idx]).values() if value > 1]) > 0:
                return False
            if len([value for value in Counter(subBoxEntries[idx]).values() if value > 1]) > 0:
                return False

        return True
                