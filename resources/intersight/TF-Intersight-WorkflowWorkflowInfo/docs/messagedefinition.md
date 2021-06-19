# TF::Intersight::WorkflowWorkflowInfo MessageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
    "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
    "<a href="#message" title="Message">Message</a>" : <i>[ <a href="messagedefinition.md">MessageDefinition</a>, ... ]</i>,
    "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
<a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
<a href="#message" title="Message">Message</a>: <i>
      - <a href="messagedefinition.md">MessageDefinition</a></i>
<a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>String</i>
</pre>

## Properties

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: List of <a href="messagedefinition.md">MessageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

