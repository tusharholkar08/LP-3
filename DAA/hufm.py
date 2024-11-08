import heapq

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # frequency of symbol
        self.symbol = symbol  # symbol name (character)
        self.left = left  # node left of current node
        self.right = right  # node right of current node
        self.huff = ''  # tree direction (0/1)
    
    # Check if current frequency less than next node's frequency
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    
    # if node is not an edge node then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    
    # if node is edge node then display its huffman code
    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol, new_val))

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

nodes = []

# converting characters and frequencies into heap queue
for i in range(len(chars)):
    heapq.heappush(nodes, Node(freq[i], chars[i]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    
    left.huff = 0
    right.huff = 1
    
    # Combining the 2 smallest nodes to create new node as their parent
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, new_node)

# Passing root of Huffman Tree
print_nodes(nodes[0])
