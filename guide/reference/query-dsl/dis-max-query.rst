
===============
 Dis Max Query 
===============




—-
layout: guide
title: Dis Max Query
cat: guide
sidebar: reference\_query\_dsl
—-

A query that generates the union of documents produced by its
subqueries, and that scores each document with the maximum score for
that document as produced by any subquery, plus a tie breaking increment
for any additional matching subqueries.

This is useful when searching for a word in multiple fields with
different boost factors (so that the fields cannot be combined
equivalently into a single search field). We want the primary score to
be the one associated with the highest boost, not the sum of the field
scores (as Boolean Query would give). If the query is “albino elephant”
this ensures that “albino” matching one field and “elephant” matching
another gets a higher score than “albino” matching both fields. To get
this result, use both Boolean Query and DisjunctionMax Query: for each
term a DisjunctionMaxQuery searches for it in each field, while the set
of these DisjunctionMaxQuery’s is combined into a BooleanQuery.

The tie breaker capability allows results that include the same term in
multiple fields to be judged better than results that include this term
in only the best of those multiple fields, without confusing this with
the better case of two different terms in the multiple fields.The
default ``tie_breaker`` is ``0.0``.

This query maps to Lucene ``DisjunctionMaxQuery``.

::

    {
        “dis_max” : {
            “tie_breaker” : 0.7,
            “boost” : 1.2,
            “queries” : [
                {
                    “term” : { “age” : 34 }
                },
                {
                    “term” : { “age” : 35 }
                }
            ]
        }
    }    




