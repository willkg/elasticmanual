
==================
 Count Groovy API 
==================




—-
layout: guide
title: Count Groovy API
cat: guide
sidebar: reference\_groovy\_api
—-

The count API is very similar to the `Java count
API </guide/reference/java-api/count.html>`_. The Groovy extension
allows to provide the query to execute as a ``Closure`` (similar to GORM
criteria builder):

::

    def count = client.count {
        indices “test”
        types “type1”
        query {
            term {
                test = “value”
            }
        }
    }

The query follows the same `Query DSL </guide/reference/query-dsl>`_.



