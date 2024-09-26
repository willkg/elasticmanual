
=============
 Match Query 
=============




—-
layout: guide
title: Match Query
cat: guide
sidebar: reference\_query\_dsl
—-

A family of ``match`` queries that accept text/numerics/dates, analyzes
it, and constructs a query out of it. For example:

::

    {
        “match” : {
            “message” : “this is a test”
        }
    }

Note, ``message`` is the name of a field, you can subsitute the name of
any field (including ``_all``) instead.

Types of Match Queries
----------------------

boolean
~~~~~~~

The default ``match`` query is of type ``boolean``. It means that the
text provided is analyzed and the analysis process constructs a boolean
query from the provided text. The ``operator`` flag can be set to ``or``
or ``and`` to control the boolean clauses (defaults to ``or``).

The ``analyzer`` can be set to control which analyzer will perform the
analysis process on the text. It default to the field explicit mapping
definition, or the default search analyzer.

``fuzziness`` can be set to a value (depending on the relevant type, for
string types it should be a value between ``0.0`` and ``1.0``) to
constructs fuzzy queries for each term analyzed. The ``prefix_length``
and ``max_expansions`` can be set in this case to control the fuzzy
process. If the fuzzy option is set the query will use
``constant_score_rewrite`` as its `rewrite
method <multi-term-rewrite.html>`_ the ``rewrite`` parameter allows to
control how the query will get rewritten.

Here is an example when providing additional parameters (note the slight
change in structure, ``message`` is the field name):

::

    {
        “match” : {
            “message” : {
                “query” : “this is a test”,
                “operator” : “and”
            }
        }
    }

phrase
~~~~~~

The ``match_phrase`` query analyzes the text and creates a ``phrase``
query out of the analyzed text. For example:

::

    {
        “match_phrase” : {
            “message” : “this is a test”
        }
    }

Since ``match_phrase`` is only a ``type`` of a ``match`` query, it can
also be used in the following manner:

::

    {
        “match” : {
            “message” : {
                “query” : “this is a test”,
                “type” : “phrase”
            }
        }
    }

A phrase query maintains order of the terms up to a configurable
``slop`` (which defaults to 0).

The ``analyzer`` can be set to control which analyzer will perform the
analysis process on the text. It default to the field explicit mapping
definition, or the default search analyzer, for example:

::

    {
        “match_phrase” : {
            “message” : {
                “query” : “this is a test”,
                “analyzer” : “my_analyzer”
            }
        }
    }

match\_phrase\_prefix
~~~~~~~~~~~~~~~~~~~~~

The ``match_phrase_prefix`` is the same as ``match_phrase``, except that
it allows for prefix matches on the last term in the text. For example:

::

    {
        “match_phrase_prefix” : {
            “message” : “this is a test”
        }
    }

Or:

::

    {
        “match” : {
            “message” : {
                “query” : “this is a test”,
                “type” : “phrase_prefix”
            }
        }
    }

It accepts the same parameters as the phrase type. In addition, it also
accepts a ``max_expansions`` parameter that can control to how many
prefixes the last term will be expanded. It is highly recommended to set
it to an acceptable value to control the execution time of the query.
For example:

::

    {
        “match_phrase_prefix” : {
            “message” : {
                “query” : “this is a test”,
                “max_expansions” : 10
            }
        }
    }

Comparison to query\_string / field
-----------------------------------

The match family of queries does not go through a “query parsing”
process. It does not support field name prefixes, wildcard characters,
or other “advance” features. For this reason, chances of it failing are
very small / non existent, and it provides an excellent behavior when it
comes to just analyze and run that text as a query behavior (which is
usually what a text search box does). Also, the ``phrase_prefix`` type
can provide a great “as you type” behavior to automatically load search
results.



