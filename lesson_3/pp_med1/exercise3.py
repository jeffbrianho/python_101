# Alyssa was asked to write an implementation of a rolling buffer. 
# You can add and remove elements from a rolling buffer. However, once the buffer becomes full, 
# any new elements will displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# What is the key difference between these implementations?

# one uses a method and mutates the same list the other uses concatenation to create a new list