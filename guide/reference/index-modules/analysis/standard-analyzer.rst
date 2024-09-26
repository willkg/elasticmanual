
===================
 Standard Analyzer 
===================




—-
layout: guide
title: Standard Analyzer
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

An analyzer of type ``standard`` that is built of using `Standard
Tokenizer <standard-tokenizer.html>`_, with `Standard Token
Filter <standard-tokenfilter.html>`_, `Lower Case Token
Filter <lowercase-tokenfilter.html>`_, and `Stop Token
Filter <stop-tokenfilter.html>`_.

The following are settings that can be set for a ``standard`` analyzer
type:

Setting
Description
``stopwords``
A list of stopword to initialize the stop filter with. Defaults to the
english stop words.
``max_token_length``
The maximum token length. If a token is seen that exceeds this length
then it is discarded. Defaults to ``255``.



