# TF::PrismaCloud::RqlSearch TimeRangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#absolute" title="Absolute">Absolute</a>" : <i>[ <a href="absolutedefinition.md">AbsoluteDefinition</a>, ... ]</i>,
    "<a href="#relative" title="Relative">Relative</a>" : <i>[ <a href="relativedefinition.md">RelativeDefinition</a>, ... ]</i>,
    "<a href="#tonow" title="ToNow">ToNow</a>" : <i>[ <a href="tonowdefinition.md">ToNowDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#absolute" title="Absolute">Absolute</a>: <i>
      - <a href="absolutedefinition.md">AbsoluteDefinition</a></i>
<a href="#relative" title="Relative">Relative</a>: <i>
      - <a href="relativedefinition.md">RelativeDefinition</a></i>
<a href="#tonow" title="ToNow">ToNow</a>: <i>
      - <a href="tonowdefinition.md">ToNowDefinition</a></i>
</pre>

## Properties

#### Absolute

_Required_: No

_Type_: List of <a href="absolutedefinition.md">AbsoluteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Relative

_Required_: No

_Type_: List of <a href="relativedefinition.md">RelativeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToNow

_Required_: No

_Type_: List of <a href="tonowdefinition.md">ToNowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

