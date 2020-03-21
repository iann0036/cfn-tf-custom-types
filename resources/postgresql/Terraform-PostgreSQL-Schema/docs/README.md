# Terraform::PostgreSQL::Schema

The ``postgresql_schema`` resource creates and manages [schema
objects](https://www.postgresql.org/docs/current/static/ddl-schemas.html) within
a PostgreSQL database.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PostgreSQL::Schema",
    "Properties" : {
        "<a href="#database" title="Database">Database</a>" : <i>String</i>,
        "<a href="#dropcascade" title="DropCascade">DropCascade</a>" : <i>Boolean</i>,
        "<a href="#ifnotexists" title="IfNotExists">IfNotExists</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policy.md">Policy</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PostgreSQL::Schema
Properties:
    <a href="#database" title="Database">Database</a>: <i>String</i>
    <a href="#dropcascade" title="DropCascade">DropCascade</a>: <i>Boolean</i>
    <a href="#ifnotexists" title="IfNotExists">IfNotExists</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policy.md">Policy</a></i>
</pre>

## Properties

#### Database

The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropCascade

When true, will also drop all the objects that are contained in the schema. (Default: false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IfNotExists

When true, use the existing schema if it exists. (Default: true).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

The ROLE who owns the schema.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: List of <a href="policy.md">Policy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

