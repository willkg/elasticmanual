
=====================
 Mapping Char Filter 
=====================




—-
layout: guide
title: Mapping Char Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A char filter of type ``mapping`` replacing characters of an analyzed
text with given mapping.

Here is a sample configuration:

::

    {
        “index” : {
            “analysis” : {
                “char_filter” : {
                    “my_mapping” : {
                        “type” : “mapping”,
                        “mappings” : [“ph=>f”, “qu=>q”]
                    }
                },
                “analyzer” : {
                    “custom_with_char_filter” : {
                        “tokenizer” : “standard”,
                        “char_filter” : [“my_mapping”]
                    },
                }
            }
        }
    }

Otherwise the setting ``mappings_path`` can specify a file where you can
put the list of char mapping :

::

    ph => f
    qu => k




