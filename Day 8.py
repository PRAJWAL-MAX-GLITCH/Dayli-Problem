class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
        self.length = float('inf')

class Solution:
    def insert(self, root, word, idx):
        node = root
        if len(word) < node.length:
            node.length = len(word)
            node.index = idx
        for char in reversed(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(word) < node.length:
                node.length = len(word)
                node.index = idx

    def search(self, root, word):
        node = root
        for char in reversed(word):
            if char not in node.children:
                break
            node = node.children[char]
        return node.index

    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()
        for i, word in enumerate(wordsContainer):
            self.insert(root, word, i)
        result = []
        for word in wordsQuery:
            result.append(self.search(root, word))
        return result
