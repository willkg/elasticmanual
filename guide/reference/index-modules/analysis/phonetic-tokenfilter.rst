
=======================
 Phonetic Token Filter 
=======================




—-
layout: guide
title: Phonetic Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A ``phonetic`` token filter that can be configured with different
``encoder`` types: ``metaphone``, ``soundex``, ``caverphone``,
``refined_soundex``, ``double_metaphone`` (uses `commons
codec <http://jakarta.apache.org/commons/codec/api-release/org/apache/commons/codec/language/package-summary.html>`_).

The ``replace`` parameter (defaults to ``true``) controls if the token
processed should be replaced with the encoded one (set it to ``true``),
or added (set it to ``false``).

For example:

::

    {
        “index” : {
            “analysis” : {
                “analyzer” : {
                    “my_analyzer” : {
                        “tokenizer” : “standard”,
                        “filter” : [“standard”, “lowercase”, “my_metaphone”]
                    }
                },
                “filter” : {
                    “my_metaphone” : {
                        “type” : “phonetic”,
                        “encoder” : “metaphone”,
                        “replace” : false
                    }
                }
            }
        }
    }




