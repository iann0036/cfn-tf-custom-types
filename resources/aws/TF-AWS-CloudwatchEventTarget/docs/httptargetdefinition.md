# TF::AWS::CloudwatchEventTarget HttpTargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headerparameters" title="HeaderParameters">HeaderParameters</a>" : <i>[ <a href="headerparametersdefinition.md">HeaderParametersDefinition</a>, ... ]</i>,
    "<a href="#pathparametervalues" title="PathParameterValues">PathParameterValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#querystringparameters" title="QueryStringParameters">QueryStringParameters</a>" : <i>[ <a href="querystringparametersdefinition.md">QueryStringParametersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headerparameters" title="HeaderParameters">HeaderParameters</a>: <i>
      - <a href="headerparametersdefinition.md">HeaderParametersDefinition</a></i>
<a href="#pathparametervalues" title="PathParameterValues">PathParameterValues</a>: <i>
      - String</i>
<a href="#querystringparameters" title="QueryStringParameters">QueryStringParameters</a>: <i>
      - <a href="querystringparametersdefinition.md">QueryStringParametersDefinition</a></i>
</pre>

## Properties

#### HeaderParameters

Enables you to specify HTTP headers to add to the request.

_Required_: No

_Type_: List of <a href="headerparametersdefinition.md">HeaderParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathParameterValues

The list of values that correspond sequentially to any path variables in your endpoint ARN (for example `arn:aws:execute-api:us-east-1:123456:myapi/*/POST/pets/*`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryStringParameters

Represents keys/values of query string parameters that are appended to the invoked endpoint.

_Required_: No

_Type_: List of <a href="querystringparametersdefinition.md">QueryStringParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

