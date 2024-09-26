
============
 Status API 
============




—-
layout: guide
title: Status API
cat: guide
sidebar: reference\_api
—-

The indices status API allows to get a comprehensive status information
of one or more indices.

::

    curl -XGET 'http://localhost:9200/twitter/_status’

In order to see the recovery status of shards, pass ``recovery`` flag
and set it to ``true``. For snapshot status, pass the ``snapshot`` flag
and set it to ``true``.

Multi Index
===========

The status API can be applied to more than one index with a single call,
or even on ``_all`` the indices.

::

    curl -XGET 'http://localhost:9200/kimchy,elasticsearch/_status’

        curl -XGET 'http://localhost:9200/_status’




