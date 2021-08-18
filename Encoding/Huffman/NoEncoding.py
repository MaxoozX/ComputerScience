class DefaultEncoding:
    """
    The default encoding, with 8 bits per characters (Assuming these are ASCII characters)
    """
    
    def __init__(self, string):
        self.original_string = original_string
        self.encoded_string = DefaultEncoding.encode(string)
        self.encoded_length = len(encoded_string)
        self.original_length = len(string)
        self.efficiency = self.encoded_length / self.original_length
    
    @staticmethod
    def encode(string):
        """
        format function instead of bin to keep leading zeros
        
        format("{}")
            # if I want 0b
            010 for 0 padding and 10 in total (counting 0b even if not in it)
            b for binary
        """
        char_values = [ord(char) for char in string]
        binary_values = [format(char, "010b") for char in char_values]
        binary_values_without_prefix = [char_bits[2:] for char_bits in binary_values]
        encoded = ''.join(binary_values_without_prefix)
        
        return encoded
    
    @staticmethod
    def decode(encoded_string):
        
        splited_string = [encoded_string[index:index+8] for index in range(0, len(encoded_string), 8)]
        
        char_values = [int(binary_value, 2) for binary_value in splited_string]
        
        chars = [chr(value) for value in char_values]
        
        decoded = "".join(chars)
        
        return decoded
        
if __name__ == '__main__':

    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    # Without performances measurement
    encoded = DefaultEncoding.encode(string)
    decoded = DefaultEncoding.decode(encoded)
    print(decoded)
    
    # With perfomances measurment
    encoded = DefaultEnoding(string)
    print(encoded.efficiency)
