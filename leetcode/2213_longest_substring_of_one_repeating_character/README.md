# 2213. Longest Substring of One Repeating Character

Difficulty: HARD

<https://leetcode.com/problems/longest-substring-of-one-repeating-character/description/>

Start datetime: 2026-10-01T12:35:42

## Problem Statement

You are given a **0-indexed string** `s`. You are also given a 0-indexed string `queryCharacters` of length k and a 0-indexed array of integer indices `queryIndices` of length k, both of which are used to describe k queries.

The ith query updates the character in `s` at index `queryIndices[i]` to the character `queryCharacters[i]`.

Return an array `lengths` of length k where `lengths[i]` is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

### Example 1

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation:

- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc".
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].

### Example 2

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:

- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].

### Constraints

- `1 <= s.length <= 105`
- `s` consists of lowercase English letters.
- `== queryCharacters.length == queryIndices.length`
- `1 <= k <= 105`
- `queryCharacters` consists of lowercase English letters.
- `0 <= queryIndices[i] < s.length`

## Notes

This problem seems like a dynamic programming problem (TODO: Link my DP page
from blog here). Actually I'm not 100% sure yet.

> [!NOTE]
> As I was writing initially, I referenced LSWRC but actually we need longest
substring with at-most one repeating character. Should be similar in approach.

Largest substring without repeating characters is a very common leetcode medium
problem ([3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) ). This problem is essentially composed on top of individual LSWRC problems.

This is because we need to apply the same algorithm for LSWRC to the result of
each of the `k` strings after the `i`th transformation. Then we need to get the
length of each of these largest substrings.

This is a small scale implementation of `MapReduce` where we are writing a program

> composed of a map procedure, which performs filtering and sorting (such as sorting students by first name into queues, one queue for each name), and a reduce method, which performs a summary operation (such as counting the number of students in each queue, yielding name frequencies)

The map is the LSWRC algorithm,
