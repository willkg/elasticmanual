
==================
 Match All Filter 
==================




—-
layout: guide
title: Match All Filter
cat: guide
sidebar: reference\_query\_dsl
—-

A filter that matches on all documents:

::

    {
        “constant_score” : {
            “filter” : {
                “match_all” : { }
            }
        }
    }




