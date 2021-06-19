# TF::Google::CloudRunDomainMapping StatusDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#message" title="Message">Message</a>" : <i>String</i>,
    "<a href="#reason" title="Reason">Reason</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>[ <a href="statusdefinition3.md">StatusDefinition3</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#message" title="Message">Message</a>: <i>String</i>
<a href="#reason" title="Reason">Reason</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>
      - <a href="statusdefinition3.md">StatusDefinition3</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Message

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reason

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: List of <a href="statusdefinition3.md">StatusDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

