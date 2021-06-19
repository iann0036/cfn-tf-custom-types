# TF::AWS::LexIntent SlotDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#responsecard" title="ResponseCard">ResponseCard</a>" : <i>String</i>,
    "<a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>" : <i>[ String, ... ]</i>,
    "<a href="#slotconstraint" title="SlotConstraint">SlotConstraint</a>" : <i>String</i>,
    "<a href="#slottype" title="SlotType">SlotType</a>" : <i>String</i>,
    "<a href="#slottypeversion" title="SlotTypeVersion">SlotTypeVersion</a>" : <i>String</i>,
    "<a href="#valueelicitationprompt" title="ValueElicitationPrompt">ValueElicitationPrompt</a>" : <i>[ <a href="valueelicitationpromptdefinition.md">ValueElicitationPromptDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#responsecard" title="ResponseCard">ResponseCard</a>: <i>String</i>
<a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>: <i>
      - String</i>
<a href="#slotconstraint" title="SlotConstraint">SlotConstraint</a>: <i>String</i>
<a href="#slottype" title="SlotType">SlotType</a>: <i>String</i>
<a href="#slottypeversion" title="SlotTypeVersion">SlotTypeVersion</a>: <i>String</i>
<a href="#valueelicitationprompt" title="ValueElicitationPrompt">ValueElicitationPrompt</a>: <i>
      - <a href="valueelicitationpromptdefinition.md">ValueElicitationPromptDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCard

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleUtterances

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotConstraint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotTypeVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueElicitationPrompt

_Required_: No

_Type_: List of <a href="valueelicitationpromptdefinition.md">ValueElicitationPromptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

