
==============
 Query Filter 
==============




—-
layout: guide
title: Query Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Wraps any query to be used as a filter. Can be placed within queries
that accept a filter.

::

    {
        “constantScore” : {
            “filter” : {
                “query” : { 
                    “query_string” : { 
                        “query” : “this AND that OR thus”
                    }
                }
            }
        }
    }

Caching
=======

The result of the filter is not cached by default. The \`\_cache\` can
be set to \`true\` to cache the **result** of the filter. This is handy
when the same query is used on several (many) other queries. Note, the
process of caching the first execution is higher when not caching (since
it needs to satisfy different queries).

Setting the \`\_cache\` element requires a different format for the
\`query\`:

::

    {
        “constantScore” : {
            “filter” : {
                “fquery” : {
                    “query” : { 
                        “query_string” : { 
                            “query” : “this AND that OR thus”
                        }
                    },
                    “_cache” : true
                }
            }
        }
    }




