
===============
 Nested Filter 
===============




—-
layout: guide
title: Nested Filter
cat: guide
sidebar: reference\_query\_dsl
—-

A ``nested`` filter, works in a similar fashion to the
`nested <nested-query.html>`_ query, except used as a filter. It follows
exactly the same structure, but also allows to cache the results (set
``_cache`` to ``true``), and have it named (set the ``_name`` value).
For example:

::

    {
        “filtered” : {
            “query” : { “match_all” : {} },
            “filter” : {
                “nested” : {
                    “path” : “obj1”,
                    “query” : {
                        “bool” : {
                            “must” : [
                                {
                                    “text” : {“obj1.name” : “blue”}
                                },
                                {
                                    “range” : {“obj1.count” : {“gt” : 5}}
                                }
                            ]
                        }
                    },
                    “_cache” : true
                }
            }
        }
    }




