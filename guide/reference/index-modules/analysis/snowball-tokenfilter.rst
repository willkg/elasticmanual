
=======================
 Snowball Token Filter 
=======================




—-
layout: guide
title: Snowball Token Filter
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

A filter that stems words using a Snowball-generated stemmer. The
``language`` parameter controls the stemmer with the following available
values: ``Armenian``, ``Basque``, ``Catalan``, ``Danish``, ``Dutch``,
``English``, ``Finnish``, ``French``, ``German``, ``German2``,
``Hungarian``, ``Italian``, ``Kp``, ``Lovins``, ``Norwegian``,
``Porter``, ``Portuguese``, ``Romanian``, ``Russian``, ``Spanish``,
``Swedish``, ``Turkish``.

For example:

::

    {
        “index” : {
            “analysis” : {
                “analyzer” : {
                    “my_analyzer” : {
                        “tokenizer” : “standard”,
                        “filter” : [“standard”, “lowercase”, “my_snow”]
                    }
                },
                “filter” : {
                    “my_snow” : {
                        “type” : “snowball”,
                        “language” : “Lovins”
                    }
                }
            }
        }
    }




