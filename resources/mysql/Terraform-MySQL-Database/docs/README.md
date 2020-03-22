# Terraform::MySQL::Database

The ``mysql_database`` resource creates and manages a database on a MySQL
server.

~> **Caution:** The ``mysql_database`` resource can completely delete your
database just as easily as it can create it. To avoid costly accidents,
consider setting
[``prevent_destroy``](/docs/configuration/resources.html#prevent_destroy)
on your database resources as an extra safety measure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::MySQL::Database",
    "Properties" : {
        "<a href="#defaultcharacterset" title="DefaultCharacterSet">DefaultCharacterSet</a>" : <i>String</i>,
        "<a href="#defaultcollation" title="DefaultCollation">DefaultCollation</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::MySQL::Database
Properties:
    <a href="#defaultcharacterset" title="DefaultCharacterSet">DefaultCharacterSet</a>: <i>String</i>
    <a href="#defaultcollation" title="DefaultCollation">DefaultCollation</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### DefaultCharacterSet

The default character set to use when
a table is created without specifying an explicit character set. Defaults
to "utf8".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCollation

The default collation to use when a table
is created without specifying an explicit collation. Defaults to
``utf8_general_ci``. Each character set has its own set of collations, so
changing the character set requires also changing the collation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the database. This must be unique within
a given MySQL server and may or may not be case-sensitive depending on
the operating system on which the MySQL server is running.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

