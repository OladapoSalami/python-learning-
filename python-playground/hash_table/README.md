# 🗄️ Hash Table Implementation
A custom implementation of a Hash Table data structure in Python, focusing on hash functions and collision resolution.

### 🧠 How it Works:
1. **Hash Function:** The `hash()` method converts a string key into a numerical index by summing the Unicode (`ord()`) values of its characters.
2. **Collision Handling:** This implementation uses **Chaining**. If two different keys produce the same hash index, they are stored in a nested dictionary (a "bucket") at that index to prevent data loss.
3. **Efficiency:** Provides near-instant data retrieval (`lookup`) by jumping directly to the calculated index.

### 🛠 Methods Included:
* `add(key, value)`: Hashes the key and stores the value in the correct bucket.
* `lookup(key)`: Retrieves the value associated with a key, returning `None` if not found.
* `remove(key)`: Deletes a specific key-value pair and cleans up empty buckets.

### 💻 Concepts Applied:
* Data Structure Design
* Hash Algorithms (Unicode Summation)
* Collision Resolution (Chaining)
* Python Dictionary Manipulation
