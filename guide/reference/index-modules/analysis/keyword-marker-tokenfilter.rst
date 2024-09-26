
=============================
 Keyword Marker Token Filter 
=============================




—-
layout: guide
title: Keyword Marker Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

Protects words from being modified by stemmers. Must be placed before
any stemming filters.

+---------------------+------------------------------------------------------------------------------------+
| Setting             | Description                                                                        |
+=====================+====================================================================================+
| ``keywords``        | A list of words to use.                                                            |
+---------------------+------------------------------------------------------------------------------------+
| ``keywords_path``   | A path (either relative to ``config`` location, or absolute) to a list of words.   |
+---------------------+------------------------------------------------------------------------------------+
| ``ignore_case``     | Set to ``true`` to lower case all words first. Defaults to ``false``.              |
+---------------------+------------------------------------------------------------------------------------+

Here is an example:

::

    index :
        analysis :
            analyzer :·
                myAnalyzer :
                    type : custom
                    tokenizer : standard
                    filter : [lowercase, protwods, porterStem]    
                protwods:
                    type: keyword_marker
                    keywords_path : analysis/protwords.txt




