def get_string_entropy(string):
    """
    Return Shannon's entropy of a string
    """
    
    prob = [ float(string.count(char)) / len(string) for char in set(string) ]

    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
   
def main():
    # How is Huffman encoding efficient (comparison with Antropy)
    
    STRING_LENGTH = 15
    TESTS = 100 # 10000
    CHARACTERS = string.ascii_letters + string.digits + string.punctuation
    SIZE = len(CHARACTERS)

    sizes = range(4, SIZE)

    avgs = []
    
    for size in sizes:
    
        sample = CHARACTERS[:size]
        sample_size = len(sample)
        
        delta_values = []
        
        for _ in range(TESTS):
            
            random_string = "".join(random.choices(sample, k=STRING_LENGTH))
            
            huffman = HuffmanEncoding(random_string)
            
            delta_values.append( abs(get_string_entropy(random_string) - huffman.efficiency) )

        huffman_avg = sum(delta_values) / TESTS
        
        print(f"{size} / {SIZE}")
        
        avgs.append(round(huffman_avg, 3))

    # print(sample_size, 20, entropy)
    
    fig = plt.figure()
    ax = fig.add_subplot()
    
    fig.suptitle("Huffman Text Encoding")
    ax.set_title(f"Measurment of Huffman encoding's efficiency (String length : {STRING_LENGTH})")
    
    ax.set_xlabel("Number of different possible characters")
    ax.set_ylabel("Shannon's entropy - Huffman encoding's efficiency (in bits)")
    ax.plot(sizes, avgs)
    plt.show()

if __name__ == '__main__':
    import string, math, random
    import matplotlib.pyplot as plt
    
    main()
