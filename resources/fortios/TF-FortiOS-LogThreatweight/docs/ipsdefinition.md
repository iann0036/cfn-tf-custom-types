# TF::FortiOS::LogThreatweight IpsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#criticalseverity" title="CriticalSeverity">CriticalSeverity</a>" : <i>String</i>,
    "<a href="#highseverity" title="HighSeverity">HighSeverity</a>" : <i>String</i>,
    "<a href="#infoseverity" title="InfoSeverity">InfoSeverity</a>" : <i>String</i>,
    "<a href="#lowseverity" title="LowSeverity">LowSeverity</a>" : <i>String</i>,
    "<a href="#mediumseverity" title="MediumSeverity">MediumSeverity</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#criticalseverity" title="CriticalSeverity">CriticalSeverity</a>: <i>String</i>
<a href="#highseverity" title="HighSeverity">HighSeverity</a>: <i>String</i>
<a href="#infoseverity" title="InfoSeverity">InfoSeverity</a>: <i>String</i>
<a href="#lowseverity" title="LowSeverity">LowSeverity</a>: <i>String</i>
<a href="#mediumseverity" title="MediumSeverity">MediumSeverity</a>: <i>String</i>
</pre>

## Properties

#### CriticalSeverity

Threat weight score for IPS critical severity events. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighSeverity

Threat weight score for IPS high severity events. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfoSeverity

Threat weight score for IPS info severity events. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowSeverity

Threat weight score for IPS low severity events. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediumSeverity

Threat weight score for IPS medium severity events. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

