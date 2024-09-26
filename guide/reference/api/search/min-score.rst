
===========================
 Search API – min\_score 
===========================




—-
layout: guide
title: Search API – min\_score
cat: guide
sidebar: reference\_api\_search
—-

Allows to filter out documents based on a minimum score:

::

    {
        “min_score”: 0.5,
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Note, most times, this does not make much sense, but is provided for
advance use cases.



