
=================================
 Search API – Histogram Facets 
=================================




—-
layout: guide
title: Search API – Histogram Facets
cat: guide
sidebar: reference\_api\_search\_facets
—-

The histogram facet works with numeric data by building a histogram
across intervals of the field values. Each value is “rounded” into an
interval (or placed in a bucket), and statistics are provided per
interval/bucket (count and total). Here is a simple example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “histo1” : {
                “histogram” : {
                    “field” : “field_name”,
                    “interval” : 100
                }
            }
        }
    }    

The above example will run a histogram facet on the ``field_name``
filed, with an ``interval`` of ``100`` (so, for example, a value of
``1055`` will be placed within the ``1000`` bucket).

The interval can also be provided as a time based interval (using the
time format). This mainly make sense when working on date fields or
field that represent absolute milliseconds, here is an example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “histo1” : {
                “histogram” : {
                    “field” : “field_name”,
                    “time_interval” : “1.5h”
                }
            }
        }
    }    

Key and Value
=============

The histogram facet allows to use a different key and value. The key is
used to place the hit/document within the appropriate bucket, and the
value is used to compute statistical data (for example, total). Here is
an example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “histo1” : {
                “histogram” : {
                    “key_field” : “key_field_name”,
                    “value_field” : “value_field_name”,
                    “interval” : 100
                }
            }
        }
    }    

Script Key and Value
====================

Sometimes, some munging of both the key and the value are needed. In the
key case, before it is rounded into a bucket, and for the value, when
the statistical data is computed per bucket
`scripts </guide/reference/modules/scripting.html>`_ can be used. Here
is an example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “histo1” : {
                “histogram” : {
                    “key_script” : “doc['date’].date.minuteOfHour”,
                    “value_script” : “doc['num1’].value”,
                }
            }
        }
    }    

In the above sample, we can use a date type field called ``date`` to get
the minute of hour from it, and the total will be computed based on
another field ``num1``. Note, in this case, no ``interval`` was
provided, so the bucket will be based directly on the ``key_script`` (no
rounding).

Parameters can also be provided to the different scripts (preferable if
the script is the same, with different values for a specific parameter,
like “factor”):

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “histo1” : {
                “histogram” : {
                    “key_script” : “doc['date’].date.minuteOfHour * factor1”,
                    “value_script” : “doc['num1’].value + factor2”,
                    “params” : {
                        “factor1” : 2,
                        “factor2” : 3
                    }
                }
            }
        }
    }    

Memory Considerations
=====================

In order to implement the histogram facet, the relevant field values are
loaded into memory from the index. This means that per shard, there
should be enough memory to contain them. Since by default, dynamic
introduced types are ``long`` and ``double``, one option to reduce the
memory footprint is to explicitly set the types for the relevant fields
to either ``short``, ``integer``, or ``float`` when possible.



