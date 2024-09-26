
===========
 Query DSL 
===========




—-
layout: guide
title: Query DSL
cat: guide
sidebar: reference\_query\_dsl
—-

**elasticsearch** provides a full Query DSL based on JSON to define
queries. In general, there are basic queries such as
`term <term-query.html>`_ or `prefix <prefix-query.html>`_. There are
also compound queries like the `bool <bool-query.html>`_ query. Queries
can also have filters associated with them such as the
`filtered <filtered-query.html>`_ or
`constant\_score <constant-score-query.html>`_ queries, with specific
filter queries.

Think of the Query DSL as an AST of queries. Certain queries can contain
other queries (like the `bool <bool-query.html>`_ query), other can
contain filters (like the
`constant\_score <constant-score-query.html>`_), and some can contain
both a query and a filter (like the `filtered <filtered-query.html>`_).
Each of those can contain **any** query of the list of queries or
**any** filter from the list of filters, resulting in the ability to
build quite complex (and interesting) queries.

Both queries and filters can be used in different APIs. For example,
within a `search query </guide/reference/api/search/query.html>`_, or as
a `facet filter </guide/reference/api/search/facets/>`_. This section
explains the components (queries and filters) that can form the AST one
can use.

Filters are very handy since they perform an order of magnitude better
then plain queries since no scoring is performed and they are
automatically cached.

Filters and Caching
===================

Filters can be a great candidate for caching. Caching the result of a
filter does not require a lot of memory, and will cause other queries
executing against the same filter (same parameters) to be blazingly
fast.

Some filters already produce a result that is easily cacheable, and the
difference between caching and not caching them is the act of placing
the result in the cache or not. These filters, which include the
`term <term-filter.html>`_, `terms <terms-filter.html>`_,
`prefix <prefix-filter.html>`_, and `range <range-filter.html>`_
filters, are by default cached and are recommended to use (compared to
the equivalent query version) when the same filter (same parameters)
will be used across multiple different queries (for example, a range
filter with age higher than 10).

Other filters, usually already working with the field data loaded into
memory, are not cached by default. Those filters are already very fast,
and the process of caching them requires extra processing in order to
allow the filter result to be used with different queries than the one
executed. These filters, including the geo,
`numeric\_range <numeric-range-filter.html>`_, and
`script <script-filter.html>`_ filters are not cached by default.

The last type of filters are those working with other filters. The
`and <and-filter.html>`_, `not <not-filter.html>`_ and
`or <or-filter.html>`_ filters are not cached as they basically just
manipulate the internal filters.

All filters allow to set ``_cache`` element on them to explicitly
control caching. They also allow to set ``_cache_key`` which will be
used as the caching key for that filter. This can be handy when using
very large filters (like a terms filter with many elements in it).



