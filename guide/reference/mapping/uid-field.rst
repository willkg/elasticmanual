
===========
 UID Field 
===========




—-
layout: guide
title: UID Field
cat: guide
sidebar: reference\_mapping
—-

Each document indexed is associated with an id and a type, the internal
``_uid`` field is the unique identifier of a document within an index
and is composed of the type and the id (meaning that different types can
have the same id and still maintain uniqueness).

The ``_uid`` field is automatically used when ``_type`` is not indexed
to perform type based filtering, and does not require the ``_id`` to be
indexed.



