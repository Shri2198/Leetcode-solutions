# LeetCode Solutions with explanations

## 1. Contains Duplicates

- **Algorithm**: Hash Table (Dictionary/HashMap)

- **Explanation**: This solution uses a hash table to track elements we've already seen while iterating through the array. For each element, we check if it already exists as a key in our dictionary. If it does, we've found a duplicate and return True immediately. If not, we add the current element as a key to the dictionary and continue. The hash table provides O(1) average-case lookup time, making this approach efficient.
The implementation stores each number as a key in the dictionary res, with its index as the value (though the value isn't actually used for the duplicate check - only the key's existence matters). This allows us to detect duplicates in a single pass through the array.

- **Time Complexity**: O(n)

## 2. Maximum SubArray

- **Algorithm**: Kadane's Algorithm

- **Explanation**: This solution uses Kadane's algorithm to find the maximum sum of a contiguous subarray. The key insight is that at any point, if our running sum becomes negative, it's better to start fresh from the current element rather than carrying the negative sum forward (since adding a negative number would only decrease any future sums).
The implementation maintains two variables:
`total`: tracks the current subarray sum
`res`: stores the maximum sum seen so far
For each element, we first check if the current running total is negative - if so, we reset it to 0 (effectively starting a new subarray). Then we add the current element to our running total and update our result if this new total is larger than our previous maximum.

- **TimeComplexity**: O(n)

## 3. Missing Number

- **Algorithm**: Hash Set (Hash Table)

- **Explanation**: Converts the array to a set for O(1) lookups, then iterates through numbers 0 to n checking which one is missing. The set eliminates the O(n) list search time from the brute force approach.

- **Time Complexity**: O(n)

## 4. Palindromic Substrings

- **Algorithm**: Expand Around Centers

- **Explanation**: For each possible center position, expands outward to count palindromic substrings. Handles both odd-length palindromes (center at single character) and even-length palindromes (center between two characters). The helper function expands left and right pointers while characters match, counting valid palindromes.

- **Time Complexity**: O(n²)

## 5. Remove Duplicates

- **Algorithm**: Two Pointers

- **Explanation**: Uses two pointers to modify the array in-place. The left pointer tracks the position for the next unique element, while right pointer scans through the array. When a new unique element is found, it's placed at the left position and left is incremented. This maintains all unique elements at the beginning of the array.

- **Time Complexity**: O(n)

## 6. Two Sum

- **Algorithm**: Hash Table (HashMap)

- **Explanation**: Uses a hash table to store each number and its index as we iterate. For each element, calculates the complement (target - current number) and checks if it exists in the hash table. If found, returns the indices of both numbers. This avoids the O(n²) nested loop approach by providing O(1) lookup time.

- **Time Complexity**: O(n)

## 7. Valid Anagram

- **Algorithm**: Hash Table (Character Frequency Counting)

- **Explanation**: Creates frequency maps for both strings by counting occurrences of each character. Two strings are anagrams if they have identical character frequencies. The solution builds hash tables for both strings, then compares them for equality.

- **Time Complexity**: O(n + m)

## 8. Group Anagrams

- **Algorithm**: Hash Table with Sorting (Grouping by Canonical Form)

- **Explanation**: Uses sorting to create a canonical form for each string - anagrams will have identical sorted representations. Groups strings by their sorted form using a hash table where the key is the sorted string and the value is a list of original strings that sort to that key.

- **Time Complexity**: O(n * k log k)

## 9. Top K Frequent Elements

- **Algorithm**: Bucket Sort with Hash Table (Frequency Counting)

- **Explanation**: Uses Counter to get frequency of each number, then employs bucket sort where each bucket index represents a frequency. Places numbers into buckets based on their frequency, then iterates from highest frequency buckets downward to collect the top k frequent elements. This avoids the O(n log n) sorting step by using the constraint that frequencies are bounded by array length.

- **Time Complexity**: O(n)

## 10. Encode and Decode Strings

- **Algorithm**: Length-Prefix Encoding with Delimiter

- **Explanation**: 
    - `Encode`: Prefixes each string with its length followed by "#" delimiter, then the actual string. This handles strings containing any characters (including delimiters) by using length information.
    - `Decode`: Parses the encoded string by first reading the length until "#", then extracting exactly that many characters as the original string. Uses the length to know exactly where each string ends, avoiding ambiguity.


- **Time Complexity**:
    - Encode: O(n) where n is total length of all strings
    - Decode: O(n) single pass through encoded string