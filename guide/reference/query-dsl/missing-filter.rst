
================
 Missing Filter 
================




—-
layout: guide
title: Missing Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents where a specific field has no value in them.

::

    {
        “constant_score” : {
            “filter” : {
                “missing” : { “field” : “user” }
            }
        }
    }

Caching
=======

The result of the filter is always cached.



