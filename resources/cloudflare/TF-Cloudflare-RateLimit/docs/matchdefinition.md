# TF::Cloudflare::RateLimit MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#request" title="Request">Request</a>" : <i>[ <a href="requestdefinition.md">RequestDefinition</a>, ... ]</i>,
    "<a href="#response" title="Response">Response</a>" : <i>[ <a href="responsedefinition.md">ResponseDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#request" title="Request">Request</a>: <i>
      - <a href="requestdefinition.md">RequestDefinition</a></i>
<a href="#response" title="Response">Response</a>: <i>
      - <a href="responsedefinition.md">ResponseDefinition</a></i>
</pre>

## Properties

#### Request

_Required_: No

_Type_: List of <a href="requestdefinition.md">RequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Response

_Required_: No

_Type_: List of <a href="responsedefinition.md">ResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

