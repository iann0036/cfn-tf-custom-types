# Terraform::AWS::CodepipelineWebhook Filter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#jsonpath" title="JsonPath">JsonPath</a>" : <i>String</i>,
    "<a href="#matchequals" title="MatchEquals">MatchEquals</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#jsonpath" title="JsonPath">JsonPath</a>: <i>String</i>
<a href="#matchequals" title="MatchEquals">MatchEquals</a>: <i>String</i>
</pre>

## Properties

#### JsonPath

The [JSON path](https://github.com/json-path/JsonPath) to filter on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchEquals

The value to match on (e.g. `refs/heads/{Branch}`). See [AWS docs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html) for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

