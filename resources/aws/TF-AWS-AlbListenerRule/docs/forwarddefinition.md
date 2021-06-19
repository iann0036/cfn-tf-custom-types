# TF::AWS::AlbListenerRule ForwardDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#stickiness" title="Stickiness">Stickiness</a>" : <i>[ <a href="stickinessdefinition.md">StickinessDefinition</a>, ... ]</i>,
    "<a href="#targetgroup" title="TargetGroup">TargetGroup</a>" : <i>[ <a href="targetgroupdefinition.md">TargetGroupDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#stickiness" title="Stickiness">Stickiness</a>: <i>
      - <a href="stickinessdefinition.md">StickinessDefinition</a></i>
<a href="#targetgroup" title="TargetGroup">TargetGroup</a>: <i>
      - <a href="targetgroupdefinition.md">TargetGroupDefinition</a></i>
</pre>

## Properties

#### Stickiness

_Required_: No

_Type_: List of <a href="stickinessdefinition.md">StickinessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroup

_Required_: No

_Type_: List of <a href="targetgroupdefinition.md">TargetGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

