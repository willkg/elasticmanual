
==================================
 Search API – Statistical Facet 
==================================




—-
layout: guide
title: Search API – Statistical Facet
cat: guide
sidebar: reference\_api\_search\_facets
—-

Statistical facet allows to compute statistical data on a numeric
fields. The statistical data include count, total, sum of squares, mean
(average), minimum, maximum, variance, and standard deviation. Here is
an example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “stat1” : {
                “statistical” : {
                    “field” : “num1”
                }
            }
        }
    }    

Script field
============

When using ``field``, the numeric value of the field is used to compute
the statistical information. Sometimes, several fields values represent
the statistics we want to compute, or some sort of mathematical
evaluation. The script field allows to define a
`script </guide/reference/modules/scripting.html>`_ to evaluate, with
its value used to compute the statistical information. For example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “stat1” : {
                “statistical” : {
                    “script” : “doc['num1’].value + doc['num2’].value”
                }
            }
        }
    }    

Parameters can also be provided to the different scripts (preferable if
the script is the same, with different values for a specific parameter,
like “factor”):

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “stat1” : {
                “statistical” : {
                    “script” : “(doc['num1’].value + doc['num2’].value) * factor”,
                    “params” : {
                        “factor” : 5
                    }
                }
            }
        }
    }    

Multi Field
===========

The statistical facet can be executed against more than one field,
returning the aggregation result across those fields. For example:

::

    {
        “query” : {
            “match_all” : {}
        },
        “facets” : {
            “stat1” : {
                “statistical” : {
                    “fields” : [“num1”, “num2”]
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



