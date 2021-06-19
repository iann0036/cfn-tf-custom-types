# TF::AVI::Labelgroup LabelsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchoperation" title="MatchOperation">MatchOperation</a>" : <i>String</i>,
    "<a href="#matchlabel" title="MatchLabel">MatchLabel</a>" : <i>[ <a href="matchlabeldefinition.md">MatchLabelDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchoperation" title="MatchOperation">MatchOperation</a>: <i>String</i>
<a href="#matchlabel" title="MatchLabel">MatchLabel</a>: <i>
      - <a href="matchlabeldefinition.md">MatchLabelDefinition</a></i>
</pre>

## Properties

#### MatchOperation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchLabel

_Required_: No

_Type_: List of <a href="matchlabeldefinition.md">MatchLabelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

