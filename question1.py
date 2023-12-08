from collections import deque
import time


def timer(func):
    def inner(*args, **kwargs):
        start = time.process_time()
        result = func(*args, **kwargs)  # Capture the result of the decorated function
        end = time.process_time()
        print(end - start)
        return result  # Return the result
    return inner

# [A]
@timer
def get_final_queue_order(input_file):
    # Using a deque (Doubly ended queue) to "append" (& "appendleft") from both ends of the container.
    queue = deque()
    try:
        with open(input_file, 'r') as text_file:
            for line in text_file:
                line = line.strip()
                if not line:
                    continue
                command, name = line.split(' ')
                if command == 'JUMP':
                    queue.appendleft(name)
                elif command == 'JOIN':
                    queue.append(name)
    except FileNotFoundError:
        print(f'File not found: {input_file}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    else:
        return list(queue)


if __name__ == '__main__':
    print(get_final_queue_order('hw3_q1.txt'))

# note:or go through list and append all the joins, append all the jumps and concatenate the lists/work frm middle out

# [B]
# TIME AND SPACE COMPLEXITY:
# Time Complexity:
# For this function the time complexity is primarily determined by the for loop that iterates
# through each line of the input_file.
# .strip() and .split() are constant time operations.
# It is the append() and appendleft() methods which contribute most to the time complexity.
# Using a deque() provides a O(1) time complexity for append() and appendleft(), as they both take constant time.
# (Unlike if they were used in a list which would provide O(N) complexity).
# Nevertheless, the loop iterates through each line in the input_file once, therefore the overall time complexity
# is O(N), whereby N is the number of lines in the file, and append operations are performed once within each iteration
# and are constant time.

# Space Complexity:
# This is determined by the additional memory used by my solution (excluding input space).
# The main contributor to space complexity is the deque, which is the primary data structure which
# stores the names of people in the queue. In the worst case, the deque could grow to accommodate all the names from
# the input file. It's space complixity is O(N), where N is the number of names in the queue.
# Other variables, such as line, command and name contribute space O(1).
# The list conversion at the end doesn't significantly affect the overall space complexity,
# as it creates a new list with the same elements of the deque. It has a space complexity of O(N) because the new
# list created is of size N.
# Thus, for my solution the overall space complexity is O(N), whereby N is the number of names in the queue.

# In summary, the provided solution has a linear time complexity O(N) and a linear space
# complexity O(N), where N is the number of lines in the input file.

# ASSUMPTIONS:
# I am assuming the input_file follows the stated format of the question,
# i.e. 'The first word on each line will either be “JUMP” or “JOIN” and the second word the
# name of the person', and that each word is separated by a space (' ').
# I also am assuming that the file only contains the commands 'JUMP' or 'JOIN', otherwise it will raise an
# error. Additionally, I am assuming that the file is not empty and contains text.
# I am assuming that the file exists, and that the function will handle a FileNotFoundError.
# I am assuming that function handles unexpected errors during file processing with the Exception.
