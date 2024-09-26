
====================
 Groovy API Anatomy 
====================




—-
layout: guide
title: Groovy API Anatomy
cat: guide
sidebar: reference\_groovy\_api
—-

Once a `GClient <client.html>`_ has been obtained, all of ElasticSearch
APIs can be executed on it. Each Groovy API is exposed using three
different mechanisms.

Closure Request
===============

The first type is to simply provide the request as a Closure, which
automatically gets resolved into the respective request instance (for
the index API, its the ``IndexRequest`` class). The API returns a
special future, called ``GActionFuture``. This is a groovier version of
elasticsearch Java ``ActionFuture`` (in turn a nicer extension to Java
own ``Future``) which allows to register listeners (closures) on it for
success and failures, as well as blocking for the response. For example:

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
        }}

        println “Indexed $indexR.response.id into $indexR.response.index/$indexR.response.type”

In the above example, calling ``indexR.response`` will simply block for
the response. We can also block for the response for a specific timeout:

::

    IndexResponse response = indexR.response “5s” // block for 5 seconds, same as:
    response = indexR.response 5, TimeValue.SECONDS //    

We can also register closures that will be called on success and on
failure:

::

    indexR.success = {IndexResponse response ->
        pritnln “Indexed $response.id into $response.index/$response.type”
    }
    indexR.failure = {Throwable t ->
        println “Failed to index: $t.message”
    }

Request
=======

This option allows to pass the actual instance of the request (instead
of a closure) as a parameter. The rest is similar to the closure as a
parameter option (the ``GActionFuture`` handling). For example:

::

    def indexR = client.index (new IndexRequest(
            index: “test”,
            type: “type1”,
            id: “1”,
            source: {
                test = “value”
                complex {
                    value1 = “value1”
                    value2 = “value2”
                }
            }))

        println “Indexed $indexR.response.id into $indexR.response.index/$indexR.response.type”

Java Like
=========

The last option is to provide an actual instance of the API request, and
an ``ActionListener`` for the callback. This is exactly like the Java
API with the added ``gexecute`` which returns the ``GActionFuture``:

::

    def indexR = node.client.prepareIndex(“test”, “type1”, “1”).setSource({
        test = “value”
        complex {
            value1 = “value1”
            value2 = “value2”
        }
    }).gexecute()




