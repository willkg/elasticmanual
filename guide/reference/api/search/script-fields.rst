
==============================
 Search API – Script Fields 
==============================




—-
layout: guide
title: Search API – Script Fields
cat: guide
sidebar: reference\_api\_search
—-

Allows to return a `script
evaluation </guide/reference/modules/scripting.html>`_ (based on
different fields) for each hit, for example:

::

    {
        “query” : {
            ...
        },
        “script_fields” : {
            “test1” : {
                “script” : “doc['my_field_name’].value * 2”
            },
            “test2” : {
                “script” : “doc['my_field_name’].value * factor”,
                “params” : {
                    “factor”  : 2.0
                }
            }
        }
    }

Script fields can work on fields that are not store (``my_field_name``
in the above case), and allow to return custom values to be returned
(the evaluated value of the script).

Script fields can also access the actual ``_source`` document indexed
and extract specific elements to be returned from it (can be an “object”
type). Here is an example:

::

        {
            “query” : {
                ...
            },
            “script_fields” : {
                “test1” : {
                    “script” : “_source.obj1.obj2” 
                }
            }
        }

Note the ``_source`` keyword here to navigate the json like model.

Its important to understand the difference between
``doc['my_field'].value`` and ``_source.my_field``. The first, using the
doc keyword, will cause the terms for that field to be loaded to memory
(cached), which will result in faster execution, but more memory
consumption. Also, the ``doc[...]`` notation only allows for simple
valued fields (can’t return a json object from it) and make sense only
on non analyzed or single term based fields.

The ``_source`` on the other hand causes the source to be loaded,
parsed, and then only the relevant part of the json is returned.



