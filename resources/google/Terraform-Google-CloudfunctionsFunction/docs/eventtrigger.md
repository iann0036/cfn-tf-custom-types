# Terraform::Google::CloudfunctionsFunction EventTrigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eventtype" title="EventType">EventType</a>" : <i>String</i>,
    "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
    "<a href="#failurepolicy" title="FailurePolicy">FailurePolicy</a>" : <i>[ <a href="eventtrigger-failurepolicy.md">FailurePolicy</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#eventtype" title="EventType">EventType</a>: <i>String</i>
<a href="#resource" title="Resource">Resource</a>: <i>String</i>
<a href="#failurepolicy" title="FailurePolicy">FailurePolicy</a>: <i>
      - <a href="eventtrigger-failurepolicy.md">FailurePolicy</a></i>
</pre>

## Properties

#### EventType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resource

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailurePolicy

_Required_: No

_Type_: List of <a href="eventtrigger-failurepolicy.md">FailurePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

