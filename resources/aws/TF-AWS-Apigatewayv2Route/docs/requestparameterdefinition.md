# TF::AWS::Apigatewayv2Route RequestParameterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#requestparameterkey" title="RequestParameterKey">RequestParameterKey</a>" : <i>String</i>,
    "<a href="#required" title="Required">Required</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#requestparameterkey" title="RequestParameterKey">RequestParameterKey</a>: <i>String</i>
<a href="#required" title="Required">Required</a>: <i>Boolean</i>
</pre>

## Properties

#### RequestParameterKey

Request parameter key. This is a [request data mapping parameter](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-data-mapping.html#websocket-mapping-request-parameters).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

Boolean whether or not the parameter is required.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

