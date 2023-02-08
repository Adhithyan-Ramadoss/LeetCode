class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in root.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in root.children:
                        return False
                    root = root.children[word[i]]
            return root.end_of_word
        return dfs(0, self.root)

dummy = WordDictionary()
dummy.addWord("bad")
dummy.addWord("dad")
dummy.addWord("mad")
dummy.addWord("pad")
print(dummy.search("bad"))
print(dummy.search(".ad"))
print(dummy.search("b.."))

dummy = WordDictionary()
dummy.addWord("badge")
dummy.addWord("dad")
dummy.addWord("mad")
dummy.addWord("pad")
print(dummy.search("bad"))
print(dummy.search(".ad"))
print(dummy.search("b.dg."))



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)