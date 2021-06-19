# TF::AWS::LexIntent ConfirmationPromptDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxattempts" title="MaxAttempts">MaxAttempts</a>" : <i>Double</i>,
    "<a href="#responsecard" title="ResponseCard">ResponseCard</a>" : <i>String</i>,
    "<a href="#message" title="Message">Message</a>" : <i>[ <a href="messagedefinition.md">MessageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxattempts" title="MaxAttempts">MaxAttempts</a>: <i>Double</i>
<a href="#responsecard" title="ResponseCard">ResponseCard</a>: <i>String</i>
<a href="#message" title="Message">Message</a>: <i>
      - <a href="messagedefinition.md">MessageDefinition</a></i>
</pre>

## Properties

#### MaxAttempts

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCard

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: List of <a href="messagedefinition.md">MessageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

