
============================
 Search API – From / Size 
============================




—-
layout: guide
title: Search API – From / Size
cat: guide
sidebar: reference\_api\_search
—-

Though can be set as request parameters, they can also be set within the
search body. ``from`` defaults to ``0``, and ``size`` defaults to
``10``.

::

    {
        “from” : 0, “size” : 10,
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }




