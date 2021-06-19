# TF::FortiOS::Switchcontrollersecuritypolicy8021X

Configure 802.1x MAC Authentication Bypass (MAB) policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Switchcontrollersecuritypolicy8021X",
    "Properties" : {
        "<a href="#authfailvlan" title="AuthFailVlan">AuthFailVlan</a>" : <i>String</i>,
        "<a href="#authfailvlanid" title="AuthFailVlanId">AuthFailVlanId</a>" : <i>String</i>,
        "<a href="#authfailvlanid" title="AuthFailVlanid">AuthFailVlanid</a>" : <i>Double</i>,
        "<a href="#authservertimeoutperiod" title="AuthserverTimeoutPeriod">AuthserverTimeoutPeriod</a>" : <i>Double</i>,
        "<a href="#authservertimeoutvlan" title="AuthserverTimeoutVlan">AuthserverTimeoutVlan</a>" : <i>String</i>,
        "<a href="#authservertimeoutvlanid" title="AuthserverTimeoutVlanid">AuthserverTimeoutVlanid</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#eapautountaggedvlans" title="EapAutoUntaggedVlans">EapAutoUntaggedVlans</a>" : <i>String</i>,
        "<a href="#eappassthru" title="EapPassthru">EapPassthru</a>" : <i>String</i>,
        "<a href="#framevidapply" title="FramevidApply">FramevidApply</a>" : <i>String</i>,
        "<a href="#guestauthdelay" title="GuestAuthDelay">GuestAuthDelay</a>" : <i>Double</i>,
        "<a href="#guestvlan" title="GuestVlan">GuestVlan</a>" : <i>String</i>,
        "<a href="#guestvlanid" title="GuestVlanId">GuestVlanId</a>" : <i>String</i>,
        "<a href="#guestvlanid" title="GuestVlanid">GuestVlanid</a>" : <i>Double</i>,
        "<a href="#macauthbypass" title="MacAuthBypass">MacAuthBypass</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#openauth" title="OpenAuth">OpenAuth</a>" : <i>String</i>,
        "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>,
        "<a href="#radiustimeoutoverwrite" title="RadiusTimeoutOverwrite">RadiusTimeoutOverwrite</a>" : <i>String</i>,
        "<a href="#securitymode" title="SecurityMode">SecurityMode</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#usergroup" title="UserGroup">UserGroup</a>" : <i>[ <a href="usergroupdefinition.md">UserGroupDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Switchcontrollersecuritypolicy8021X
Properties:
    <a href="#authfailvlan" title="AuthFailVlan">AuthFailVlan</a>: <i>String</i>
    <a href="#authfailvlanid" title="AuthFailVlanId">AuthFailVlanId</a>: <i>String</i>
    <a href="#authfailvlanid" title="AuthFailVlanid">AuthFailVlanid</a>: <i>Double</i>
    <a href="#authservertimeoutperiod" title="AuthserverTimeoutPeriod">AuthserverTimeoutPeriod</a>: <i>Double</i>
    <a href="#authservertimeoutvlan" title="AuthserverTimeoutVlan">AuthserverTimeoutVlan</a>: <i>String</i>
    <a href="#authservertimeoutvlanid" title="AuthserverTimeoutVlanid">AuthserverTimeoutVlanid</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#eapautountaggedvlans" title="EapAutoUntaggedVlans">EapAutoUntaggedVlans</a>: <i>String</i>
    <a href="#eappassthru" title="EapPassthru">EapPassthru</a>: <i>String</i>
    <a href="#framevidapply" title="FramevidApply">FramevidApply</a>: <i>String</i>
    <a href="#guestauthdelay" title="GuestAuthDelay">GuestAuthDelay</a>: <i>Double</i>
    <a href="#guestvlan" title="GuestVlan">GuestVlan</a>: <i>String</i>
    <a href="#guestvlanid" title="GuestVlanId">GuestVlanId</a>: <i>String</i>
    <a href="#guestvlanid" title="GuestVlanid">GuestVlanid</a>: <i>Double</i>
    <a href="#macauthbypass" title="MacAuthBypass">MacAuthBypass</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#openauth" title="OpenAuth">OpenAuth</a>: <i>String</i>
    <a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
    <a href="#radiustimeoutoverwrite" title="RadiusTimeoutOverwrite">RadiusTimeoutOverwrite</a>: <i>String</i>
    <a href="#securitymode" title="SecurityMode">SecurityMode</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#usergroup" title="UserGroup">UserGroup</a>: <i>
      - <a href="usergroupdefinition.md">UserGroupDefinition</a></i>
</pre>

## Properties

#### AuthFailVlan

Enable to allow limited access to clients that cannot authenticate. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFailVlanId

VLAN ID on which authentication failed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFailVlanid

VLAN ID on which authentication failed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthserverTimeoutPeriod

Authentication server timeout period (3 - 15 sec, default = 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthserverTimeoutVlan

Enable/disable the authentication server timeout VLAN to allow limited access when RADIUS is unavailable.  Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthserverTimeoutVlanid

Authentication server timeout VLAN name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapAutoUntaggedVlans

Enable/disable automatic inclusion of untagged VLANs. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapPassthru

Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FramevidApply

Enable/disable the capability to apply the EAP/MAB frame VLAN to the port native VLAN. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAuthDelay

Guest authentication delay (1 - 900  sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestVlan

Enable the guest VLAN feature to allow limited access to non-802.1X-compliant clients. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestVlanId

Guest VLAN name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestVlanid

Guest VLAN ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAuthBypass

Enable/disable MAB for this policy. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Policy name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenAuth

Enable/disable open authentication for this policy. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

Policy type. Valid values: `802.1X`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusTimeoutOverwrite

Enable to override the global RADIUS session timeout. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityMode

Port or MAC based 802.1X security mode. Valid values: `802.1X`, `802.1X-mac-based`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroup

_Required_: No

_Type_: List of <a href="usergroupdefinition.md">UserGroupDefinition</a>

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

