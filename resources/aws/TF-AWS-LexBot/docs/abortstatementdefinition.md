# TF::AWS::LexBot AbortStatementDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#responsecard" title="ResponseCard">ResponseCard</a>" : <i>String</i>,
    "<a href="#message" title="Message">Message</a>" : <i>[ <a href="messagedefinition.md">MessageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#responsecard" title="ResponseCard">ResponseCard</a>: <i>String</i>
<a href="#message" title="Message">Message</a>: <i>
      - <a href="messagedefinition.md">MessageDefinition</a></i>
</pre>

## Properties

#### ResponseCard

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: List of <a href="messagedefinition.md">MessageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

