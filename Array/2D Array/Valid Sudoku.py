# Use one unified set of tuples to save seen occurences of all three types. Format: ( type_identifier, number, row/col/box_label(s) )
# type_identifier is some custom number, like 1 indicates row type, 2 indicates column type
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()  # saves observed (1, num, row) or (2, num, col) or (3, num, i // 3, j // 3)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                num = board[i][j]
                if (1, num, i) in seen or (2, num, j) in seen or (3, num, i // 3, j // 3) in seen:
                    return False
                else:
                    seen.add((1, num, i))
                    seen.add((2, num, j))
                    seen.add((3, num, i // 3, j // 3))

        return True

# Or scan 3 times to save space:
# 	public boolean isValidSudoku(char[][] board) {
# 	    if (board == null || board.length != 9 || board[0].length != 9)
# 		return false;

# 	    HashSet<Integer> nums = new HashSet<Integer>(9);

# 	    for (int i = 0; i < 9; i++) {
# 		nums.clear();
# 		for (int j = 0; j < 9; j++) {
# 		    char c = board[i][j];

# 		    if (c != '.' && nums.contains('0' - c))
# 			return false;
# 		    nums.add('0' - c);
# 		}
# 	    }

# 	    for (int i = 0; i < 9; i++) {
# 		nums.clear();
# 		for (int j = 0; j < 9; j++) {
# 		    char c = board[j][i];

# 		    if (c != '.' && nums.contains('0' - c))
# 			return false;
# 		    nums.add('0' - c);
# 		}
# 	    }

# 	    for (int m = 0; m < 9; m += 3) {
# 		for (int n = 0; n < 9; n += 3) {
# 		    nums.clear();
# 		    for (int i = m; i < m + 3; i++) {
# 			for (int j = n; j < n + 3; j++) {

# 			    char c = board[i][j];
# 			    if (c != '.' && nums.contains('0' - c))
# 				return false;
# 			    nums.add('0' - c);

# 			}
# 		    }
# 		}
# 	    }

# 	    return true;
# 	}
#     }

#     /*
#      * [2015] Simpler to implement, but costs much more space
#      *
#      * *NOTE: element board[i][j] belongs to the (i/3*3 + j/3)-th sub-board
#      */
#     public class Solution {
# 	public boolean isValidSudoku(char[][] board) {
# 	    boolean[][] rows = new boolean[9][9];
# 	    boolean[][] columns = new boolean[9][9];
# 	    boolean[][] blocks = new boolean[9][9];

# 	    for (int i = 0; i < 9; i++) {
# 		for (int j = 0; j < 9; j++) {
# 		    if (board[i][j] == '.') {
# 			continue;
# 		    }
# 		    int num = board[i][j] - '1';// let c belongs to 0 ~ 8
# 		    if (rows[i][num] || columns[j][num] || blocks[i / 3 * 3 + j / 3][num]) {
# 			return false;
# 		    }
# 		    rows[i][num] = columns[j][num] = blocks[i / 3 * 3 + j / 3][num] = true;
# 		}
# 	    }

# 	    return true;
# 	}
#     }