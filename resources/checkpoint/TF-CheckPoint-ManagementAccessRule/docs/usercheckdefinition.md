# TF::CheckPoint::ManagementAccessRule UserCheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#confirm" title="Confirm">Confirm</a>" : <i>String</i>,
    "<a href="#frequency" title="Frequency">Frequency</a>" : <i>String</i>,
    "<a href="#interaction" title="Interaction">Interaction</a>" : <i>String</i>,
    "<a href="#customfrequency" title="CustomFrequency">CustomFrequency</a>" : <i>[ <a href="customfrequencydefinition.md">CustomFrequencyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#confirm" title="Confirm">Confirm</a>: <i>String</i>
<a href="#frequency" title="Frequency">Frequency</a>: <i>String</i>
<a href="#interaction" title="Interaction">Interaction</a>: <i>String</i>
<a href="#customfrequency" title="CustomFrequency">CustomFrequency</a>: <i>
      - <a href="customfrequencydefinition.md">CustomFrequencyDefinition</a></i>
</pre>

## Properties

#### Confirm

N/A.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frequency

N/A.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interaction

N/A.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomFrequency

_Required_: No

_Type_: List of <a href="customfrequencydefinition.md">CustomFrequencyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

