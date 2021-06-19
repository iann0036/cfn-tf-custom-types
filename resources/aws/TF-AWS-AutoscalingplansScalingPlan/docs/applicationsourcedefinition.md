# TF::AWS::AutoscalingplansScalingPlan ApplicationSourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudformationstackarn" title="CloudformationStackArn">CloudformationStackArn</a>" : <i>String</i>,
    "<a href="#tagfilter" title="TagFilter">TagFilter</a>" : <i>[ <a href="tagfilterdefinition.md">TagFilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudformationstackarn" title="CloudformationStackArn">CloudformationStackArn</a>: <i>String</i>
<a href="#tagfilter" title="TagFilter">TagFilter</a>: <i>
      - <a href="tagfilterdefinition.md">TagFilterDefinition</a></i>
</pre>

## Properties

#### CloudformationStackArn

The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagFilter

_Required_: No

_Type_: List of <a href="tagfilterdefinition.md">TagFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

