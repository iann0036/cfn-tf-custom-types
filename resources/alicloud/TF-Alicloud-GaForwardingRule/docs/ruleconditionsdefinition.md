# TF::Alicloud::GaForwardingRule RuleConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ruleconditiontype" title="RuleConditionType">RuleConditionType</a>" : <i>String</i>,
    "<a href="#hostconfig" title="HostConfig">HostConfig</a>" : <i>[ <a href="hostconfigdefinition.md">HostConfigDefinition</a>, ... ]</i>,
    "<a href="#pathconfig" title="PathConfig">PathConfig</a>" : <i>[ <a href="pathconfigdefinition.md">PathConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ruleconditiontype" title="RuleConditionType">RuleConditionType</a>: <i>String</i>
<a href="#hostconfig" title="HostConfig">HostConfig</a>: <i>
      - <a href="hostconfigdefinition.md">HostConfigDefinition</a></i>
<a href="#pathconfig" title="PathConfig">PathConfig</a>: <i>
      - <a href="pathconfigdefinition.md">PathConfigDefinition</a></i>
</pre>

## Properties

#### RuleConditionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostConfig

_Required_: No

_Type_: List of <a href="hostconfigdefinition.md">HostConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathConfig

_Required_: No

_Type_: List of <a href="pathconfigdefinition.md">PathConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

