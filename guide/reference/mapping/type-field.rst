
============
 Type Field 
============




—-
layout: guide
title: Type Field
cat: guide
sidebar: reference\_mapping
—-

Each document indexed is associated with an id and a type. The type,
when indexing, is automatically indexed into a ``_type`` field. By
default, the ``_type`` field is indexed (but **not** analyzed) and not
stored. This means that the ``_type`` field can be queried.

The ``_type`` field can be stored as well, for example:

::

    {
        “tweet” : {
            “_type” : {“store” : “yes”}
        }
    }

The ``_type`` field can also not be indexed, and all the APIs will still
work except for specific queries (term queries / filters) or faceting
done on the ``_type`` field.

::

    {
        “tweet” : {
            “_type” : {“index” : “no”}
        }
    }




