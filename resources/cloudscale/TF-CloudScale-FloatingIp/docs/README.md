# TF::CloudScale::FloatingIp

Provides a cloudscale.ch Floating IP to represent a publicly-accessible static IP address or IP network that can be assigned to one of your cloudscale.ch servers. Floating IPs can be moved between servers. Possible use cases include: High-availability, non-disruptive maintenance, multiple IPs per server, or re-using the same IP after replacing a server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudScale::FloatingIp",
    "Properties" : {
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>Double</i>,
        "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>,
        "<a href="#regionslug" title="RegionSlug">RegionSlug</a>" : <i>String</i>,
        "<a href="#reverseptr" title="ReversePtr">ReversePtr</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudScale::FloatingIp
Properties:
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>Double</i>
    <a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
    <a href="#regionslug" title="RegionSlug">RegionSlug</a>: <i>String</i>
    <a href="#reverseptr" title="ReversePtr">ReversePtr</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### IpVersion

`4` or `6`, for an IPv4 or IPv6 address or network respectively.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

If you want to assign an entire network instead of a single IP address to your server, you must specify the prefix length. Currently, there is only support for `ip_version=6` and `prefix_length=56`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionSlug

You can specify a region slug. Options include `lpg` and `rma`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReversePtr

You can specify the PTR record (reverse DNS pointer) in case of a single Floating IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

(Re-)Assign the Floating IP to this server (UUID).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

You can specify the type. Options include `regional` (default) and `global`.

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

#### Href

Returns the <code>Href</code> value.

#### Id

Returns the <code>Id</code> value.

#### Network

Returns the <code>Network</code> value.

#### NextHop

Returns the <code>NextHop</code> value.

