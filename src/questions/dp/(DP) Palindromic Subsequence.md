# Longest Palindromic Subsequence (LPS) and Related Problems

## Problem Description

This document outlines key concepts and formulas related to the Longest Palindromic Subsequence (LPS) of a string and its applications to finding minimum insertions or deletions to make a string a palindrome.

*   **Longest Palindromic Subsequence (LPS):** A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindromic subsequence is a subsequence that reads the same forwards and backward. The LPS is the longest such subsequence.

## Key Formulas and Concepts

1.  **Length of LPS:**
    The length of the Longest Palindromic Subsequence (LPS) of a string `str` is equal to the length of the Longest Common Subsequence (LCS) of `str` and its reverse `reverse(str)`.

    `Length of LPS(str) = Length of LCS(str, reverse(str))`

2.  **Minimum Deletions to Make a String a Palindrome:**
    To make a string `str` a palindrome by deleting characters, the minimum number of deletions required is:

    `No. of Deletions = (Length of str) - (Length of LPS(str))`

3.  **Minimum Insertions to Make a String a Palindrome:**
    To make a string `str` a palindrome by inserting characters, the minimum number of insertions required is equal to the minimum number of deletions:

    `No. of Insertions = No. of Deletions`
