
======================
 Numeric Range Filter 
======================




—-
layout: guide
title: Numeric Range Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents with fields that have values within a certain numeric
range. Similar to range filter, except that it works only with numeric
values, and the filter execution works differently.

::

    {
        “constant_score” : {
            “filter” : {
                “numeric_range” : {
                    “age” : { 
                        “from” : “10”, 
                        “to” : “20”, 
                        “include_lower” : true, 
                        “include_upper” : false
                    }
                }
            }
        }
    }

The numeric range filter works by loading all the relevant field values
into memory, and checking for the relevant docs if they satisfy the
range requirements. This require more memory since the numeric range
data are loaded to memory, but can provide a significant increase in
performance. Note, if the relevant field values have already been loaded
to memory, for example because it was used in facets or was sorted on,
then this filter should be used.

The ``numeric_range`` filter top level parameters include:

Name
Description
``from``
The lower bound. Defaults to start from the first.
``to``
The upper bound. Defaults to unbounded.
``from_inclusive``
Should the first from (if set) be inclusive or not. Defaults to ``true``
``to_inclusive``
Should the last to (if set) be inclusive or not. Defaults to ``true``.
``gt``
Same as setting ``from`` and ``from_inclusive`` to ``false``.
``gte``
Same as setting ``from`` and ``from_inclusive`` to ``true``.
``lt``
Same as setting ``to`` and ``to_inclusive`` to ``false``.
``lte``
Same as setting ``to`` and ``to_inclusive`` to ``true``.
Caching
=======

The result of the filter is not cached by default. The ``_cache`` can be
set to ``true`` to cache the **result** of the filter. This is handy
when the same points parameters are used on several (many) other
queries. Note, the process of caching the first execution is higher when
caching (since it needs to satisfy different queries).

If caching the **result** of the filter is desired (for example, using
the same “teen” filter with ages between 10 and 20), then it is
advisable to simply use the `range <range-filter.html>`_ filter.



