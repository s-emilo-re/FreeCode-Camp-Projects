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
        # Compute the hash of the key
        hashed_key = self.hash(key)
        
        # Check if the hash exists in the collection
        if hashed_key in self.collection:
            # Check if the specific key exists in the nested dictionary
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        
        # Key not found
        return None