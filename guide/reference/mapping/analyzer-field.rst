
================
 Analyzer Field 
================




—-
layout: guide
title: Analyzer Field
cat: guide
sidebar: reference\_mapping
—-

The ``_analyzer`` mapping allows to use a document field property as the
name of the analyzer that will be used to index the document. The
analyzer will be used for any field that does not explicitly defines an
``analyzer`` or ``index_analyzer`` when indexing.

Here is a simple mapping:

::

    {
        “type1” : {
            “_analyzer” : {
                “path” : “my_field”
            }
        }
    }

The above will use the value of the ``my_field`` to lookup an analyzer
registered under it. For example, indexing a the following doc:

::

    {
        “my_field” : “whitespace”
    }

Will cause the ``whitespace`` analyzer to be used as the index analyzer
for all fields without explicit analyzer setting.

The default path value is ``_analyzer``, so the analyzer can be driven
for a specific document by setting ``_analyzer`` field in it. If custom
json field name is needed, an explicit mapping with a different path
should be set.

By default, the ``_analyzer`` field is indexed, it can be disabled by
settings ``index`` to ``no`` in the mapping.



