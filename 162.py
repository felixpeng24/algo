"""
Given a list of words, return the shortest unique prefix of each word. For example, given the list:

dog
cat
apple
apricot
fish
Return the list:

d
c
app
apr
f

"""

#uses trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def insert(word, root):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.count += 1

def find_unique_prefix(word, root):
    node = root
    prefix = ""
    for char in word:
        prefix += char
        if node.children[char].count == 1:
            return prefix
        node = node.children[char]
    return prefix

def shortest_unique_prefix(words):
    root = TrieNode()
    for word in words:
        insert(word, root)
    
    return [find_unique_prefix(word, root) for word in words]

# Example usage
words = ["dog", "cat", "apple", "apricot", "fish"]
print(shortest_unique_prefix(words))
