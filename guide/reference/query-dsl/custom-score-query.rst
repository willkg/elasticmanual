
====================
 Custom Score Query 
====================




—-
layout: guide
title: Custom Score Query
cat: guide
sidebar: reference\_query\_dsl
—-

``custom_score`` query allows to wrap another query and customize the
scoring of it optionally with a computation derived from other field
values in the doc (numeric ones) using `script
expression </guide/reference/modules/scripting.html>`_. Here is a simple
sample:

::

    “custom_score” : {
        “query” : {
            ....
        },
        “script” : “_score * doc['my_numeric_field’].value”
    }

On top of the different scripting field values and expression, the
``_score`` script parameter can be used to retrieve the score based on
the wrapped query.

Script Parameters
=================

Scripts are cached for faster execution. If the script has parameters
that it needs to take into account, it is preferable to use the same
script, and provide parameters to it:

::

    “custom_score” : {
        “query” : {
            ....
        },
        “params” : {
            “param1” : 2,
            “param2” : 3.1
        }
        “script” : “_score * doc['my_numeric_field’].value / pow(param1, param2)”
    }




