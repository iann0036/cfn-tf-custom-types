# TF::Google::KmsCryptoKeyIamMember ConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#expression" title="Expression">Expression</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#expression" title="Expression">Expression</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### Description

An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expression

Textual representation of an expression in Common Expression Language syntax.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

A title for the expression, i.e. a short string describing its purpose.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

