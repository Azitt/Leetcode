## Find the Difference ###############
def find_diff(str1,str2):
    result = 0
    for c in str1:
        result ^= ord(c)
    for c in str2:
        result ^= ord(c)    
    if len(str2) > len(str1):
        index = str2.index(chr(result))
        return index
    else:
        index = str1.index(chr(result))
        return index
str1,str2 = "wxyz", "zwxgy"
print(find_diff(str1,str2)) 

## Complement of Base 10 Number ############
from math import log2, floor

def find_bitwise_complement(num): 
    bin_count = floor(log2(num)) + 1
    mask = (1 << bin_count) - 1    
    return num ^ mask
print(find_bitwise_complement(42)) 

## Flipping an Image ######################
def flip_and_invert_image(image):
    mid = (len(image[0])-1)//2
    end = len(image[0]) - 1
    for i in range(len(image)):
     for j in range(mid+1):
         image[i][j]  , image[i][end-j] = image[i][end-j]^ 1 , image[i][j] ^ 1
    return image     
         
image = [[1,1,0],[1,0,1],[0,0,0]] 
print(flip_and_invert_image(image)) 

## Single Number #########################
def single_number(nums):
    
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [1,2,2,3,3,1,4]
print(single_number(nums))

## Two Single Numbers ######################
def two_single_numbers(nums):
   bitwise_xor = 0
   for num in nums:
       bitwise_xor ^= num
   
   ##  -bitwise_xor is 2s’ complement bitwise_xor
   bitwise_mask = bitwise_xor & -bitwise_xor

   result = 0
    
   for num in nums:
        if num & bitwise_mask:
            result ^= num
    
   return [result, bitwise_xor ^ result]    
nums = [1,2,2,3,3,4]
print(two_single_numbers(nums))  

## Encode and Decode Strings ###################
def encode(strings):
    encoded_string = ""

    for x in strings:
        encoded_string += length_to_bytes(x) + x

    return encoded_string


def decode(string):
    i = 0
    decoded_string = []

    while i < len(string):
        length = bytes_to_length(string[i : i + 4])
        i += 4
        decoded_string.append(string[i : i + length])
        i += length

    return decoded_string


def length_to_bytes(x):
    length = len(x) 
    bytes = []

    for i in range(4):
        bytes.append(chr(length >> (i * 8)))

    bytes.reverse()
    bytes_string = "".join(bytes)

    return bytes_string


def bytes_to_length(bytes_string):
    result = 0

    for c in bytes_string:
        result = result * 256 + ord(c)

    return result

input = ["coding", "is", "fun"]
encoded = encode(input)
print(decode(encoded))

## Reverse Bits #############
def reverse_bits(n):
    result = 0
    for _ in range(32):  # There are 32 bits in an unsigned 32-bit integer
        result = result << 1  # Shift result to the left by 1 bit to make room for the next
        result = result | (n & 1)  # Add the rightmost bit of n to result
        n = n >> 1  # Shift n to the right by 1 bit to process the next bit
    return result

print(reverse_bits(43261596))

           