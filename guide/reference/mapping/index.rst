
=========
 Mapping 
=========




—-
layout: guide
title: Mapping
cat: guide
sidebar: reference\_mapping
—-

Mapping is the process of defining how a document should be mapped to
the Search Engine, including its searchable characteristics such as
which fields are searchable and if/how they are tokenized. In
ElasticSearch, an index may store documents of different “mapping
types”. ElasticSearch allows one to associate multiple mapping
definitions for each mapping type.

Explicit mapping is defined on an index/type level. By default, there
isn’t a need to define an explicit mapping, since one is automatically
created and registered when a new type or new field is introduced (with
no performance overhead) and have sensible defaults. Only when the
defaults need to be overridden must a mapping definition be provided.

Mapping Types
-------------

Mapping types are a way to try and divide the documents indexed into the
same index into logical groups. Think of it as tables in a database.
Though there is separation between types, its not a full separation (all
end up as a document within the same Lucene index).

Field names with the same name across types are highly recommended to
have the same type and same mapping characteristics (analysis settings
for example). There is an effort to allow to explicitly “choose” which
field to use by using type prefix (``my_type.my_field``), but its not
complete, and there are places where it will never work (like faceting
on the field).

In practice though, this restriction is almost never an issue. The field
name usually ends up being a good indication to its “typeness” (e.g.
“first\_name” will always be a string). Note also, that this does not
apply to the cross index case.

Mapping API
-----------

To create a mapping, you will need the `Put Mapping
API </guide/reference/api/admin-indices-put-mapping.html>`_, or you can
add multiple mappings when you `create an
index </guide/reference/api/admin-indices-create-index.html>`_.



