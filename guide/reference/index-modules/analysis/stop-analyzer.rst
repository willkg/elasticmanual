
===============
 Stop Analyzer 
===============




—-
layout: guide
title: Stop Analyzer
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

An analyzer of type ``stop`` that is built using a `Lower Case
Tokenizer <lowercase-tokenizer.html>`_, with `Stop Token
Filter <stop-tokenfilter.html>`_.

The following are settings that can be set for a ``stop`` analyzer type:

Setting
Description
``stopwords``
A list of stopword to initialize the stop filter with. Defaults to the
english stop words.
``stopwords_path``
A path (either relative to ``config`` location, or absolute) to a
stopwords file configuration.



