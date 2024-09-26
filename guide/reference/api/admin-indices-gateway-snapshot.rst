
======================
 Gateway Snapshot API 
======================




—-
layout: guide
title: Gateway Snapshot API
cat: guide
sidebar: reference\_api
—-

The gateway snapshot API allows to explicitly perform a snapshot through
the gateway of one or more indices (backup them). By default, each index
gateway periodically snapshot changes, though it can be disabled and be
controlled completely through this API.

Note, this API only applies when using shared storage gateway
implementation, and does not apply when using the (default) local
gateway.

::

    $ curl -XPOST 'http://localhost:9200/twitter/_gateway/snapshot’

Multi Index
===========

The gateway snapshot API can be applied to more than one index with a
single call, or even on ``_all`` the indices.

::

    $ curl -XPOST 'http://localhost:9200/kimchy,elasticsearch/_gateway/snapshot’

        $ curl -XPOST 'http://localhost:9200/_gateway/snapshot’




