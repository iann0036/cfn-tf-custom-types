# TF::NS1::Record AnswersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#answer" title="Answer">Answer</a>" : <i>String</i>,
    "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="metadefinition.md">MetaDefinition</a>, ... ]</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#answer" title="Answer">Answer</a>: <i>String</i>
<a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="metadefinition.md">MetaDefinition</a></i>
<a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### Answer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

_Required_: No

_Type_: List of <a href="metadefinition.md">MetaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

