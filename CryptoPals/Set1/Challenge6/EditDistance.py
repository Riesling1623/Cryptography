"""
    Edit Distance using Dynamic Programming
    Source: https://www.geeksforgeeks.org/edit-distance-dp-5/

    In the challenge, they said: "The Hamming distance is just the number of DIFFERING BITS."
    We need to find the Edit Distance between two binary strings, not two strings.
    So I convert the string to binary.
"""

def conv_bin(test_string):
    return ''.join(format(ord(i), '08b') for i in test_string)

def editDistance(str1, str2):

    # Get the lengths of the input strings
    m = len(str1)
    n = len(str2)

    # Initialize a list to store the current row
    curr = [0] * (n+1)

    # Initialize the first row with values from 0 to n
    for j in range(n+1):
        curr[j] = j
    
    # Initialize a variable to store the previous value
    previous = 0

    # Loop through the rows of the dynamic programming matrix
    for i in range(1, m+1):
        # Store the current value at the beginning of the row.
        previous = curr[0]
        curr[0] = i

        # Loop through the columns of the dynamic programming matrix.
        for j in range(1, n+1):
            # Store the current value in a temporary variable.
            temp = curr[j]

            # Check if the characters at the current positions in str1 and str2 are the same
            if str1[i - 1] == str2[j - 1]:
                curr[j] = previous
            else:
                # Update the current cell with the minimum of the three adjacent cells.
                curr[j] = 1 + min(previous, curr[j - 1], curr[j])
            
            # Update the previous variable with the temporary value.
            previous = temp
        
    # The value in the last cell represents the minimum number of operations
    return curr[n]

# Driver code
if __name__ == '__main__':
    str1 = 'this is a test'
    str2 = 'wokka wokka!!!'

    ans = editDistance(str1, str2)
    print(ans)