
=====================
 Lowercase Tokenizer 
=====================




—-
layout: guide
title: Lowercase Tokenizer
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A tokenizer of type ``lowercase`` that performs the function of `Letter
Tokenizer <letter-tokenizer.html>`_ and `Lower Case Token
Filter <lowercase-tokenfilter.html>`_ together. It divides text at
non-letters and converts them to lower case. While it is functionally
equivalent to the combination of `Letter
Tokenizer <letter-tokenizer.html>`_ and `Lower Case Token
Filter <lowercase-tokenizer.html>`_, there is a performance advantage to
doing the two tasks at once, hence this (redundant) implementation.



