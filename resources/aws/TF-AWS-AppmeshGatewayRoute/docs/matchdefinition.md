# TF::AWS::AppmeshGatewayRoute MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
</pre>

## Properties

#### Prefix

Specifies the path to match requests with. This parameter must always start with `/`, which by itself matches all requests to the virtual service name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

