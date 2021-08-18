"""
File where I experiment Huffman encoding.

The shortest way to encode text by only encoding length-1 (only using length-1 pattern)

The efficiency of the huffman encoding depends on the entropy, the lowest the entropy, the highest the efficency

"""
from collections import Counter

class Node:
    """
    A simple node class to work with the huffman tree
    """
    
    def __init__(self, name, value, children=None):
        self.children = children if children else []
        self.name = name
        self.value = value
        
    def __repr__(self):
        return f"Node[{self.name}, {self.value}]"
     
class HuffmanEncoding:
    """
    Encode an ASCII string using an huffman tree to get the shortest output possible.
    """
    
    def __init__(self, string):
        """
        Algorithm steps
        
        1 - Count how many times appear each character
        
        2 - Get every character (without repetition) in order of number of apparitions
        
        3 - Add a corresponding node to each character in a the pool
        
        WHILE LEN(POOL) > 1 {
            
            4 - Find the lowest sum of two consequetives value (the most to the right)
            
            5 - Get the 2 corresponding nodes
            
            6 - Create a new node with the two nodes as children, remove the two nodes and replace them with the new node
            
        } # The tree is now built
        
        7 - Iterate through the tree to the edges and to assign each character it's huffman code
        
        8 - Encode the string using the new characters' codes
        
        """
        
        self.original_string = string
        self.encoded_string, self.char_dict = self.encode(string)
        self.encoded_length = len(self.encoded_string)
        self.original_length = len(string)
        self.efficiency = self.encoded_length / self.original_length
        
    @staticmethod
    def _build_tree(string):
      
        char_counter = Counter(string)
        
        pool = [ Node(char, frequence) for char, frequence in char_counter.most_common() ]
        
        new_node = None
        
        while len(pool) > 1:
            
            sum_of_two_consequtives = HuffmanEncoding._get_sums_of_pairs(pool)
            
            minimum = (float('inf'), None)
            for index, value in enumerate(sum_of_two_consequtives):
                if value <= minimum[0]:
                    minimum = (value, index)
                    
            index = minimum[1] + 1
        
            node_a = pool[index-1]
            node_b = pool[index]
            new_node = Node(
                "".join((node_a.name, node_b.name)),
                node_a.value + node_b.value,
                [node_a, node_b]
                )
            pool[index-1:index+1] = [new_node]
            
        # Cover the case where the string is only composed of a single character (maybe multiple times)
        root = new_node if new_node else Node(pool[0].name, pool[0].value, [pool[0]])
        return root
        
    @staticmethod
    def _iterate_through_edges(root):
        char_dict = {}
    
        # Recursion may not be the fastest but it's the easiest
        def iterate(node, string):
            # print(node.children, string)
            if not node.children:
                char_dict[node.name] = string
            for index, child in enumerate(reversed(node.children)):
                iterate(child, string + str(index))
                            
        iterate(root, "")
        
        return char_dict
        
    @staticmethod
    def _encode_with_char_dict(string, char_dict):
        return  "".join([char_dict[char] for char in string])
        
    @staticmethod
    def _get_sums_of_pairs(pool):
        return [pool[i-1].value + pool[i].value for i in range(1, len(pool))]
        
    @staticmethod
    def encode(string):
        root = HuffmanEncoding._build_tree(string)
        char_dict = HuffmanEncoding._iterate_through_edges(root)
        encoded = HuffmanEncoding._encode_with_char_dict(string, char_dict)
        return encoded, char_dict
    
    @staticmethod
    def decode(encoded_string, characters_dict):
        # Using a buffer
        
        decoding_dict = {v: k for k, v in characters_dict.items()}
        
        output = ""
        bits_buffer = ""
        
        for bit in encoded_string:
            bits_buffer += bit
            if bits_buffer in decoding_dict:
                output += decoding_dict[bits_buffer]
                bits_buffer = ""
                
        return output
      
if __name__ == '__main__':
    
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    
    encoded, char_dict = HuffmanEncoding.encode(string)
    decoded = HuffmanEncoding.decode(encoded, char_dict)
    print(decoded)
    
    encoded = HuffmanEncoding(string)
    print(encoded.efficiency)
