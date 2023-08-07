"""Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def insertWords(root, word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True

        for word in words:
            insertWords(self.root, word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()     # to avoid duplication use res as set

        def dfs(r, c, node, word):
            if node.word:
                res.add(word)
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                    board[r][c] not in node.children):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))
            return
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, self.root, "")
        return res
