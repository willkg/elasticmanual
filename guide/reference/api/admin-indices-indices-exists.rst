
====================
 Indices Exists API 
====================




—-
layout: guide
title: Indices Exists API
cat: guide
sidebar: reference\_api
—-

Used to check if the index (indices) exists or not. For example:

::

    curl -XHEAD 'http://localhost:9200/twitter’

The HTTP status code indicates if it exists or not. A ``404`` means its
not found, and ``200`` means its there.



