
============
 Array Type 
============




—-
layout: guide
title: Array Type
cat: guide
sidebar: reference\_mapping
—-

JSON documents allow to define an array (list) of fields or objects.
Mapping array types could not be simpler since arrays gets automatically
detected and mapping them can be done either with `Core
Types <core-types.html>`_ or `Object Type <object-type.html>`_ mappings.
For example, the following JSON defines several arrays:

::

    {
        “tweet” : {
            “message” : “some arrays in this tweet…”,
            “tags” : [“elasticsearch”, “wow”],
            “lists” : [
                {
                    “name” : “prog_list”,
                    “description” : “programming list”
                },
                {
                    “name” : “cool_list”,
                    “description” : “cool stuff list”
                }
            ]
        }
    }

The above JSON has the ``tags`` property defining a list of a simple
``string`` type, and the ``lists`` property is an ``object`` type array.
Here is a sample explicit mapping:

::

    {
        “tweet” : {
            “properties” : {
                “message” : {“type” : “string”},
                “tags” : {“type” : “string”, “index_name” : “tag”},
                “lists” : {
                    “properties” : {
                        “name” : {“type” : “string”}, 
                        “description” : {“type” : “string”}
                    }
                }
            }
        }
    }

The fact that array types are automatically support can be shown by the
fact that the following JSON document is perfectly fine:

::

    {
        “tweet” : {
            “message” : “some arrays in this tweet…”,
            “tags” : “elasticsearch”,
            “lists” : {
                “name” : “prog_list”,
                “description” : “programming list”
            }
        }
    }

Note also, that thanks to the fact that we used the ``index_name`` to
use the non plural form (``tag`` instead of ``tags``), we can actually
refer to the field using the ``index_name`` as well. For example, we can
execute a query using ``tweet.tags:wow`` or ``tweet.tag:wow``. We could,
of course, name the field as ``tag`` and skip the ``index_name`` all
together).



