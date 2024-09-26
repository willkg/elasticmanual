
=============================
 Search API – Range Facets 
=============================




—-
layout: guide
title: Search API – Range Facets
cat: guide
sidebar: reference\_api\_search\_facets
—-

``range`` facet allow to specify a set of ranges and get both the number
of docs (count) that fall within each range, and aggregated data either
based on the field, or using another field. Here is a simple example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “range1” : {
                “range” : {
                    “field” : “field_name”,
                    “ranges” : [
                        { “to” : 50 },
                        { “from” : 20, “to” : 70 },
                        { “from” : 70, “to” : 120 },
                        { “from” : 150 }
                    ]
                }
            }
        }
    }

Another option which is a bit more DSL enabled is to provide the ranges
on the actual field name, for example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “range1” : {
                “range” : {
                    “my_field” : [
                        { “to” : 50 },
                        { “from” : 20, “to” : 70 },
                        { “from” : 70, “to” : 120 },
                        { “from” : 150 }
                    ]
                }
            }
        }
    }

Key and Value
=============

The ``range`` facet allow to use a different field to check if it doc
falls within a range, and another field to compute aggregated data per
range (like total). For example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “range1” : {
                “range” : {
                    “key_field” : “field_name”,
                    “value_field” : “another_field_name”,
                    “ranges” : [
                        { “to” : 50 },
                        { “from” : 20, “to” : 70 },
                        { “from” : 70, “to” : 120 },
                        { “from” : 150 }
                    ]
                }
            }
        }
    }

Script Key and Value
====================

Sometimes, some munging of both the key and the value are needed. In the
key case, before it is checked if it falls within a range, and for the
value, when the statistical data is computed per range scripts can be
used. Here is an example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “range1” : {
                “range” : {
                    “key_script” : “doc['date’].date.minuteOfHour”,
                    “value_script” : “doc['num1’].value”,
                    “ranges” : [
                        { “to” : 50 },
                        { “from” : 20, “to” : 70 },
                        { “from” : 70, “to” : 120 },
                        { “from” : 150 }
                    ]
                }
            }
        }
    }

Date Ranges
===========

The range facet support also providing the range as string formatted
dates.



