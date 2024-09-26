
============
 Size Field 
============




—-
layout: guide
title: Size Field
cat: guide
sidebar: reference\_mapping
—-

The ``_size`` field allows to automatically index the size of the
original ``_source`` indexed (not the compressed size, if compressed).
By default, its disabled. In order to enable it, set the mapping to:

::

    {
        “tweet” : {
            “_size” : {“enabled” : true}
        }
    }

In order to also store it, use:

::

    {
        “tweet” : {
            “_size” : {“enabled” : true, “store” : “yes”}
        }
    }




