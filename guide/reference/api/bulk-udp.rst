
==============
 Bulk UDP API 
==============




—-
layout: guide
title: Bulk UDP API
cat: guide
sidebar: reference\_api
—-

A Bulk UDP service is a service listening over UDP for bulk format
requests. The idea is to provide a low latency UDP service that allows
to easily index data that is not of critical nature.

The Bulk UDP service is disabled by default, but can be enabled by
setting ``bulk.udp.enabled`` to ``true``.

The bulk UDP service performs internal bulk aggregation of the data and
then flushes it based on several parameters:

-  ``bulk.udp.bulk_actions``: The number of actions to flush a bulk
   after, defaults to ``1000``.
-  ``bulk.udp.bulk_size``: The size of the current bulk request to flush
   the request once exceeded, defaults to ``5mb``.
-  ``bulk.udp.flush_interval``: An interval after which the current
   request is flushed, regardless of the above limits. Defaults to
   ``5s``.
-  ``bulk.udp.concurrent_requests``: The number on max in flight bulk
   requests allowed. Defaults to ``4``.

The network settings allowed are:

-  ``bulk.udp.host``: The host to bind to, defaults to ``network.host``
   which defaults to any.
-  ``bulk.udp.port``: The port to use, defaults to ``9700-9800``.
-  ``bulk.udp.receive_buffer_size``: The receive buffer size, defaults
   to ``10mb``.

Here is an example of how it can be used:

::

    > cat bulk.txt
    { “index” : { “_index” : “test”, “_type” : “type1” } }
    { “field1” : “value1” }
    { “index” : { “_index” : “test”, “_type” : “type1” } }
    { “field1” : “value1” }

::

    > cat bulk.txt | nc -w 0 -u localhost 9700




