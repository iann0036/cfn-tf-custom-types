# Terraform::DigitalOcean::DatabaseConnectionPool

Provides a DigitalOcean database connection pool resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::DatabaseConnectionPool",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::DatabaseConnectionPool
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#dbname" title="DbName">DbName</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### ClusterId

The ID of the source database cluster. Note: This must be a PostgreSQL cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

The database for use with the connection pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The PGBouncer transaction mode for the connection pool. The allowed values are session, transaction, and statement.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for the database connection pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The desired size of the PGBouncer connection pool.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The name of the database user for use with the connection pool.

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

#### Host

Returns the <code>Host</code> value.

#### Id

Returns the <code>Id</code> value.

#### Password

Returns the <code>Password</code> value.

#### Port

Returns the <code>Port</code> value.

#### PrivateHost

Returns the <code>PrivateHost</code> value.

#### PrivateUri

Returns the <code>PrivateUri</code> value.

#### Uri

Returns the <code>Uri</code> value.

