
=============================
 Search API – Highlighting 
=============================




—-
layout: guide
title: Search API – Highlighting
cat: guide
sidebar: reference\_api\_search
—-

Allow to highlight search results on one or more fields. The
implementation uses the either lucene ``fast-vector-highlighter`` or
``highlighter``. The search request body:

::

    {
        “query” : {...},
        “highlight” : {
            “fields” : {
                “content” : {}
            }
        }
    }

In the above case, the ``content`` field will be highlighted for each
search hit (there will be another element in each search hit, called
``highlight``, which includes the highlighted fields and the highlighted
fragments).

In order to perform highlighting, the actual content of the field is
required. If the field in question is stored (has ``store`` set to
``yes`` in the mapping), it will be used, otherwise, the actual
``_source`` will be loaded and the relevant field will be extracted from
it.

If no ``term_vector`` information is provided (by setting it to
``with_positions_offsets`` in the mapping), then the plain highlighter
will be used. If it is provided, then the fast vector highlighter will
be used. When term vectors are available, highlighting will be performed
faster at the cost of bigger index size.

Here is an example of setting the ``content`` field to allow for
highlighting on it (this will cause the index to be bigger):

::

    {
        “type_name” : {
            “content” : {“store” : “yes”, “term_vector” : “with_positions_offsets”}
        }
    }

Highlighting Tags
=================

By default, the highlighting will wrap highlighted text in ``<em>`` and
``</em>``. This can be controlled by setting ``pre_tags`` and
``post_tags``, for example:

::

    {
        “query” : {...},
        “highlight” : {
            “pre_tags” : [”“, ““],
            “post_tags” : [”“, ““],
            “fields” : {
                “_all” : {}
            }
        }
    }

There can be a single tag or more, and the “importance” is ordered.
There are also built in “tag” schemas, with currently a single schema
called ``styled`` with ``pre_tags`` of:

::

    , , ,
    , , ,
    , , ,

And post tag of ``</em>``. If you think of more nice to have built in
tag schemas, just send an email to the mailing list or open an issue.
Here is an example of switching tag schemas:

::

    {
        “query” : {...},
        “highlight” : {
            “tags_schema” : “styled”,
            “fields” : {
                “content” : {}
            }
        }
    }

Highlighted Fragments
=====================

Each field highlighted can control the size of the highlighted fragment
in characters (defaults to ``100``), and the maximum number of fragments
to return (defaults to ``5``). For example:

::

    {
        “query” : {...},
        “highlight” : {
            “fields” : {
                “content” : {“fragment_size” : 150, “number_of_fragments” : 3}
            }
        }
    }

On top of this it is possible to specify that highlighted fragments are
order by score:

::

    {
        “query” : {...},
        “highlight” : {
            “order” : “score”,
            “fields” : {
                “content” : {“fragment_size” : 150, “number_of_fragments” : 3}
            }
        }
    }

Note the score of text fragment in this case is calculated by Lucene
highlighting framework. For implementation details you can check
``ScoreOrderFragmentsBuilder.java`` class.

If the ``number_of_fragments`` value is set to 0 then no fragments are
produced, instead the whole content of the field is returned, and of
course it is highlighted. This can be very handy if short texts (like
document title or address) need to be highlighted but no fragmentation
is required. Note that ``fragment_size`` is ignored in this case.

::

    {
        “query” : {...},
        “highlight” : {
            “fields” : {
                “_all” : {},
                “bio.title” : {“number_of_fragments” : 0}
            }
        }
    }

When using ``fast-vector-highlighter`` one can use ``fragment_offset``
parameter to conrol the margin to start highlighting from.

Global Settings
===============

Highlighting settings can be set on a global level and then overridden
at the field level.

::

    {
        “query” : {...},
        “highlight” : {
            “number_of_fragments” : 3,
            “fragment_size” : 150,
            “tag_schema” : “styled”,
            “fields” : {
                “_all” : { “pre_tags” : [”“], “post_tags” : [”“] },
                “bio.title” : { “number_of_fragments” : 0 },
                “bio.author” : { “number_of_fragments” : 0 },
                “bio.content” : { “number_of_fragments” : 5, “order” : “score” }
            }
        }
    }




