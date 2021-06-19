# TF::FortiOS::FmgSystemAdminUser

This resource supports Create/Read/Update/Delete admin user for FortiManager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FmgSystemAdminUser",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#profileid" title="Profileid">Profileid</a>" : <i>String</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>String</i>,
        "<a href="#rpcpermit" title="RpcPermit">RpcPermit</a>" : <i>String</i>,
        "<a href="#trusthost1" title="Trusthost1">Trusthost1</a>" : <i>String</i>,
        "<a href="#trusthost2" title="Trusthost2">Trusthost2</a>" : <i>String</i>,
        "<a href="#trusthost3" title="Trusthost3">Trusthost3</a>" : <i>String</i>,
        "<a href="#usertype" title="UserType">UserType</a>" : <i>String</i>,
        "<a href="#userid" title="Userid">Userid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FmgSystemAdminUser
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#profileid" title="Profileid">Profileid</a>: <i>String</i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>String</i>
    <a href="#rpcpermit" title="RpcPermit">RpcPermit</a>: <i>String</i>
    <a href="#trusthost1" title="Trusthost1">Trusthost1</a>: <i>String</i>
    <a href="#trusthost2" title="Trusthost2">Trusthost2</a>: <i>String</i>
    <a href="#trusthost3" title="Trusthost3">Trusthost3</a>: <i>String</i>
    <a href="#usertype" title="UserType">UserType</a>: <i>String</i>
    <a href="#userid" title="Userid">Userid</a>: <i>String</i>
</pre>

## Properties

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profileid

Profile id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

RADIUS server name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpcPermit

Rpc permit, Enum: ["read-write", "none", "read"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost1

Admin user trusted host IP, default 0.0.0.0 0.0.0.0 for all.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost2

Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost3

Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserType

User type, Enum: ["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Userid

User name.

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

#### Id

Returns the <code>Id</code> value.

