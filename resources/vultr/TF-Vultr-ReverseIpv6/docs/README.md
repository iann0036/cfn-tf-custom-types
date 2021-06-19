# TF::Vultr::ReverseIpv6

Provides a Vultr Reverse IPv6 resource. This can be used to create, read,
modify, and delete reverse DNS records for IPv6 addresses. Upon success, DNS
changes may take 6-12 hours to become active.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::ReverseIpv6",
    "Properties" : {
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#reverse" title="Reverse">Reverse</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::ReverseIpv6
Properties:
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#reverse" title="Reverse">Reverse</a>: <i>String</i>
</pre>

## Properties

#### InstanceId

The ID of the server you want to set an IPv6
reverse DNS record for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

The IPv6 address used in the reverse DNS record.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reverse

The hostname used in the IPv6 reverse DNS record.

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

