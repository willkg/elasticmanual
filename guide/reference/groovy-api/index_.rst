
==================
 Index Groovy API 
==================




—-
layout: guide
title: Index Groovy API
cat: guide
sidebar: reference\_groovy\_api
—-

The index API is very similar to the `Java index
API </guide/reference/java-api/index_.html>`_. The Groovy extension to
it is the ability to provide the indexed source using a closure. For
example:

::

    def indexR = client.index {
        index “test”
        type “type1”
        id “1”
        source {
            test = “value”
            complex {
                value1 = “value1”
                value2 = “value2”
            }
        }
    }

In the above example, the source closure itself gets transformed into an
XContent (defaults to JSON). In order to change how the source closure
is serialized, a global (static) setting can be set on the ``GClient``
by changing the ``indexContentType`` field.

Note also that the ``source`` can be set using the typical Java based
APIs, the ``Closure`` option is a Groovy extension.



