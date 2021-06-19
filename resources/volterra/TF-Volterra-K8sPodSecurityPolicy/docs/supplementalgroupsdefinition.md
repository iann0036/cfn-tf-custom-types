# TF::Volterra::K8sPodSecurityPolicy SupplementalGroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rule" title="Rule">Rule</a>" : <i>String</i>,
    "<a href="#idranges" title="IdRanges">IdRanges</a>" : <i>[ <a href="idrangesdefinition.md">IdRangesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rule" title="Rule">Rule</a>: <i>String</i>
<a href="#idranges" title="IdRanges">IdRanges</a>: <i>
      - <a href="idrangesdefinition.md">IdRangesDefinition</a></i>
</pre>

## Properties

#### Rule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdRanges

_Required_: No

_Type_: List of <a href="idrangesdefinition.md">IdRangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

