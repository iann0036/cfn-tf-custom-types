# TF::FortiOS::SwitchcontrollerVlan

Configure VLANs for switch controller. Applies to FortiOS Version `<= 6.2.0`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerVlan",
    "Properties" : {
        "<a href="#auth" title="Auth">Auth</a>" : <i>String</i>,
        "<a href="#color" title="Color">Color</a>" : <i>Double</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#portalmessageoverridegroup" title="PortalMessageOverrideGroup">PortalMessageOverrideGroup</a>" : <i>String</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>String</i>,
        "<a href="#security" title="Security">Security</a>" : <i>String</i>,
        "<a href="#usergroup" title="Usergroup">Usergroup</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vlanid" title="Vlanid">Vlanid</a>" : <i>Double</i>,
        "<a href="#portalmessageoverrides" title="PortalMessageOverrides">PortalMessageOverrides</a>" : <i>[ <a href="portalmessageoverridesdefinition.md">PortalMessageOverridesDefinition</a>, ... ]</i>,
        "<a href="#selectedusergroups" title="SelectedUsergroups">SelectedUsergroups</a>" : <i>[ <a href="selectedusergroupsdefinition.md">SelectedUsergroupsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerVlan
Properties:
    <a href="#auth" title="Auth">Auth</a>: <i>String</i>
    <a href="#color" title="Color">Color</a>: <i>Double</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#portalmessageoverridegroup" title="PortalMessageOverrideGroup">PortalMessageOverrideGroup</a>: <i>String</i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>String</i>
    <a href="#security" title="Security">Security</a>: <i>String</i>
    <a href="#usergroup" title="Usergroup">Usergroup</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vlanid" title="Vlanid">Vlanid</a>: <i>Double</i>
    <a href="#portalmessageoverrides" title="PortalMessageOverrides">PortalMessageOverrides</a>: <i>
      - <a href="portalmessageoverridesdefinition.md">PortalMessageOverridesDefinition</a></i>
    <a href="#selectedusergroups" title="SelectedUsergroups">SelectedUsergroups</a>: <i>
      - <a href="selectedusergroupsdefinition.md">SelectedUsergroupsDefinition</a></i>
</pre>

## Properties

#### Auth

Authentication. Valid values: `radius`, `usergroup`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of icon on the GUI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Switch VLAN name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalMessageOverrideGroup

Specify captive portal replacement message override group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

Authentication radius server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Security

Security. Valid values: `open`, `captive-portal`, `8021x`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usergroup

Authentication usergroup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

Virtual domain,.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlanid

VLAN ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalMessageOverrides

_Required_: No

_Type_: List of <a href="portalmessageoverridesdefinition.md">PortalMessageOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedUsergroups

_Required_: No

_Type_: List of <a href="selectedusergroupsdefinition.md">SelectedUsergroupsDefinition</a>

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

