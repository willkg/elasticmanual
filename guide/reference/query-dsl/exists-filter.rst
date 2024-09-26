
===============
 Exists Filter 
===============




—-
layout: guide
title: Exists Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents where a specific field has a value in them.

::

    {
        “constant_score” : {
            “filter” : {
                “exists” : { “field” : “user” }
            }
        }
    }

Caching
=======

The result of the filter is always cached.



