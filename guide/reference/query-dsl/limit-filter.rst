
==============
 Limit Filter 
==============




—-
layout: guide
title: Limit Filter
cat: guide
sidebar: reference\_query\_dsl
—-

A limit filter limits the number of documents (per shard) to execute on.
For example:

::

    {
        “filtered” : {
            “filter” : {
                 “limit” : {“value” : 100}
             },
             “query” : {
                “term” : { “name.first” : “shay” }
            }
        }
    }




