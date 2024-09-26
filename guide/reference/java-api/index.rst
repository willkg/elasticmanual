
==========
 Java API 
==========




—-
layout: guide
title: Java API
cat: guide
sidebar: reference\_java\_api
—-

This section describes the Java API that elasticsearch provides. All
elasticsearch operations are executed using a `Client <client.html>`_
object. All operations are completely asynchronous in nature (either
accepts a listener, or return a future).

Additionally, operations on a client may be accumulated and executed in
`Bulk <bulk.html>`_.

Note, all the `APIs </guide/reference/api>`_ are exposed through the
Java API (actually, the Java API is used internally to execute them).

Maven Repository
----------------

elasticsearch is hosted on `Sonatype <http://www.sonatype.org/>`_, with
both a `releases
repo <http://oss.sonatype.org/content/repositories/releases/>`_ and a
`snapshots
repo <http://oss.sonatype.org/content/repositories/snapshots>`_.



