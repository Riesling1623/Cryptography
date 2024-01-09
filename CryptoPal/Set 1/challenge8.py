"""
    CryptoPals - Set 1
    Challenge 8: Detect AES in ECB mode Solution
"""

line_num = 1

with open("CryptoPal/Set 1/8.txt", 'r') as file:
    for line in file:
        content_line = line[:len(line)-1]   # ignore the \n when read the text file
        blocks_content_line = [ content_line[(16*i):(16*(i+1))] for i in range(int(len(content_line)/16)) ]
        set_blocks = set(blocks_content_line)
        if len(blocks_content_line) != len(set_blocks):
            # The problem with ECB is that it is stateless and deterministic, so if two lengths if different, that means it has the same 16 byte plaintext
            # This solution is only true for this situation
            print("AES in ECB mode in line", line_num)
            break
        else:
            line_num += 1

# done