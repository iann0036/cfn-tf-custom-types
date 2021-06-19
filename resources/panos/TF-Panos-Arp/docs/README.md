# TF::Panos::Arp

Manages ARP config attached to an interface.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::Arp",
    "Properties" : {
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfacename" title="InterfaceName">InterfaceName</a>" : <i>String</i>,
        "<a href="#interfacetype" title="InterfaceType">InterfaceType</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
        "<a href="#subinterfacename" title="SubinterfaceName">SubinterfaceName</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::Arp
Properties:
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfacename" title="InterfaceName">InterfaceName</a>: <i>String</i>
    <a href="#interfacetype" title="InterfaceType">InterfaceType</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
    <a href="#subinterfacename" title="SubinterfaceName">SubinterfaceName</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
</pre>

## Properties

#### Interface

The interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceName

The interface name (leave this empty for VLAN interfaces).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceType

The interface type.  Valid values are `ethernet` (default),
`aggregate-ethernet`, or `vlan`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

The IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

The MAC address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubinterfaceName

The subinterface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template location.

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

