from turtle import ht


print('My favorite colors are: pink, purple, blue, and green')
print('Hello', 'world!')
developer = 'Alice'
print(type(developer))

my_str = 'hello world'
print(my_str[0])  # h

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')
    else:
        print('You got it!')


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get the radius
        return self._radius
  
    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)

print(my_circle.radius) # 3
print(my_circle.area) # 28.26

#BUILDING A HASH TABLE
class HashTable:
    def __init__(self):
        """
        Initialize the hash table with an empty collection dictionary.
        The collection will store key-value pairs using the hash as the key.
        """
        self.collection = {}
    
    def hash(self, key):
        """
        Compute a hash value for a given string key.
        
        Args:
            key (str): The string to hash
        
        Returns:
            int: The sum of Unicode values of all characters in the string
        """
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value
    
    def add(self, key, value):
        """
        Add a key-value pair to the hash table.
        
        Args:
            key: The key to store (will be hashed)
            value: The value to associate with the key
        """
        # Compute the hash of the key
        hashed_key = self.hash(key)
        
        # Check if this hash already exists in the collection
        if hashed_key in self.collection:
            # If it exists, add the key-value pair to the existing nested dictionary
            self.collection[hashed_key][key] = value
        else:
            # If it doesn't exist, create a new nested dictionary with this pair
            self.collection[hashed_key] = {key: value}
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        
        Args:
            key: The key to remove (will be hashed)
        """
        # Compute the hash of the key
        hashed_key = self.hash(key)
        
        # Check if the hash exists in the collection
        if hashed_key in self.collection:
            # Check if the specific key exists in the nested dictionary
            if key in self.collection[hashed_key]:
                # Remove the specific key-value pair
                del self.collection[hashed_key][key]
                
                # If the nested dictionary is now empty, remove it
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]
        # If key doesn't exist, do nothing (no error raised)
    
    def lookup(self, key):
        """
        Look up a value by its key.
        
        Args:
            key: The key to look up (will be hashed)
        
        Returns:
            The value associated with the key, or None if not found
        """
        # Compute the hash of the key
        hashed_key = self.hash(key)
        
        # Check if the hash exists in the collection
        if hashed_key in self.collection:
            # Check if the specific key exists in the nested dictionary
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        
        # Key not found
        return None
    
# Example usage:
hash_table = HashTable()
hash_table.add('name', 'Alice')
print(hash_table.lookup('name'))  # Output: Alice

hash_table.add("golf", "sport")
print("After adding 'golf':", hash_table.collection)



# Quick Sort Implementation
def quick_sort(arr):
    """
    Sorts a list of integers using the quicksort algorithm.
    Returns a new sorted list without modifying the input.
    """
    # Base case: return a copy to keep the original list unchanged
    if len(arr) <= 1:
        return arr[:]

    # Choose the first element as the pivot
    pivot = arr[0]

    # Partition into three sublists:
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recursively sort less and greater, then concatenate
    return quick_sort(less) + equal + quick_sort(greater)


# --- Test calls (remove these if not needed for submission) ---
print(quick_sort([20, 3, 14, 1, 5]))        # [1, 3, 5, 14, 20]
print(quick_sort([83, 4, 24, 2]))           # [2, 4, 24, 83]
print(quick_sort([4, 42, 16, 23, 15, 8]))   # [4, 8, 15, 16, 23, 42]
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
# [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]

# Verify that the original list is not modified:
original = [20, 3, 14, 1, 5]
sorted_copy = quick_sort(original)
print("Original:", original)   # [20, 3, 14, 1, 5]  → unchanged
print("Sorted:  ", sorted_copy)




# Towers of Hanoi Solver
def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = [f"{rods[0]} {rods[1]} {rods[2]}"]

    def move(src, dst):
        rods[dst].append(rods[src].pop())
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def hanoi(n, src, dst, aux):
        if n == 0:
            return
        hanoi(n - 1, src, aux, dst)
        move(src, dst)
        hanoi(n - 1, aux, dst, src)

    hanoi(n, 0, 2, 1)
    return "\n".join(states)





# N-Queens Solver
def dfs_n_queens(n):
    solutions = []
    if n < 1:
        return []
    def is_safe(queens, row, col):
        for r in range(row):
            c = queens[r]

            if c == col:
                return False

            if abs(r - row) == abs(c - col):
                return False

        return True

    def backtrack(row, queens):
        if row == n:
            solutions.append(queens[:])
            return

        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                backtrack(row + 1, queens)
                queens.pop()

    backtrack(0, [])
    return solutions