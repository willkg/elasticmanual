
===================
 Delete Groovy API 
===================




—-
layout: guide
title: Delete Groovy API
cat: guide
sidebar: reference\_groovy\_api
—-

The delete API is very similar to the `Java delete
API </guide/reference/java-api/delete.html>`_, here is an example:

::

    def deleteF = node.client.delete {
        index “test”
        type “type1”
        id “1”
    }




