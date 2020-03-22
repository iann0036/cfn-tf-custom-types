# Terraform::OVH::IpReverse

Provides a OVH IP reverse.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OVH::IpReverse",
    "Properties" : {
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#ipreverse" title="Ipreverse">Ipreverse</a>" : <i>String</i>,
        "<a href="#reverse" title="Reverse">Reverse</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OVH::IpReverse
Properties:
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#ipreverse" title="Ipreverse">Ipreverse</a>: <i>String</i>
    <a href="#reverse" title="Reverse">Reverse</a>: <i>String</i>
</pre>

## Properties

#### Ip

The IP block to which the IP belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipreverse

The IP to set the reverse of, default to `ip` if `ip` is a /32 (IPv4) or a /128 (IPv6).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reverse

The value of the reverse.

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

