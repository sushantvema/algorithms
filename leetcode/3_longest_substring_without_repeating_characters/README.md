# 3. Longest Substring Without Repeating Characters

Difficulty: MEDIUM

<https://leetcode.com/problems/longest-substring-without-repeating-characters/description/>

Start datetime: 2026-10-01T13:28:54

## Problem Statement

Given a string `s`, find the length of the **longest substring**  without
duplicate characters.

### Example 1

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

### Example 2

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

### Example 3

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints

- `0 <= s.length <= 10^5`
- `s` consists of English letters, digits, symbols, and spaces

## Notes

This is a pretty foundational problem based on what I have seen.

Perhaps some of the applications are decryption of messages across noisy
communication channels (because messages might get replicated in a payload to
take into account packet loss).

Anyway, let's get started. It's always helpful to look at the examples first, if
provided.

But first - I realize that for any string, if the length of the string == the
length of the elements in its unique set of characters, the longest substring
without duplicate characters is the initial string itself. This logic could be
useful - but is it performant?

Probably not. At least in python, `str.split()` seems to be O(n) in the average
and most common cases, where `n` is the length of the string.

- Without args or with a single-character separator, the algorithm makes linear
passes through the input string to locate delimiters and slice substrings, hence
resulting in O(n) performance (refer to [Stack Overflow: Time/space complexity
of in-built python functions](https://stackoverflow.com/a/55114114) ). Generally
speaking, by looking at the source code of the underlying builtin python
functions we can gauge runtime.
- Python's `set()` is implemented as a **hash table**  under the hood, so
lookup/insert/delete can be expected to be O(1) average (refer to [Stack
Overflow: Time complexity of python set operations?](https://stackoverflow.com/a/44080017) )

The next thing to realize is that the number of possible substrings in a string of up to `k` length (where `k` is the length of the original string) (pertinent because we want to think of the search space)
is finite. In fact, the number of possible substrings is just a clever math trick:

1. Number of substrings of length one is `n` (choose any of the `n` characters)
2. Number of substrings of length two is `n-1` (choose any of the n-1 adjacent pairs, like a sliding window)
3. ... n-2 (adjacent triplets)
4. Length `k` is `n-k+1` where `1 <= k <= n`

So, total number of substrings of all lengths from 1 to `n` = `n + (n-1) + (n-2) + ... + 2 + 1` which `n(n+1) / 2`

This is called the **n-th triangular number formula.**

This of-course is asymptotically O(n^2) for large `n`. That's terrible. This above discussed approach has O(n^2) runtime overall, but is incorrect because we're needlessly thinkign about a bottom-up approach.

Instead, what happens if we start by looking at the largest possible cases and
then reducing the search space iteratively?

This makes me think of some sort of two pointers approach.
