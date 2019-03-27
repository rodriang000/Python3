Homework 05
===========

Part 1
------
1.) I used a generator function for every char in the alphabet took the permutations
of perm in permutations of length -1 of the alphabet. It then yielded char + the 
permutations. 
2.) In the smash is where the filtering for passwords, in one long list comprehension.
I looked for the prefix + character using the permutations function, and then compared 
the results to see if the sha1sum is in hashes. 
3.) For handling process on multiple cores I created a subsmash function and used the 
functools include with functools.partial to seperate smash with length -1. I got 
the prefixes by using PREFIX + character for character in ALPHABET, and created the
pool by using multiprocessing.Pool with cores. I then used passwords with itertools.chain
with an imap of subsmashes to prefixes to seperate the process.
4.) I verified my code work by making a shell script to test my functions that runs the
code python3 -m doctest -v hulk.py. And once that worked I did the full make test and
converted my code into generator functions to finish the make test. 

Part 2
------
8 core: 170.011 U  | .264 S
6 core: 173.654 U  | .275 S
4 core: 176.432 U  | .234 S
2 core: 178.788 U  | .249 S
1 core: 182.843 U  |  .035 S 

Part 3
------
Length would make a password more complex to brute force, since every added character 
in the password would increase the number of permutations by n!, and as evidenced with 
our homework.
