
==============================
 Search API – Named Filters 
==============================




—-
layout: guide
title: Search API – Named Filters
cat: guide
sidebar: reference\_api\_search
—-

Each filter can accept a \_name in its top level definition, for
example:

::

    {
        “filtered” : {
            “query” : {
                “term” : { “name.first” : “shay” }
            },
            “filter” : {
                “terms” : {
                    “name.last” : [“banon”, “kimchy”],
                    “_name” : “test”
                }
            }
        }
    }

The search response will include for each hit the ``matched_filters`` it
matched on (note, this feature make sense for ``or`` / ``bool``
filters).

Note, the query filter had to be enhanced in order to support this. In
order to set a name, the ``fquery`` filter should be used, which wraps a
query (just so there will be a place to set a name for it), for example:

::

    {
        “filtered” : {
            “query” : {
                “term” : { “name.first” : “shay” }
            },
            “filter” : {
                “fquery” : {
                    “query” : {
                        “term” : { “name.last” : “banon” }
                    },
                    “_name” : “test”
                }
            }
        }
    }




