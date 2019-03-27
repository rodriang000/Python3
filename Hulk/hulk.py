#!/usr/bin/env python3

import functools
import hashlib
import itertools
import multiprocessing
import os
import string
import sys

# Constants

ALPHABET    = string.ascii_lowercase + string.digits
ARGUMENTS   = sys.argv[1:]
CORES       = 1
HASHES      = 'hashes.txt'
LENGTH      = 1
PREFIX      = ''

# Functions

def usage(exit_code=0):
    print('''Usage: {} [-a alphabet -c CORES -l LENGTH -p PREFIX -s HASHES]
    -a ALPHABET Alphabet to use in permutations
    -c CORES    CPU Cores to use
    -l LENGTH   Length of permutations
    -p PREFIX   Prefix for all permutations
    -s HASHES   Path of hashes file'''.format(os.path.basename(sys.argv[0])))
    sys.exit(exit_code)

def sha1sum(s):
    ''' Generate sha1 digest for given string.
    >>> sha1sum('wake me up inside')
    '5bfb1100e6ef294554c1e99ff35ad11db6d7b67b'

    >>> sha1sum('baby now we got bad blood')
    '9c6d9c069682759c941a6206f08fb013c55a0a6e'
    '''
    # Conver to bytes
    sbyte = s.encode()
    hash_object = hashlib.sha1(sbyte)
    hex_dig = hash_object.hexdigest()
    return hex_dig

def permutations(length, alphabet=ALPHABET):
    ''' Recursively yield all permutations of alphabet up to provided length.

    >>> list(permutations(1, 'ab'))
    ['a', 'b']

    >>> list(permutations(2, 'ab'))
    ['aa', 'ab', 'ba', 'bb']

    >>> list(permutations(1))       # doctest: +ELLIPSIS
    ['a', 'b', ..., '9']

    >>> list(permutations(2))       # doctest: +ELLIPSIS
    ['aa', 'ab', ..., '99']

    >>> import inspect; inspect.isgeneratorfunction(permutations)
    True
    '''
    if length <= 1:
        for char in alphabet:
            yield char
    else:
        for char in alphabet:
            for perm in permutations(length - 1, alphabet):
                yield char + perm

def smash(hashes, length, alphabet=ALPHABET, prefix=''):
    ''' Return all password permutations of specified length that are in hashes

    >>> smash([sha1sum('ab')], 2)
    ['ab']

    >>> smash([sha1sum('abc')], 2, prefix='a')
    ['abc']

    >>> smash(map(sha1sum, 'abc'), 1, 'abc')
    ['a', 'b', 'c']
    '''
    return[ prefix+character for character in permutations(length, alphabet) if sha1sum(prefix+character) in hashes ]
# Main Execution

if __name__ == '__main__':
    # Parse command line
    ARGUMENT = sys.argv[1:]
    while ARGUMENT and ARGUMENT[0].startswith('-') and len(ARGUMENT[0]) > 1:
        arg = ARGUMENT.pop(0)
        if arg == '-a':
            ALPHABET = ARGUMENT.pop(0)
        elif arg == '-c':
            CORES = int(ARGUMENT.pop(0))
        elif arg == '-l':
            LENGTH = int(ARGUMENT.pop(0))
        elif arg == '-p':
            PREFIX = ARGUMENT.pop(0)
        elif arg == '-s':
            HASHES = ARGUMENT.pop(0)
        elif arg == '-h':
            usage(0)
        else:
            usage(1)

    if len(ARGUMENT) == 0:
        ARGUMENT.append('-')

    for line in ARGUMENT:
        if line == '-':
            stream = sys.stdin
        else:
            stream = open(line)
    # Load hashes set
    hashes = set(hsh.strip() for hsh in open(HASHES))
    #Execute smash function
    if CORES > 1 and LENGTH > 1:
        subsmash = functools.partial(smash,hashes,LENGTH-1, ALPHABET)
        prefixes = [PREFIX+character for character in ALPHABET ]
        pool = multiprocessing.Pool(CORES)
        passwords = itertools.chain.from_iterable(pool.imap(subsmash, prefixes))
    else:
        passwords = smash(hashes, LENGTH, ALPHABET, PREFIX)
        
    #print passwords
    for i in passwords:
        print(i)
# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
