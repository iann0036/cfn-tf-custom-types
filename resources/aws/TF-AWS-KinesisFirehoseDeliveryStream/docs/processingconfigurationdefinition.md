# TF::AWS::KinesisFirehoseDeliveryStream ProcessingConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#processors" title="Processors">Processors</a>" : <i>[ <a href="processorsdefinition.md">ProcessorsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#processors" title="Processors">Processors</a>: <i>
      - <a href="processorsdefinition.md">ProcessorsDefinition</a></i>
</pre>

## Properties

#### Enabled

Enables or disables data processing.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Processors

_Required_: No

_Type_: List of <a href="processorsdefinition.md">ProcessorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

