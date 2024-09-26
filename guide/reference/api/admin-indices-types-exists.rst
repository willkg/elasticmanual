
==================
 Types Exists API 
==================




—-
layout: guide
title: Types Exists API
cat: guide
sidebar: reference\_api
—-

Used to check if a type/types exists in an index/indices (available
since 0.20).

::

    curl -XHEAD 'http://localhost:9200/twitter/tweet’

The HTTP status code indicates if it exists or not. A ``404`` means its
not found, and ``200`` means its there.



