
=============
 Boost Field 
=============




—-
layout: guide
title: Boost Field
cat: guide
sidebar: reference\_mapping
—-

Boosting is the process of enhancing the relevancy of a document or
field. Field level mapping allows to define explicit boost level on a
specific field. The boost field mapping (applied on the `root
object <root-object-type.html>`_) allows to define a boost field mapping
where **its content will control the boost level of the document**. For
example, consider the following mapping:

::

    {
        “tweet” : {
            “_boost” : {“name” : “_boost”, “null_value” : 1.0}
        }
    }

The above mapping defines mapping for a field named ``_boost``. If the
``_boost`` field exists within the JSON document indexed, its value will
control the boost level of the document indexed. For example, the
following JSON document will be indexed with a boost value of ``2.2``:

::

    {
        “tweet” {
            “_boost” : 2.2,
            “message” : “This is a tweet!”
        }
    }




