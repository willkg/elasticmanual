
============================
 Search API – Index Boost 
============================




—-
layout: guide
title: Search API – Index Boost
cat: guide
sidebar: reference\_api\_search
—-

Allows to configure different boost level per index when searching
across more than one indices. This is very handy when hits coming from
one index matter more than hits coming from another index (think social
graph where each user has an index).

::

    {
        “indices_boost” : {
            “index1” : 1.4,
            “index2” : 1.3
        }
    }




