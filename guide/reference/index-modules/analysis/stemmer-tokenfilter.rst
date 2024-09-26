
======================
 Stemmer Token Filter 
======================




—-
layout: guide
title: Stemmer Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A filter that stems words (similar to ``snowball``, but with more
options). The ``language``/@name@ parameter controls the stemmer with
the following available values:

armenian, basque, catalan, danish, dutch, english, finnish, french,
german, german2, greek, hungarian, italian, kp, lovins, norwegian,
porter, porter2, portuguese, romanian, russian, spanish, swedish,
turkish, minimal\_english, possessive\_english, light\_finish,
light\_french, minimal\_french, light\_german, minimal\_german, hindi,
light\_hungarian, indonesian, light\_italian, light\_portuguese,
minimal\_portuguese, portuguese, light\_russian, light\_spanish,
light\_swedish.

For example:

::

    {
        “index” : {
            “analysis” : {
                “analyzer” : {
                    “my_analyzer” : {
                        “tokenizer” : “standard”,
                        “filter” : [“standard”, “lowercase”, “my_stemmer”]
                    }
                },
                “filter” : {
                    “my_stemmer” : {
                        “type” : “stemmer”,
                        “name” : “light_german”
                    }
                }
            }
        }
    }




