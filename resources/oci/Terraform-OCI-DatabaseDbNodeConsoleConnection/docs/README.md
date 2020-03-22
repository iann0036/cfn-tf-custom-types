# Terraform::OCI::DatabaseDbNodeConsoleConnection

This resource provides the Db Node Console Connection resource in Oracle Cloud Infrastructure Database service.

Creates a new console connection to the specified dbNode.
After the console connection has been created and is available,
you connect to the console using SSH.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseDbNodeConsoleConnection",
    "Properties" : {
        "<a href="#dbnodeid" title="DbNodeId">DbNodeId</a>" : <i>String</i>,
        "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseDbNodeConsoleConnection
Properties:
    <a href="#dbnodeid" title="DbNodeId">DbNodeId</a>: <i>String</i>
    <a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DbNodeId

The database node [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

The SSH public key used to authenticate the console connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### ConnectionString

Returns the <code>ConnectionString</code> value.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

