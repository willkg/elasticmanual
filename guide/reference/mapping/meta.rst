
======
 Meta 
======




—-
layout: guide
title: Meta
cat: guide
sidebar: reference\_mapping
—-

Each mapping can have custom meta data associated with it. These are
simple storage elements that are simply persisted along with the mapping
and can be retrieved when fetching the mapping definition. The meta is
defined under the ``_meta`` element, for example:

::

    {
        “tweet” : {
            “_meta” : {
                “attr1” : “value1”,
                “attr2” : {
                    “attr3” : “value3”
                }
            }
        }
    }

Meta can be handy for example for client libraries that perform
serialization and deserialization to store its meta model (for example,
the class the document maps to).



