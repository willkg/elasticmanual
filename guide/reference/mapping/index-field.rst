
=============
 Index Field 
=============




—-
layout: guide
title: Index Field
cat: guide
sidebar: reference\_mapping
—-

The ability to store in a document the index it belongs to. By default
it is disabled, in order to enable it, the following mapping should be
defined:

::

    {
        “tweet” : {
            “_index” : { “enabled” : true }
        }
    }




