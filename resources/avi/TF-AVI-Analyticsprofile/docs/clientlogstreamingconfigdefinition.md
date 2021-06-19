# TF::AVI::Analyticsprofile ClientLogStreamingConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#externalserver" title="ExternalServer">ExternalServer</a>" : <i>String</i>,
    "<a href="#externalserverport" title="ExternalServerPort">ExternalServerPort</a>" : <i>Double</i>,
    "<a href="#logtypestosend" title="LogTypesToSend">LogTypesToSend</a>" : <i>String</i>,
    "<a href="#maxlogspersecond" title="MaxLogsPerSecond">MaxLogsPerSecond</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#formatconfig" title="FormatConfig">FormatConfig</a>" : <i>[ <a href="formatconfigdefinition.md">FormatConfigDefinition</a>, ... ]</i>,
    "<a href="#syslogconfig" title="SyslogConfig">SyslogConfig</a>" : <i>[ <a href="syslogconfigdefinition.md">SyslogConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#externalserver" title="ExternalServer">ExternalServer</a>: <i>String</i>
<a href="#externalserverport" title="ExternalServerPort">ExternalServerPort</a>: <i>Double</i>
<a href="#logtypestosend" title="LogTypesToSend">LogTypesToSend</a>: <i>String</i>
<a href="#maxlogspersecond" title="MaxLogsPerSecond">MaxLogsPerSecond</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#formatconfig" title="FormatConfig">FormatConfig</a>: <i>
      - <a href="formatconfigdefinition.md">FormatConfigDefinition</a></i>
<a href="#syslogconfig" title="SyslogConfig">SyslogConfig</a>: <i>
      - <a href="syslogconfigdefinition.md">SyslogConfigDefinition</a></i>
</pre>

## Properties

#### ExternalServer

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalServerPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogTypesToSend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLogsPerSecond

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormatConfig

_Required_: No

_Type_: List of <a href="formatconfigdefinition.md">FormatConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogConfig

_Required_: No

_Type_: List of <a href="syslogconfigdefinition.md">SyslogConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

