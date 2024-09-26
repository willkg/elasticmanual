
============================
 Compound Word Token Filter 
============================




—-
layout: guide
title: Compound Word Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

Token filters that allow to decompose compound words. There are two
types available: ``dictionary_decompounder`` and
``hyphenation_decompounder``.

The following are settings that can be set for a compound word token
filter type:

Setting
Description
``word_list``
A list of words to use.
``word_list_path``
A path (either relative to ``config`` location, or absolute) to a list
of words.
Here is an example:

::

    index :
        analysis :
            analyzer :·
                myAnalyzer2 :
                    type : custom
                    tokenizer : standard
                    filter : [myTokenFilter1, myTokenFilter2]
            filter :
                myTokenFilter1 :
                    type : dictionary_decompounder
                    word_list: [one, two, three]
                myTokenFilter2 :
                    type : hyphenation_decompounder
                    word_list_path: path/to/words.txt




