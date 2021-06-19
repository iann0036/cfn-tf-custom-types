# TF::Checkly::AlertChannel WebhookDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#queryparameters" title="QueryParameters">QueryParameters</a>" : <i>[ <a href="queryparametersdefinition.md">QueryParametersDefinition</a>, ... ]</i>,
    "<a href="#template" title="Template">Template</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#webhooksecret" title="WebhookSecret">WebhookSecret</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#queryparameters" title="QueryParameters">QueryParameters</a>: <i>
      - <a href="queryparametersdefinition.md">QueryParametersDefinition</a></i>
<a href="#template" title="Template">Template</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#webhooksecret" title="WebhookSecret">WebhookSecret</a>: <i>String</i>
</pre>

## Properties

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameters

_Required_: No

_Type_: List of <a href="queryparametersdefinition.md">QueryParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

