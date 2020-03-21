# Terraform::AzureRM::NetworkWatcherFlowLog RetentionPolicy

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

The number of days to retain flow log records.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Boolean flag to enable/disable retention.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

