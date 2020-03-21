# Terraform::AzureRM::MonitorDiagnosticSetting Metric RetentionPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#days" title="Days">Days</a>" : <i>Double</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#days" title="Days">Days</a>: <i>Double</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Days

The number of days for which this Retention Policy should apply.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is this Retention Policy enabled?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

