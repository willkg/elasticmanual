
================
 Get Groovy API 
================




—-
layout: guide
title: Get Groovy API
cat: guide
sidebar: reference\_groovy\_api
—-

The get API is very similar to the `Java get
API </guide/reference/java-api/get.html>`_. The main benefit of using
groovy is handling the source content. It can be automatically converted
to a ``Map`` which means using Groovy to navigate it is simple:

::

    def getF = node.client.get {
        index “test”
        type “type1”
        id “1”}

        println “Result of field2: $getF.response.source.complex.field2”




