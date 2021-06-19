# TF::Alicloud::CmsGroupMetricRule EscalationsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#critical" title="Critical">Critical</a>" : <i>[ <a href="criticaldefinition.md">CriticalDefinition</a>, ... ]</i>,
    "<a href="#info" title="Info">Info</a>" : <i>[ <a href="infodefinition.md">InfoDefinition</a>, ... ]</i>,
    "<a href="#warn" title="Warn">Warn</a>" : <i>[ <a href="warndefinition.md">WarnDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#critical" title="Critical">Critical</a>: <i>
      - <a href="criticaldefinition.md">CriticalDefinition</a></i>
<a href="#info" title="Info">Info</a>: <i>
      - <a href="infodefinition.md">InfoDefinition</a></i>
<a href="#warn" title="Warn">Warn</a>: <i>
      - <a href="warndefinition.md">WarnDefinition</a></i>
</pre>

## Properties

#### Critical

_Required_: No

_Type_: List of <a href="criticaldefinition.md">CriticalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Info

_Required_: No

_Type_: List of <a href="infodefinition.md">InfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Warn

_Required_: No

_Type_: List of <a href="warndefinition.md">WarnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

