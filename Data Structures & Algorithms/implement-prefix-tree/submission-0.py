class TrieNode:
    def __init__(self):
        self.children = {} # character -> empty trie node
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        # insert characters into the try
        for c in word:
            # character hasnt been inserted
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # character already exists, move to next and continue loop
            cur = cur.children[c]

        # mark the end of the word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        # check each character
        for c in word:
            # if its not present in the trie immediately return false
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord # make sure its marked as a word and not a prefix

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True

        
        