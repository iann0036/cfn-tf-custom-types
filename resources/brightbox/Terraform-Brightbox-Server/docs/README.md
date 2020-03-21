# Terraform::Brightbox::Server

Provides a Brightbox Server resource. This can be used to create,
modify, and delete Servers. Servers also support
[provisioning](/docs/provisioners/index.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Brightbox::Server",
    "Properties" : {
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servergroups" title="ServerGroups">ServerGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#userdatabase64" title="UserDataBase64">UserDataBase64</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Brightbox::Server
Properties:
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servergroups" title="ServerGroups">ServerGroups</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#userdatabase64" title="UserDataBase64">UserDataBase64</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Image

The Server image ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Server name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroups

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The handle of the server type required (`1gb.ssd`, etc).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDataBase64

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The handle of the zone required (`gb1-a`, `gb1-b`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fqdn

Returns the <code>Fqdn</code> value.

#### Hostname

Returns the <code>Hostname</code> value.

#### Interface

Returns the <code>Interface</code> value.

#### Ipv4Address

Returns the <code>Ipv4Address</code> value.

#### Ipv4AddressPrivate

Returns the <code>Ipv4AddressPrivate</code> value.

#### Ipv6Address

Returns the <code>Ipv6Address</code> value.

#### Ipv6Hostname

Returns the <code>Ipv6Hostname</code> value.

#### Locked

Returns the <code>Locked</code> value.

#### PublicHostname

Returns the <code>PublicHostname</code> value.

#### Status

Returns the <code>Status</code> value.

#### Username

Returns the <code>Username</code> value.

