
==========================
 Porter Stem Token Filter 
==========================




—-
layout: guide
title: Porter Stem Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A token filter of type ``porterStem`` that transforms the token stream
as per the Porter stemming algorithm.

Note, the input to the stemming filter must already be in lower case, so
you will need to use `Lower Case Token
Filter <lowercase-tokenfilter.html>`_ or `Lower Case
Tokenizer <lowercase-tokenizer.html>`_ farther down the Tokenizer chain
in order for this to work properly!. For example, when using custom
analyzer, make sure the ``lowercase`` filter comes before the
``porterStem`` filter in the list of filters.



