
=================
 Custom Analyzer 
=================




—-
layout: guide
title: Custom Analyzer
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

An analyzer of type ``custom`` that allows to combine a ``Tokenizer``
with zero or more ``Token Filters``, and zero or more ``Char Filters``.
The custom analyzer accepts a logical/registered name of the tokenizer
to use, and a list of logical/registered names of token filters.

The following are settings that can be set for a ``custom`` analyzer
type:

Setting
Description
``tokenizer``
The logical / registered name of the tokenizer to use.
``filter``
An optional list of logical / registered name of token filters.
``char_filter``
An optional list of logical / registered name of char filters.
Here is an example:

::

    index :
        analysis :
            analyzer : 
                myAnalyzer2 :
                    type : custom
                    tokenizer : myTokenizer1
                    filter : [myTokenFilter1, myTokenFilter2]
                    char_filter : [my_html]
            tokenizer :
                myTokenizer1 :
                    type : standard
                    max_token_length : 900
            filter :
                myTokenFilter1 :
                    type : stop
                    stopwords : [stop1, stop2, stop3, stop4]
                myTokenFilter2 :
                    type : length
                    min : 0
                    max : 2000
            char_filter :
                  my_html :
                    type : html_strip
                    escaped_tags : [xxx, yyy]
                    read_ahead : 1024




