
==========================
 Path Hierarchy Tokenizer 
==========================




—-
layout: guide
title: Path Hierarchy Tokenizer
cat: guide
sidebar: reference\_index\_modules\_analysis
—-

The ``path_hierarchy`` tokenizer takes something like this:

::

    /something/something/else

And produces tokens:

::

    /something
    /something/something
    /something/something/else

Setting
Description
``delimiter``
The character delimiter to use, defaults to ``/``.
``replacement``
An optional replacement character to use. Defaults to the ``delimiter``.
``buffer_size``
The buffer size to use, defaults to ``1024``.
``reverse``
Generates tokens in reverse order, defaults to ``false``.
``skip``
Controls initial tokens to skip, defaults to ``0``.



