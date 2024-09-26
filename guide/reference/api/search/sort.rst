
=====================
 Search API – Sort 
=====================




—-
layout: guide
title: Search API – Sort
cat: guide
sidebar: reference\_api\_search
—-

Allows to add one or more sort on specific fields. Each sort can be
reversed as well. The sort is defined on a per field level, with special
field name for ``_score`` to sort by score.

::

    {
        “sort” : [
            { “post_date” : {“order” : “asc”} },
            “user”,
            { “name” : “desc” },
            { “age” : “desc” },
            “_score”
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

If the JSON parser support ordering without an array, the sort request
can also be structured as follows:

::

    {
        “sort” : {
            { “post_date” : {“order” : “asc”} },
            “user” : { },
            “_score” : { }
        },
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Sort Values
===========

The sort values for each document returned are also returned as part of
the response.

Missing Values
==============

Numeric fields support specific handling for missing fields in a doc.
The ``missing`` value can be ``_last``, ``_first``, or a custom value
(that will be used for missing docs as the sort value). For example:

::

    {
        “sort” : [
            { “price” : {“missing” : “_last”} },
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Geo Distance Sorting
====================

Allow to sort by ``_geo_distance``. Here is an example:

::

    {
        “sort” : [
            {
                “_geo_distance” : {
                    “pin.location” : [-70, 40],
                    “order” : “asc”,
                    “unit” : “km”
                }
            }
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

The following formats are supported in providing the coordinates:

Lat Lon as Properties
---------------------

::

    {
        “sort” : [
            {
                “_geo_distance” : {
                    “pin.location” : {
                        “lat” : 40,
                        “lon”, -70
                    }
                    “order” : “asc”,
                    “unit” : “km”
                }
            }
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Lat Lon as String
-----------------

Format in ``lat,lon``.

::

    {
        “sort” : [
            {
                “_geo_distance” : {
                    “pin.location” : “-70,40”,
                    “order” : “asc”,
                    “unit” : “km”
                }
            }
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Geohash
-------

::

    {
        “sort” : [
            {
                “_geo_distance” : {
                    “pin.location” : “drm3btev3e86”,
                    “order” : “asc”,
                    “unit” : “km”
                }
            }
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Lat Lon as Array
----------------

Format in ``[lon, lat]``, note, the order of lon/lat here in order to
conform with `GeoJSON <http://geojson.org/>`_.

::

    {
        “sort” : [
            {
                “_geo_distance” : {
                    “pin.location” : [-70, 40],
                    “order” : “asc”,
                    “unit” : “km”
                }
            }
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Script Based Sorting
====================

Allow to sort based on custom scripts, here is an example:

::

    {
        “query” : {
            ....
        },
        “sort” : {
            “_script” : { 
                “script” : “doc['field_name’].value * factor”,
                “type” : “number”,
                “params” : {
                    “factor” : 1.1
                },
                “order” : “asc”
            }
        }
    }

Note, it is recommended, for single custom based script based sorting,
to use ``custom_score`` query instead as sorting based on score is
faster.

Track Scores
============

When sorting on a field, scores are not computed. By setting
``track_scores`` to true, scores will still be computed and tracked.

::

    {
        “track_scores”: true,
        “sort” : [
            { “post_date” : {“reverse” : true} },
            { “name” : “desc” },
            { “age” : “desc” }
        ],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Memory Considerations
=====================

When sorting, the relevant sorted field values are loaded into memory.
This means that per shard, there should be enough memory to contain
them. For string based types, the field sorted on should not be analyzed
/ tokenized. For numeric types, if possible, it is recommended to
explicitly set the type to six\_hun types (like ``short``, ``integer``
and ``float``).



