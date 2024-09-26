
======================
 Elision Token Filter 
======================




—-
layout: guide
title: Elision Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A token filter which removes elisions. For example, “l’avion” (the
plane) will tokenized as “avion” (plane).

Accepts ``articles`` setting which is a set of stop words articles. For
example:

::

    “index” : {
        “analysis” : {
            “analyzer” : {
                “default” : {
                    “tokenizer” : “standard”,
                    “filter” : [“standard”, “elision”]
                }
            },
            “filter” : {
                “elision” : {
                    “type” : “elision”,
                    “articles” : [“l”, “m”, “t”, “qu”, “n”, “s”, “j”]
                }
            }
        }
    }




