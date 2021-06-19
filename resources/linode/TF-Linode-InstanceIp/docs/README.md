# TF::Linode::InstanceIp

~> **NOTICE:** You may need to contact support to increase your instance IP limit before you can allocate additional IPs.

Manages a Linode instance IP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Linode::InstanceIp",
    "Properties" : {
        "<a href="#linodeid" title="LinodeId">LinodeId</a>" : <i>Double</i>,
        "<a href="#public" title="Public">Public</a>" : <i>Boolean</i>,
        "<a href="#rdns" title="Rdns">Rdns</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Linode::InstanceIp
Properties:
    <a href="#linodeid" title="LinodeId">LinodeId</a>: <i>Double</i>
    <a href="#public" title="Public">Public</a>: <i>Boolean</i>
    <a href="#rdns" title="Rdns">Rdns</a>: <i>String</i>
</pre>

## Properties

#### LinodeId

The ID of the Linode to allocate an IPv4 address for.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Public

Whether the IPv4 address is public or private. Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rdns

The reverse DNS assigned to this address.

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

#### Address

Returns the <code>Address</code> value.

#### Gateway

Returns the <code>Gateway</code> value.

#### Id

Returns the <code>Id</code> value.

#### Prefix

Returns the <code>Prefix</code> value.

#### Region

Returns the <code>Region</code> value.

#### SubnetMask

Returns the <code>SubnetMask</code> value.

#### Type

Returns the <code>Type</code> value.

