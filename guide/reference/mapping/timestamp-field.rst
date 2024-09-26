
=================
 Timestamp Field 
=================




—-
layout: guide
title: Timestamp Field
cat: guide
sidebar: reference\_mapping
—-

The ``_timestamp`` field allows to automatically index the timestamp of
a document. It can be provided externally via the index request or in
the ``_source``. If it is not provided externally it will be
automatically set to the date the document was processed by the indexing
chain.

enabled
=======

By default it is disabled, in order to enable it, the following mapping
should be defined:

::

    {
        “tweet” : {
            “_timestamp” : { “enabled” : true }
        }
    }

store / index
=============

By default the ``_timestamp`` field has ``store`` set to ``no`` and
``index`` set to ``not_analyzed``. It can be queried as a standard date
field.

path
====

The ``_timestamp`` value can be provided as an external value when
indexing. But, it can also be automatically extracted from the document
to index based on a ``path``. For example, having the following mapping:

::

    {
        “tweet” : {
            “_timestamp” : {
                “enabled” : true,
                “path” : “post_date”
            }
        }
    }

Will cause ``2009-11-15T14:12:12`` to be used as the timestamp value
for:

::

    {
        “message” : “You know, for Search”,
        “post_date” : “2009-11-15T14:12:12”
        }
    }

Note, using ``path`` without explicit timestamp value provided require
an additional (though quite fast) parsing phase.

format
======

You can define the `date format <date-format.html>`_ used to parse the
provided timestamp value. For example:

::

    {
        “tweet” : {
            “_timestamp” : {
                “enabled” : true,
                “path” : “post_date”,
                “format” : “YYYY-MM-dd”
            }
        }
    }

Note, the default format is ``dateOptionalTime``. The timestamp value
will first be parsed as a number and if it fails the format will be
tried.



