
===================
 Glossary of terms 
===================




—-
layout: glossary
title: Glossary of terms
cat: guide
glossary: – id: analysis text: > Analysis is the process of converting
`full text <#text>`_ to `terms <#term>`_. Depending on which analyzer is
used, these phrases: “@FOO BAR@”, “@Foo-Bar@”, “@foo,bar@” will probably
all result in the terms “@foo@” and “@bar@”. These terms are what is
actually stored in the index.

A full text query (not a `term <#term>`_ query) for “@FoO:bAR@” will
also be analyzed to the terms “@foo@”,”@bar@” and will thus match the
terms stored in the index. It is this process of analysis (both at index
time and at search time) that allows elasticsearch to perform full text
queries. Also see `text <#text>`_ and `term <#term>`_. – id: cluster
text: > A cluster consists of one or more `nodes <#node>`_ which share
the same cluster name. Each cluster has a single master node which is
chosen automatically by the cluster and which can be replaced if the
current master node fails.

- id: document text: > A document is a JSON document which is stored in
elasticsearch. It is like a row in a table in a relational database.
Each document is stored in an `index <#index>`_ and has a
`type <#type>`_ and an `id <#id>`_.

A document is a JSON object (also known in other languages as a hash /
hashmap / associative array) which contains zero or more
`fields <#field>`_, or key-value pairs. The original JSON document that
is indexed will be stored in the `@\_source@ field <#source_field>`_,
which is returned by default when getting or searching for a document.

- id: id text: > The ID of a `document <#document>`_ identifies a
document. The ``index/type/id`` of a document must be unique. If no ID
is provided, then it will be auto-generated. (also see
`routing <#routing>`_)

- id: field text: > A `document <#document>`_ contains a list of fields,
or key-value pairs. The value can be a simple (scalar) value (eg a
string, integer, date), or a nested structure like an array or an
object. A field is similar to a column in a table in a relational
database.

The `mapping <#mapping>`_ for each field has a field 'type’ (not to be
confused with document `type <#type>`_) which indicates the type of data
that can be stored in that field, eg ``integer``, ``string``,
``object``. The mapping also allows you to define (amongst other things)
how the value for a field should be analyzed.

- id: index text: > An index is like a 'database’ in a relational
database. It has a `mapping <#mapping>`_ which defines multiple
`types <#type>`_.

An index is a logical namespace which maps to one or more `primary
shards <#primary_shard>`_ and can have zero or more `replica
shards <#replica>`_.

- id: mapping text: > A mapping is like a 'schema definition’ in a
relational database. Each `index <#index>`_ has a mapping, which defines
each `type <#type>`_ within the index, plus a number of index-wide
settings.

A mapping can either be defined explicitly, or it will be generated
automatically when a document is indexed. – id: node text: > A node is a
running instance of elasticsearch which belongs to a
`cluster <#cluster>`_. Multiple nodes can be started on a single server
for testing purposes, but usually you should have one node per server.
At startup, a node will use unicast (or multicast, if specified) to
discover an existing cluster with the same cluster name and will try to
join that cluster.

- id: primary shard text: > Each document is stored in a single primary
`shard <#shard>`_. When you index a document, it is indexed first on the
primary shard, then on all `replicas <#replica_shard>`_ of the primary
shard.

By default, an `index <#index>`_ has 5 primary shards. You can specify
fewer or more primary shards to scale the number of
`documents <#document>`_ that your index can handle. You cannot change
the number of primary shards in an index, once the index is created. See
also `routing <#routing>`_

- id: replica shard text: > Each `primary shard <#primary_shard>`_ can
have zero or more replicas. A replica is a copy of the primary shard,
and has two purposes:

# increase failover: a replica shard can be promoted to a primary shard
if the primary fails # increase performance: get and search requests can
be handled by primary or replica shards. By default, each primary shard
has one replica, but the number of replicas can be changed dynamically
on an existing index. A replica shard will never be started on the same
node as its primary shard.

- id: routing text: > When you index a document, it is stored on a
single `primary shard <#primary_shard>`_. That shard is chosen by
hashing the ``routing`` value. By default, the ``routing`` value is
derived from the ID of the document or, if the document has a specified
parent document, from the ID of the parent document (to ensure that
child and parent documents are stored on the same shard).

This value can be overridden by specifying a ``routing`` value at index
time, or a `routing
field </guide/reference/mapping/routing-field.html>`_ in the
`mapping <#mapping>`_.

- id: shard text: > A shard is a single Lucene instance. It is a
low-level “worker” unit which is managed automatically by elasticsearch.
An index is a logical namespace which points to
`primary <#primary_shard>`_ and `replica <#replica_shard>`_ shards.

Other than defining the number of primary and replica shards that an
index should have, you never need to refer to shards directly. Instead,
your code should deal only with an index. Elasticsearch distributes
shards amongst all `nodes <#node>`_ in the `cluster <#cluster>`_, and
can be move shards automatically from one node to another in the case of
node failure, or the addition of new nodes.

- id: source field text: > By default, the JSON document that you index
will be stored in the ``_source`` field and will be returned by all get
and search requests. This allows you access to the original object
directly from search results, rather than requiring a second step to
retrieve the object from an ID.

Note: the exact JSON string that you indexed will be returned to you,
even if it contains invalid JSON. The contents of this field do not
indicate anything about how the data in the object has been indexed. –
id: term text: > A term is an exact value that is indexed in
elasticsearch. The terms ``foo``, ``Foo``, @FOO are NOT equivalent.
Terms (ie exact values) can be searched for using 'term’ queries. See
also `text <#text>`_ and `analysis <#analysis>`_. – id: text text: >
Text (or full text) is ordinary unstructured text, such as this
paragraph. By default, text will by `analyzed <analysis>`_ into
`terms <#term>`_, which is what is actually stored in the index. Text
`fields <#field>`_ need to be analyzed at index time in order to be
searchable as full text, and keywords in full text queries must be
analyzed at search time to produce (and search for) the same terms that
were generated at index time. See also `term <#term>`_ and
`analysis <#analysis>`_. – id: type text: > A type is like a 'table’ in
a relational database. Each type has a list of `fields <#field>`_ that
can be specified for `documents <#document>`_ of that type. The
`mapping <#mapping>`_ defines how each field in the document is
analyzed.

—-



