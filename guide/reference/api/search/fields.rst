
=======================
 Search API – Fields 
=======================




—-
layout: guide
title: Search API – Fields
cat: guide
sidebar: reference\_api\_search
—-

Allows to selectively load specific fields for each document represented
by a search hit. Defaults to load the internal ``_source`` field.

::

    {
        “fields” : [“user”, “postDate”],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

The fields will automatically load stored fields (``store`` mapping set
to ``yes``), or, if not stored, will load the ``_source`` and extract it
from it (allowing to return nested document object).

``*`` can be used to load all stored fields from the document.

An empty array will cause only the ``_id`` and ``_type`` for each hit to
be returned, for example:

::

    {
        “fields” : [],
        “query” : {
            “term” : { “user” : “kimchy” }
        }
    }

Script fields can also be automatically detected and used as fields, so
things like ``_source.obj1.obj2`` can be used, though not recommended,
as ``obj1.obj2`` will work as well.



