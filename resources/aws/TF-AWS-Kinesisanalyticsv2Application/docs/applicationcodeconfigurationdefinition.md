# TF::AWS::Kinesisanalyticsv2Application ApplicationCodeConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#codecontenttype" title="CodeContentType">CodeContentType</a>" : <i>String</i>,
    "<a href="#codecontent" title="CodeContent">CodeContent</a>" : <i>[ <a href="codecontentdefinition.md">CodeContentDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#codecontenttype" title="CodeContentType">CodeContentType</a>: <i>String</i>
<a href="#codecontent" title="CodeContent">CodeContent</a>: <i>
      - <a href="codecontentdefinition.md">CodeContentDefinition</a></i>
</pre>

## Properties

#### CodeContentType

Specifies whether the code content is in text or zip format. Valid values: `PLAINTEXT`, `ZIPFILE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeContent

_Required_: No

_Type_: List of <a href="codecontentdefinition.md">CodeContentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

