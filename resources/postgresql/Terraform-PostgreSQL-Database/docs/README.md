# Terraform::PostgreSQL::Database

The ``postgresql_database`` resource creates and manages [database
objects](https://www.postgresql.org/docs/current/static/managing-databases.html)
within a PostgreSQL server instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PostgreSQL::Database",
    "Properties" : {
        "<a href="#allowconnections" title="AllowConnections">AllowConnections</a>" : <i>Boolean</i>,
        "<a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>" : <i>Double</i>,
        "<a href="#encoding" title="Encoding">Encoding</a>" : <i>String</i>,
        "<a href="#istemplate" title="IsTemplate">IsTemplate</a>" : <i>Boolean</i>,
        "<a href="#lccollate" title="LcCollate">LcCollate</a>" : <i>String</i>,
        "<a href="#lcctype" title="LcCtype">LcCtype</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#tablespacename" title="TablespaceName">TablespaceName</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PostgreSQL::Database
Properties:
    <a href="#allowconnections" title="AllowConnections">AllowConnections</a>: <i>Boolean</i>
    <a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>: <i>Double</i>
    <a href="#encoding" title="Encoding">Encoding</a>: <i>String</i>
    <a href="#istemplate" title="IsTemplate">IsTemplate</a>: <i>Boolean</i>
    <a href="#lccollate" title="LcCollate">LcCollate</a>: <i>String</i>
    <a href="#lcctype" title="LcCtype">LcCtype</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#tablespacename" title="TablespaceName">TablespaceName</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
</pre>

## Properties

#### AllowConnections

If `false` then no one can connect to this
database. The default is `true`, allowing connections (except as restricted by
other mechanisms, such as `GRANT` or `REVOKE CONNECT`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionLimit

How many concurrent connections can be
established to this database. `-1` (the default) means no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encoding

Character set encoding to use in the database.
Specify a string constant (e.g. `UTF8` or `SQL_ASCII`), or an integer encoding
number.  If unset or set to an empty string the default encoding is set to
`UTF8`.  If set to `DEFAULT` Terraform will use the same encoding as the
template database.  Changing this value will force the creation of a new
resource as this value can only be changed when a database is created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsTemplate

If `true`, then this database can be cloned by any
user with `CREATEDB` privileges; if `false` (the default), then only
superusers or the owner of the database can clone it.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LcCollate

Collation order (`LC_COLLATE`) to use in the
database.  This affects the sort order applied to strings, e.g. in queries
with `ORDER BY`, as well as the order used in indexes on text columns. If
unset or set to an empty string the default collation is set to `C`.  If set
to `DEFAULT` Terraform will use the same collation order as the specified
`template` database.  Changing this value will force the creation of a new
resource as this value can only be changed when a database is created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LcCtype

Character classification (`LC_CTYPE`) to use in the
database. This affects the categorization of characters, e.g. lower, upper and
digit. If unset or set to an empty string the default character classification
is set to `C`.  If set to `DEFAULT` Terraform will use the character
classification of the specified `template` database.  Changing this value will
force the creation of a new resource as this value can only be changed when a
database is created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the database. Must be unique on the PostgreSQL
server instance where it is configured.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

The role name of the user who will own the database, or
`DEFAULT` to use the default (namely, the user executing the command). To
create a database owned by another role or to change the owner of an existing
database, you must be a direct or indirect member of the specified role, or
the username in the provider is a superuser.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TablespaceName

The name of the tablespace that will be
associated with the database, or `DEFAULT` to use the template database's
tablespace.  This tablespace will be the default tablespace used for objects
created in this database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The name of the template database from which to create
the database, or `DEFAULT` to use the default template (`template0`).  NOTE:
the default in Terraform is `template0`, not `template1`.  Changing this value
will force the creation of a new resource as this value can only be changed
when a database is created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

