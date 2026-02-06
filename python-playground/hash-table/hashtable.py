class HashTable:
    def __init__(self):
        # Requirement 2: Initialize collection as an empty dictionary
        self.collection = {}

    def hash(self, key):
        # Requirement 5 & 14: Sum of Unicode values using ord()
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value

    def add(self, key, value):
        # Requirement 15, 16, 21, 22: Handle storage and collisions
        h_index = self.hash(key)
        
        # If the hash index doesn't exist, create a nested dictionary
        if h_index not in self.collection:
            self.collection[h_index] = {}
        
        # Add the specific key-value pair to the nested dictionary
        self.collection[h_index][key] = value

    def lookup(self, key):
        # Requirement 12, 18, 19, 20: Retrieve value or return None
        h_index = self.hash(key)
        
        # Check if index exists AND if the specific key is in that bucket
        if h_index in self.collection and key in self.collection[h_index]:
            return self.collection[h_index][key]
        return None

    def remove(self, key):
        # Requirement 8, 10, 11, 17: Delete specific key without error
        h_index = self.hash(key)
        
        if h_index in self.collection and key in self.collection[h_index]:
            del self.collection[h_index][key]
            
            # Optional: Clean up empty hash buckets
            if not self.collection[h_index]:
                del self.collection[h_index]
