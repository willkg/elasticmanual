
===============================
 Stemmer Override Token Filter 
===============================




—-
layout: guide
title: Stemmer Override Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

Overrides stemming algorithms, by applying a custom mapping, then
protecting these terms from being modified by stemmers. Must be placed
before any stemming filters.

Rules are separted by “=>”

+------------------+---------------------------------------------------------------------------------------+
| Setting          | Description                                                                           |
+==================+=======================================================================================+
| ``rules``        | A list of mapping rules to use.                                                       |
+------------------+---------------------------------------------------------------------------------------+
| ``rules_path``   | A path (either relative to ``config`` location, or absolute) to a list of mappings.   |
+------------------+---------------------------------------------------------------------------------------+

Here is an example:

::

    index :
        analysis :
            analyzer :·
                myAnalyzer :
                    type : custom
                    tokenizer : standard
                    filter : [lowercase, custom_stems, porterStem]    
            filter:
                custom_stems:
                    type: stemmer_override
                    rules_path : analysis/custom_stems.txt




