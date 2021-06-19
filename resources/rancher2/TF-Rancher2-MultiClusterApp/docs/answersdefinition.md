# TF::Rancher2::MultiClusterApp AnswersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
    "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ <a href="valuesdefinition.md">ValuesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
<a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
<a href="#values" title="Values">Values</a>: <i>
      - <a href="valuesdefinition.md">ValuesDefinition</a></i>
</pre>

## Properties

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

_Required_: No

_Type_: List of <a href="valuesdefinition.md">ValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

