
================
 Boosting Query 
================




—-
layout: guide
title: Boosting Query
cat: guide
sidebar: reference\_query\_dsl
—-

The ``boosting`` query can be used to effectively demote results that
match a given query. Unlike the “NOT” clause in bool query, this still
selects documents that contain undesirable terms, but reduces their
overall score.

::

    {
        “boosting” : {
            “positive” : {
                “term” : {
                    “field1” : “value1”
                }
            },
            “negative” : {
                “term” : {
                    “field2” : “value2”
                }
            },
            “negative_boost” : 0.2
        }
    }




