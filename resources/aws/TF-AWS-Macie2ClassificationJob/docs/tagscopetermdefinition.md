# TF::AWS::Macie2ClassificationJob TagScopeTermDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comparator" title="Comparator">Comparator</a>" : <i>String</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#tagvalues" title="TagValues">TagValues</a>" : <i>[ <a href="tagvaluesdefinition.md">TagValuesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comparator" title="Comparator">Comparator</a>: <i>String</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#tagvalues" title="TagValues">TagValues</a>: <i>
      - <a href="tagvaluesdefinition.md">TagValuesDefinition</a></i>
</pre>

## Properties

#### Comparator

The operator to use in the condition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The tag key to use in the condition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

The type of object to apply the condition to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagValues

_Required_: No

_Type_: List of <a href="tagvaluesdefinition.md">TagValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

