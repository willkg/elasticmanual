
===============
 Script Filter 
===============




—-
layout: guide
title: Script Filter
cat: guide
sidebar: reference\_query\_dsl
—-

A filter allowing to define
`scripts </guide/reference/modules/scripting.html>`_ as filters. For
example:

::

    “filtered” : {
        “query” : {
            ...
        }, 
        “filter” : {
            “script” : {
                “script” : “doc['num1’].value > 1”
            }
        }
    }

Custom Parameters
=================

Scripts are compiled and cached for faster execution. If the same script
can be used, just with different parameters provider, it is preferable
to use the ability to pass parameters to the script itself, for example:

::

    “filtered” : {
        “query” : {
            ...
        }, 
        “filter” : {
            “script” : {
                “script” : “doc['num1’].value > param1”
                “params” : {
                    “param1” : 5
                }
            }
        }
    }

Caching
=======

The result of the filter is not cached by default. The \`\_cache\` can
be set to \`true\` to cache the **result** of the filter. This is handy
when the same script and parameters are used on several (many) other
queries. Note, the process of caching the first execution is higher when
caching (since it needs to satisfy different queries).



