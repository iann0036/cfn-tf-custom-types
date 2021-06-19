# TF::FortiOS::SystemCentralmanagement

Configure central management.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemCentralmanagement",
    "Properties" : {
        "<a href="#allowmonitor" title="AllowMonitor">AllowMonitor</a>" : <i>String</i>,
        "<a href="#allowpushconfiguration" title="AllowPushConfiguration">AllowPushConfiguration</a>" : <i>String</i>,
        "<a href="#allowpushfirmware" title="AllowPushFirmware">AllowPushFirmware</a>" : <i>String</i>,
        "<a href="#allowremotefirmwareupgrade" title="AllowRemoteFirmwareUpgrade">AllowRemoteFirmwareUpgrade</a>" : <i>String</i>,
        "<a href="#cacert" title="CaCert">CaCert</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#encalgorithm" title="EncAlgorithm">EncAlgorithm</a>" : <i>String</i>,
        "<a href="#fmg" title="Fmg">Fmg</a>" : <i>String</i>,
        "<a href="#fmgsourceip" title="FmgSourceIp">FmgSourceIp</a>" : <i>String</i>,
        "<a href="#fmgsourceip6" title="FmgSourceIp6">FmgSourceIp6</a>" : <i>String</i>,
        "<a href="#fmgupdateport" title="FmgUpdatePort">FmgUpdatePort</a>" : <i>String</i>,
        "<a href="#includedefaultservers" title="IncludeDefaultServers">IncludeDefaultServers</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#localcert" title="LocalCert">LocalCert</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#scheduleconfigrestore" title="ScheduleConfigRestore">ScheduleConfigRestore</a>" : <i>String</i>,
        "<a href="#schedulescriptrestore" title="ScheduleScriptRestore">ScheduleScriptRestore</a>" : <i>String</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#serverlist" title="ServerList">ServerList</a>" : <i>[ <a href="serverlistdefinition.md">ServerListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemCentralmanagement
Properties:
    <a href="#allowmonitor" title="AllowMonitor">AllowMonitor</a>: <i>String</i>
    <a href="#allowpushconfiguration" title="AllowPushConfiguration">AllowPushConfiguration</a>: <i>String</i>
    <a href="#allowpushfirmware" title="AllowPushFirmware">AllowPushFirmware</a>: <i>String</i>
    <a href="#allowremotefirmwareupgrade" title="AllowRemoteFirmwareUpgrade">AllowRemoteFirmwareUpgrade</a>: <i>String</i>
    <a href="#cacert" title="CaCert">CaCert</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#encalgorithm" title="EncAlgorithm">EncAlgorithm</a>: <i>String</i>
    <a href="#fmg" title="Fmg">Fmg</a>: <i>String</i>
    <a href="#fmgsourceip" title="FmgSourceIp">FmgSourceIp</a>: <i>String</i>
    <a href="#fmgsourceip6" title="FmgSourceIp6">FmgSourceIp6</a>: <i>String</i>
    <a href="#fmgupdateport" title="FmgUpdatePort">FmgUpdatePort</a>: <i>String</i>
    <a href="#includedefaultservers" title="IncludeDefaultServers">IncludeDefaultServers</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
    <a href="#localcert" title="LocalCert">LocalCert</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#scheduleconfigrestore" title="ScheduleConfigRestore">ScheduleConfigRestore</a>: <i>String</i>
    <a href="#schedulescriptrestore" title="ScheduleScriptRestore">ScheduleScriptRestore</a>: <i>String</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#serverlist" title="ServerList">ServerList</a>: <i>
      - <a href="serverlistdefinition.md">ServerListDefinition</a></i>
</pre>

## Properties

#### AllowMonitor

Enable/disable allowing the central management server to remotely monitor this FortiGate Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowPushConfiguration

Enable/disable allowing the central management server to push configuration changes to this FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowPushFirmware

Enable/disable allowing the central management server to push firmware updates to this FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRemoteFirmwareUpgrade

Enable/disable remotely upgrading the firmware on this FortiGate from the central management server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCert

CA certificate to be used by FGFM protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncAlgorithm

Encryption strength for communications between the FortiGate and central management. Valid values: `default`, `high`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fmg

IP address or FQDN of the FortiManager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FmgSourceIp

IPv4 source address that this FortiGate uses when communicating with FortiManager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FmgSourceIp6

IPv6 source address that this FortiGate uses when communicating with FortiManager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FmgUpdatePort

Port used to communicate with FortiManager that is acting as a FortiGuard update server. Valid values: `8890`, `443`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeDefaultServers

Enable/disable inclusion of public FortiGuard servers in the override server list. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalCert

Certificate to be used by FGFM protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Central management mode. Valid values: `normal`, `backup`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleConfigRestore

Enable/disable allowing the central management server to restore the configuration of this FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleScriptRestore

Enable/disable allowing the central management server to restore the scripts stored on this FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

Serial number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Central management type. Valid values: `fortimanager`, `fortiguard`, `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

Virtual domain (VDOM) name to use when communicating with FortiManager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerList

_Required_: No

_Type_: List of <a href="serverlistdefinition.md">ServerListDefinition</a>

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

