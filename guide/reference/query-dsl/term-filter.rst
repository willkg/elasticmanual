
=============
 Term Filter 
=============




—-
layout: guide
title: Term Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents that have fields that contain a term (**not
analyzed**). Similar to term query, except that it acts as a filter. Can
be placed within queries that accept a filter, for example:

::

    {
        “constant_score” : {
            “filter” : {
                “term” : { “user” : “kimchy”}
            }
        }
    }

Caching
=======

The result of the filter is automatically cached by default. The
\`\_cache\` can be set to \`false\` to turn it off. Here is an example:

::

    {
        “constant_score” : {
            “filter” : {
                “term” : { 
                    “user” : “kimchy”,
                    “_cache” : false
                }
            }
        }
    }




