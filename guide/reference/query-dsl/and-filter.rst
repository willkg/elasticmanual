
============
 And Filter 
============




—-
layout: guide
title: And Filter
cat: guide
sidebar: reference\_query\_dsl
—-

A filter that matches documents using ``AND`` boolean operator on other
queries. This filter is more performant then `bool <bool-filter.html>`_
filter. Can be placed within queries that accept a filter.

::

    {
        “filtered” : {
            “query” : {
                “term” : { “name.first” : “shay” }
            },
            “filter” : {
                “and” : [
                    {
                        “range” : { 
                            “postDate” : { 
                                “from” : “2010-03-01”,
                                “to” : “2010-04-01”
                            }
                        }
                    },
                    {
                        “prefix” : { “name.second” : “ba” }
                    }
                ]
            }
        }
    }

Caching
=======

The result of the filter is not cached by default. The \`\_cache\` can
be set to \`true\` in order to cache it (tough usually not needed).
Since the ``_cache`` element requires to be set on the ``and`` filter
itself, the structure then changes a bit to have the filters provided
within a ``filters`` element:

::

    {
        “filtered” : {
            “query” : {
                “term” : { “name.first” : “shay” }
            },
            “filter” : {
                “and” : 
                    “filters”: [
                        {
                            “range” : { 
                                “postDate” : { 
                                    “from” : “2010-03-01”,
                                    “to” : “2010-04-01”
                                }
                            }
                        },
                        {
                            “prefix” : { “name.second” : “ba” }
                        }
                    ],
                    “_cache” : true
                }
            }
        }
    }




