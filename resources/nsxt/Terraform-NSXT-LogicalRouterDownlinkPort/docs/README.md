# Terraform::NSXT::LogicalRouterDownlinkPort

This resource provides a means to define a downlink port on a logical router to connect a logical tier1 router to a logical switch. The result of this is to provide a default gateway to virtual machines running on the logical switch.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LogicalRouterDownlinkPort",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#linkedlogicalswitchportid" title="LinkedLogicalSwitchPortId">LinkedLogicalSwitchPortId</a>" : <i>String</i>,
        "<a href="#logicalrouterid" title="LogicalRouterId">LogicalRouterId</a>" : <i>String</i>,
        "<a href="#urpfmode" title="UrpfMode">UrpfMode</a>" : <i>String</i>,
        "<a href="#servicebinding" title="ServiceBinding">ServiceBinding</a>" : <i>[ <a href="servicebinding.md">ServiceBinding</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LogicalRouterDownlinkPort
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#linkedlogicalswitchportid" title="LinkedLogicalSwitchPortId">LinkedLogicalSwitchPortId</a>: <i>String</i>
    <a href="#logicalrouterid" title="LogicalRouterId">LogicalRouterId</a>: <i>String</i>
    <a href="#urpfmode" title="UrpfMode">UrpfMode</a>: <i>String</i>
    <a href="#servicebinding" title="ServiceBinding">ServiceBinding</a>: <i>
      - <a href="servicebinding.md">ServiceBinding</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name, defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

Logical router port subnet (ip_address / prefix length).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkedLogicalSwitchPortId

Identifier for port on logical switch to connect to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalRouterId

Identifier for logical Tier-1 router on which this port is created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrpfMode

Unicast Reverse Path Forwarding mode. Accepted values are "NONE" and "STRICT" which is the default value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceBinding

_Required_: No

_Type_: List of <a href="servicebinding.md">ServiceBinding</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

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

#### MacAddress

Returns the <code>MacAddress</code> value.

#### Revision

Returns the <code>Revision</code> value.

