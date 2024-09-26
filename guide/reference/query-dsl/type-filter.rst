
=============
 Type Filter 
=============




—-
layout: guide
title: Type Filter
cat: guide
sidebar: reference\_query\_dsl
—-

Filters documents matching the provided document / mapping type. Note,
this filter can work even when the ``_type`` field is not indexed (using
the ``_uid`` field).

::

    {
        “type” : {
            “value” : “my_type”
        }
    }    




