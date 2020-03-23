# Terraform::AWS::KinesisFirehoseDeliveryStream ProcessingConfiguration Processors

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="processingconfiguration-processors-parameters.md">Parameters</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="processingconfiguration-processors-parameters.md">Parameters</a></i>
</pre>

## Properties

#### Type

The type of processor. Valid Values: `Lambda`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="processingconfiguration-processors-parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

