# TF::NSXT::VlanLogicalSwitch

This resource provides a method to create vlan logical switch in NSX. Virtual machines can then be connected to the appropriate logical switch for the desired topology and network connectivity.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::VlanLogicalSwitch",
    "Properties" : {
        "<a href="#adminstate" title="AdminState">AdminState</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#ippoolid" title="IpPoolId">IpPoolId</a>" : <i>String</i>,
        "<a href="#macpoolid" title="MacPoolId">MacPoolId</a>" : <i>String</i>,
        "<a href="#transportzoneid" title="TransportZoneId">TransportZoneId</a>" : <i>String</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>Double</i>,
        "<a href="#addressbinding" title="AddressBinding">AddressBinding</a>" : <i>[ <a href="addressbindingdefinition.md">AddressBindingDefinition</a>, ... ]</i>,
        "<a href="#switchingprofileid" title="SwitchingProfileId">SwitchingProfileId</a>" : <i>[ <a href="switchingprofileiddefinition.md">SwitchingProfileIdDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::VlanLogicalSwitch
Properties:
    <a href="#adminstate" title="AdminState">AdminState</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#ippoolid" title="IpPoolId">IpPoolId</a>: <i>String</i>
    <a href="#macpoolid" title="MacPoolId">MacPoolId</a>: <i>String</i>
    <a href="#transportzoneid" title="TransportZoneId">TransportZoneId</a>: <i>String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>Double</i>
    <a href="#addressbinding" title="AddressBinding">AddressBinding</a>: <i>
      - <a href="addressbindingdefinition.md">AddressBindingDefinition</a></i>
    <a href="#switchingprofileid" title="SwitchingProfileId">SwitchingProfileId</a>: <i>
      - <a href="switchingprofileiddefinition.md">SwitchingProfileIdDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### AdminState

Admin state for the logical switch. Accepted values - 'UP' or 'DOWN'. The default value is 'UP'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### IpPoolId

Ip Pool ID to be associated with the logical switch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacPoolId

Mac Pool ID to be associated with the logical switch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransportZoneId

Transport Zone ID for the logical switch.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

Vlan for the logical switch.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressBinding

_Required_: No

_Type_: List of <a href="addressbindingdefinition.md">AddressBindingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingProfileId

_Required_: No

_Type_: List of <a href="switchingprofileiddefinition.md">SwitchingProfileIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Revision

Returns the <code>Revision</code> value.

