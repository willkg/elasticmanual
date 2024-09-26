
===========================
 Geo Distance Range Filter 
===========================




—-
layout: guide
title: Geo Distance Range Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents that exists within a range from a specific point:

::

    {
        “filtered” : {
            “query” : {
                “match_all” : {}
            },
            “filter” : {
                “geo_distance_range” : {
                    “from” : “200km”,
                    “to” : “400km”
                    “pin.location” : {
                        “lat” : 40,
                        “lon” : -70
                    }
                }
            }
        }
    }

Supports the same point location parameter as the ``geo_distance``
filter. And also support the common parameters for range (lt, lte, gt,
gte, from, to, include\_upper and include\_lower).



