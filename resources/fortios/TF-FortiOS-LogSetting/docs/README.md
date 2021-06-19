# TF::FortiOS::LogSetting

Configure general log settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogSetting",
    "Properties" : {
        "<a href="#brieftrafficformat" title="BriefTrafficFormat">BriefTrafficFormat</a>" : <i>String</i>,
        "<a href="#daemonlog" title="DaemonLog">DaemonLog</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#expolicyimplicitlog" title="ExpolicyImplicitLog">ExpolicyImplicitLog</a>" : <i>String</i>,
        "<a href="#fazoverride" title="FazOverride">FazOverride</a>" : <i>String</i>,
        "<a href="#fwpolicy6implicitlog" title="Fwpolicy6ImplicitLog">Fwpolicy6ImplicitLog</a>" : <i>String</i>,
        "<a href="#fwpolicyimplicitlog" title="FwpolicyImplicitLog">FwpolicyImplicitLog</a>" : <i>String</i>,
        "<a href="#localinallow" title="LocalInAllow">LocalInAllow</a>" : <i>String</i>,
        "<a href="#localindenybroadcast" title="LocalInDenyBroadcast">LocalInDenyBroadcast</a>" : <i>String</i>,
        "<a href="#localindenyunicast" title="LocalInDenyUnicast">LocalInDenyUnicast</a>" : <i>String</i>,
        "<a href="#localout" title="LocalOut">LocalOut</a>" : <i>String</i>,
        "<a href="#loginvalidpacket" title="LogInvalidPacket">LogInvalidPacket</a>" : <i>String</i>,
        "<a href="#logpolicycomment" title="LogPolicyComment">LogPolicyComment</a>" : <i>String</i>,
        "<a href="#logpolicyname" title="LogPolicyName">LogPolicyName</a>" : <i>String</i>,
        "<a href="#loguserinupper" title="LogUserInUpper">LogUserInUpper</a>" : <i>String</i>,
        "<a href="#neighborevent" title="NeighborEvent">NeighborEvent</a>" : <i>String</i>,
        "<a href="#resolveip" title="ResolveIp">ResolveIp</a>" : <i>String</i>,
        "<a href="#resolveport" title="ResolvePort">ResolvePort</a>" : <i>String</i>,
        "<a href="#syslogoverride" title="SyslogOverride">SyslogOverride</a>" : <i>String</i>,
        "<a href="#useranonymize" title="UserAnonymize">UserAnonymize</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#customlogfields" title="CustomLogFields">CustomLogFields</a>" : <i>[ <a href="customlogfieldsdefinition.md">CustomLogFieldsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogSetting
Properties:
    <a href="#brieftrafficformat" title="BriefTrafficFormat">BriefTrafficFormat</a>: <i>String</i>
    <a href="#daemonlog" title="DaemonLog">DaemonLog</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#expolicyimplicitlog" title="ExpolicyImplicitLog">ExpolicyImplicitLog</a>: <i>String</i>
    <a href="#fazoverride" title="FazOverride">FazOverride</a>: <i>String</i>
    <a href="#fwpolicy6implicitlog" title="Fwpolicy6ImplicitLog">Fwpolicy6ImplicitLog</a>: <i>String</i>
    <a href="#fwpolicyimplicitlog" title="FwpolicyImplicitLog">FwpolicyImplicitLog</a>: <i>String</i>
    <a href="#localinallow" title="LocalInAllow">LocalInAllow</a>: <i>String</i>
    <a href="#localindenybroadcast" title="LocalInDenyBroadcast">LocalInDenyBroadcast</a>: <i>String</i>
    <a href="#localindenyunicast" title="LocalInDenyUnicast">LocalInDenyUnicast</a>: <i>String</i>
    <a href="#localout" title="LocalOut">LocalOut</a>: <i>String</i>
    <a href="#loginvalidpacket" title="LogInvalidPacket">LogInvalidPacket</a>: <i>String</i>
    <a href="#logpolicycomment" title="LogPolicyComment">LogPolicyComment</a>: <i>String</i>
    <a href="#logpolicyname" title="LogPolicyName">LogPolicyName</a>: <i>String</i>
    <a href="#loguserinupper" title="LogUserInUpper">LogUserInUpper</a>: <i>String</i>
    <a href="#neighborevent" title="NeighborEvent">NeighborEvent</a>: <i>String</i>
    <a href="#resolveip" title="ResolveIp">ResolveIp</a>: <i>String</i>
    <a href="#resolveport" title="ResolvePort">ResolvePort</a>: <i>String</i>
    <a href="#syslogoverride" title="SyslogOverride">SyslogOverride</a>: <i>String</i>
    <a href="#useranonymize" title="UserAnonymize">UserAnonymize</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#customlogfields" title="CustomLogFields">CustomLogFields</a>: <i>
      - <a href="customlogfieldsdefinition.md">CustomLogFieldsDefinition</a></i>
</pre>

## Properties

#### BriefTrafficFormat

Enable/disable brief format traffic logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaemonLog

Enable/disable daemon logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpolicyImplicitLog

Enable/disable explicit proxy firewall implicit policy logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FazOverride

Enable/disable override FortiAnalyzer settings. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fwpolicy6ImplicitLog

Enable/disable implicit firewall policy6 logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwpolicyImplicitLog

Enable/disable implicit firewall policy logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalInAllow

Enable/disable local-in-allow logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalInDenyBroadcast

Enable/disable local-in-deny-broadcast logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalInDenyUnicast

Enable/disable local-in-deny-unicast logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalOut

Enable/disable local-out logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogInvalidPacket

Enable/disable invalid packet traffic logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPolicyComment

Enable/disable inserting policy comments into traffic logs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPolicyName

Enable/disable inserting policy name into traffic logs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogUserInUpper

Enable/disable logs with user-in-upper. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborEvent

Enable/disable neighbor event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveIp

Enable/disable adding resolved domain names to traffic logs if possible. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolvePort

Enable/disable adding resolved service names to traffic logs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogOverride

Enable/disable override Syslog settings. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAnonymize

Enable/disable anonymizing user names in log messages. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomLogFields

_Required_: No

_Type_: List of <a href="customlogfieldsdefinition.md">CustomLogFieldsDefinition</a>

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

