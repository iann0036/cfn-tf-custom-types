# TF::ILert::Connection EmailDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bodytemplate" title="BodyTemplate">BodyTemplate</a>" : <i>String</i>,
    "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bodytemplate" title="BodyTemplate">BodyTemplate</a>: <i>String</i>
<a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
<a href="#subject" title="Subject">Subject</a>: <i>String</i>
</pre>

## Properties

#### BodyTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

