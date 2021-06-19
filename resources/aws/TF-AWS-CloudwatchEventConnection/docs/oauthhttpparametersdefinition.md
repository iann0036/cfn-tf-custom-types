# TF::AWS::CloudwatchEventConnection OauthHttpParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#body" title="Body">Body</a>" : <i>[ <a href="bodydefinition.md">BodyDefinition</a>, ... ]</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="headerdefinition.md">HeaderDefinition</a>, ... ]</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>[ <a href="querystringdefinition.md">QueryStringDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#body" title="Body">Body</a>: <i>
      - <a href="bodydefinition.md">BodyDefinition</a></i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="headerdefinition.md">HeaderDefinition</a></i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>
      - <a href="querystringdefinition.md">QueryStringDefinition</a></i>
</pre>

## Properties

#### Body

_Required_: No

_Type_: List of <a href="bodydefinition.md">BodyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="headerdefinition.md">HeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: No

_Type_: List of <a href="querystringdefinition.md">QueryStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

