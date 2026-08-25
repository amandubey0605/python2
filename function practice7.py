# strip() is a string method used to remove spaces (or specified characters) from the beginning and end of a string.

# Example 1: Remove spaces
# name = "   Aman   "
# print(name.strip())

# Output:
# Aman

# Q1. write a python function to remove a given word in a list and strip it at same time
def remove_word(lst, word):
    new_list = []

    for item in lst:
        item = item.strip()
        if item != word:
            new_list.append(item)

    return new_list
l = ["aman", "  rohan  ", "harry", "  rohan ", "python"]
print(remove_word(l, "rohan"))


#  Step 1:
# new_list = []

# Creates an empty list where we will store the final answer.

# Step 2:
# for item in lst:

# Takes each item from the list one by one.

# First: "aman"
# Second: " rohan "
# Third: "harry"
# Fourth: " rohan "
# Fifth: "python"
# Step 3:
# item = item.strip()

# Removes extra spaces.

# For example:

# "  rohan  "  →  "rohan"
# Step 4:
# if item != word:

# Checks if the item is not equal to "rohan".

# "aman" != "rohan" → True ✅
# "rohan" != "rohan" → False ❌
# "harry" != "rohan" → True ✅
# Step 5:
# new_list.append(item)

# If the item is not "rohan", add it to new_list.

# So new_list becomes:

# ['aman']
# ['aman', 'harry']
# ['aman', 'harry', 'python']
# Finally:
# return new_list

# Returns:

# ['aman', 'harry', 'python']

# So, the function:

# Removes extra spaces using strip().
# Removes the given word ("rohan").
# Returns the remaining words in a new list.