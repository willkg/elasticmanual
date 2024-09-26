
=================
 Match All Query 
=================




—-
layout: guide
title: Match All Query
cat: guide
sidebar: reference\_query\_dsl
—-

A query that matches all documents. Maps to Lucene
``MatchAllDocsQuery``.

::

    {
        “match_all” : { }
    }

Which can also have boost associated with it:

::

    {
        “match_all” : { “boost” : 1.2 }
    }

Index Time Boost
----------------

When indexing, a boost value can either be associated on the document
level, or per field. The match all query does not take boosting into
account by default. In order to take boosting into account, the
``norms_field`` needs to be provided in order to explicitly specify
which field the boosting will be done on (Note, this will result in
slower execution time). For example:

::

    {
        “match_all” : { “norms_field” : “my_field” }
    }




