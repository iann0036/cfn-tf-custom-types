# TF::FortiOS::LogThreatweight

Configure threat weight settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogThreatweight",
    "Properties" : {
        "<a href="#blockedconnection" title="BlockedConnection">BlockedConnection</a>" : <i>String</i>,
        "<a href="#botnetconnectiondetected" title="BotnetConnectionDetected">BotnetConnectionDetected</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#failedconnection" title="FailedConnection">FailedConnection</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#urlblockdetected" title="UrlBlockDetected">UrlBlockDetected</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#application" title="Application">Application</a>" : <i>[ <a href="applicationdefinition.md">ApplicationDefinition</a>, ... ]</i>,
        "<a href="#geolocation" title="Geolocation">Geolocation</a>" : <i>[ <a href="geolocationdefinition.md">GeolocationDefinition</a>, ... ]</i>,
        "<a href="#ips" title="Ips">Ips</a>" : <i>[ <a href="ipsdefinition.md">IpsDefinition</a>, ... ]</i>,
        "<a href="#level" title="Level">Level</a>" : <i>[ <a href="leveldefinition.md">LevelDefinition</a>, ... ]</i>,
        "<a href="#malware" title="Malware">Malware</a>" : <i>[ <a href="malwaredefinition.md">MalwareDefinition</a>, ... ]</i>,
        "<a href="#web" title="Web">Web</a>" : <i>[ <a href="webdefinition.md">WebDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogThreatweight
Properties:
    <a href="#blockedconnection" title="BlockedConnection">BlockedConnection</a>: <i>String</i>
    <a href="#botnetconnectiondetected" title="BotnetConnectionDetected">BotnetConnectionDetected</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#failedconnection" title="FailedConnection">FailedConnection</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#urlblockdetected" title="UrlBlockDetected">UrlBlockDetected</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#application" title="Application">Application</a>: <i>
      - <a href="applicationdefinition.md">ApplicationDefinition</a></i>
    <a href="#geolocation" title="Geolocation">Geolocation</a>: <i>
      - <a href="geolocationdefinition.md">GeolocationDefinition</a></i>
    <a href="#ips" title="Ips">Ips</a>: <i>
      - <a href="ipsdefinition.md">IpsDefinition</a></i>
    <a href="#level" title="Level">Level</a>: <i>
      - <a href="leveldefinition.md">LevelDefinition</a></i>
    <a href="#malware" title="Malware">Malware</a>: <i>
      - <a href="malwaredefinition.md">MalwareDefinition</a></i>
    <a href="#web" title="Web">Web</a>: <i>
      - <a href="webdefinition.md">WebDefinition</a></i>
</pre>

## Properties

#### BlockedConnection

Threat weight score for blocked connections. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BotnetConnectionDetected

Threat weight score for detected botnet connections. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedConnection

Threat weight score for failed connections. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the threat weight feature. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlBlockDetected

Threat weight score for URL blocking. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

_Required_: No

_Type_: List of <a href="applicationdefinition.md">ApplicationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Geolocation

_Required_: No

_Type_: List of <a href="geolocationdefinition.md">GeolocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ips

_Required_: No

_Type_: List of <a href="ipsdefinition.md">IpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

_Required_: No

_Type_: List of <a href="leveldefinition.md">LevelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Malware

_Required_: No

_Type_: List of <a href="malwaredefinition.md">MalwareDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Web

_Required_: No

_Type_: List of <a href="webdefinition.md">WebDefinition</a>

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

