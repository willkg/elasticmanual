
=============
 Analyze API 
=============




—-
layout: guide
title: Analyze API
cat: guide
sidebar: reference\_api
—-

Performs the analysis process on a text and return the tokens breakdown
of the text. Here is an example:

::

    curl -XGET 'localhost:9200/test/_analyze?text=this+is+a+test’

The above will run an analysis on the “this is a test” text, using the
default index analyzer associated with the ``test`` index. An
``analyzer`` can also be provided to use a different analyzer:

::

    curl -XGET 'localhost:9200/test/_analyze?analyzer=whitespace’ -d 'this is a test’

Also, the analyzer can be derived based on a field mapping, for example:

::

    curl -XGET 'localhost:9200/test/_analyze?field=obj1.field1’ -d 'this is a test’

Will cause the analysis to happen based on the analyzer configure in the
mapping for ``obj1.field1`` (and if not, the default index analyzer).

Also, the text can be provided as part of the request body, and not as a
parameter.

Format
------

By default, the format the tokens are returned in are in json and its
called ``detailed``. The ``text`` format value provides the analyzed
data in a text stream that is a bit more readable.



