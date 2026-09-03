# Comb Sort

Comb sort is an improvement over [[bubble-sort]] aiming to eliminate the problem
of small values near the end of the list, which  causes bubble sort to take more
time than necessary.

Comb sort uses a larger gap for comparison which gradually reduces until it
becomes 1.

Helps by "jumping over" some unnecsssary comparisons and swaps.

Apparently, an optimum shrink factor has been found to be 1.3 (by testing Comb
sort over 200k random lists).

Worst case remains O(n^2)
