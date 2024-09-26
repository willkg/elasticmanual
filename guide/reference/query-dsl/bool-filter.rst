
=============
 Bool Filter 
=============




—-
layout: guide
title: Bool Filter
cat: guide
sidebar: reference\_query\_dsl
—-

A filter that matches documents matching boolean combinations of other
queries. Similar in concept to Boolean query, except that the clauses
are other filters. Can be placed within queries that accept a filter.

::

    {
        “filtered” : {
            “query” : {
                “queryString” : { 
                    “default_field” : “message”, 
                    “query” : “elasticsearch”
                }
            },
            “filter” : {
                “bool” : {
                    “must” : {
                        “term” : { “tag” : “wow” }
                    },
                    “must_not” : {
                        “range” : {
                            “age” : { “from” : 10, “to” : 20 }
                        }
                    },
                    “should” : [
                        {
                            “term” : { “tag” : “sometag” }
                        },
                        {
                            “term” : { “tag” : “sometagtag” }
                        }
                    ]
                }
            }
        }
    }    

Caching
=======

The result of the ``bool`` filter is not cached by default (though
internal filters might be). The ``_cache`` can be set to ``true`` in
order to enable caching.



