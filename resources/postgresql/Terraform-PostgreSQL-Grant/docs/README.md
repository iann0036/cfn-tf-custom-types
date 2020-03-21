# Terraform::PostgreSQL::Grant

The ``postgresql_grant`` resource creates and manages privileges given to a user for a database schema.

~> **Note:** This resource needs Postgresql version 9 or above.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PostgreSQL::Grant",
    "Properties" : {
        "<a href="#database" title="Database">Database</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#privileges" title="Privileges">Privileges</a>" : <i>[ String, ... ]</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PostgreSQL::Grant
Properties:
    <a href="#database" title="Database">Database</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#privileges" title="Privileges">Privileges</a>: <i>
      - String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#schema" title="Schema">Schema</a>: <i>String</i>
</pre>

## Properties

#### Database

The database to grant privileges on for this role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

The PostgreSQL object type to grant the privileges on (one of: table, sequence).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileges

The list of privileges to grant.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The name of the role to grant privileges on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

The database schema to grant privileges on for this role.

_Required_: Yes

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

