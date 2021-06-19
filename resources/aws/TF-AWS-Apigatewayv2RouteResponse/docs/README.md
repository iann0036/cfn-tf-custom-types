# TF::AWS::Apigatewayv2RouteResponse

Manages an Amazon API Gateway Version 2 route response.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2RouteResponse",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#modelselectionexpression" title="ModelSelectionExpression">ModelSelectionExpression</a>" : <i>String</i>,
        "<a href="#responsemodels" title="ResponseModels">ResponseModels</a>" : <i>[ <a href="responsemodelsdefinition.md">ResponseModelsDefinition</a>, ... ]</i>,
        "<a href="#routeid" title="RouteId">RouteId</a>" : <i>String</i>,
        "<a href="#routeresponsekey" title="RouteResponseKey">RouteResponseKey</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2RouteResponse
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#modelselectionexpression" title="ModelSelectionExpression">ModelSelectionExpression</a>: <i>String</i>
    <a href="#responsemodels" title="ResponseModels">ResponseModels</a>: <i>
      - <a href="responsemodelsdefinition.md">ResponseModelsDefinition</a></i>
    <a href="#routeid" title="RouteId">RouteId</a>: <i>String</i>
    <a href="#routeresponsekey" title="RouteResponseKey">RouteResponseKey</a>: <i>String</i>
</pre>

## Properties

#### ApiId

The API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelSelectionExpression

The [model selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) for the route response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseModels

The response models for the route response.

_Required_: No

_Type_: List of <a href="responsemodelsdefinition.md">ResponseModelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteId

The identifier of the [`aws_apigatewayv2_route`](/docs/providers/aws/r/apigatewayv2_route.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteResponseKey

The route response key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

