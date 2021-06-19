# TF::FortiOS::FirewallObjectVip

Provides a resource to configure firewall virtual IPs (VIPs) of FortiOS.

!> **Warning:** The resource will be deprecated and replaced by new resource `fortios_firewall_vip`, we recommend that you use the new resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallObjectVip",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#extintf" title="Extintf">Extintf</a>" : <i>String</i>,
        "<a href="#extip" title="Extip">Extip</a>" : <i>String</i>,
        "<a href="#extport" title="Extport">Extport</a>" : <i>String</i>,
        "<a href="#mappedip" title="Mappedip">Mappedip</a>" : <i>[ String, ... ]</i>,
        "<a href="#mappedport" title="Mappedport">Mappedport</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#portforward" title="Portforward">Portforward</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallObjectVip
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#extintf" title="Extintf">Extintf</a>: <i>String</i>
    <a href="#extip" title="Extip">Extip</a>: <i>String</i>
    <a href="#extport" title="Extport">Extport</a>: <i>String</i>
    <a href="#mappedip" title="Mappedip">Mappedip</a>: <i>
      - String</i>
    <a href="#mappedport" title="Mappedport">Mappedport</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#portforward" title="Portforward">Portforward</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extintf

Interface connected to the source network that receives the packets that will be forwarded to the destination network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extip

IP address or address range on the external interface that you want to map to an address or address range on the
destination network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extport

Incoming port number range that you want to map to a port number range on the destination network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mappedip

IP address or address range on the destination network to which the external IP address is mapped.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mappedport

Port number range on the destination network to which the external port number range is mapped.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Virtual IP name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portforward

Enable/disable port forwarding.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol to use when forwarding packets.

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

#### Id

Returns the <code>Id</code> value.

