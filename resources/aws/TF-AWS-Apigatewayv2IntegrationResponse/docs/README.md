# TF::AWS::Apigatewayv2IntegrationResponse

Manages an Amazon API Gateway Version 2 integration response.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2IntegrationResponse",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#contenthandlingstrategy" title="ContentHandlingStrategy">ContentHandlingStrategy</a>" : <i>String</i>,
        "<a href="#integrationid" title="IntegrationId">IntegrationId</a>" : <i>String</i>,
        "<a href="#integrationresponsekey" title="IntegrationResponseKey">IntegrationResponseKey</a>" : <i>String</i>,
        "<a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>" : <i>[ <a href="responsetemplatesdefinition.md">ResponseTemplatesDefinition</a>, ... ]</i>,
        "<a href="#templateselectionexpression" title="TemplateSelectionExpression">TemplateSelectionExpression</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2IntegrationResponse
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#contenthandlingstrategy" title="ContentHandlingStrategy">ContentHandlingStrategy</a>: <i>String</i>
    <a href="#integrationid" title="IntegrationId">IntegrationId</a>: <i>String</i>
    <a href="#integrationresponsekey" title="IntegrationResponseKey">IntegrationResponseKey</a>: <i>String</i>
    <a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>: <i>
      - <a href="responsetemplatesdefinition.md">ResponseTemplatesDefinition</a></i>
    <a href="#templateselectionexpression" title="TemplateSelectionExpression">TemplateSelectionExpression</a>: <i>String</i>
</pre>

## Properties

#### ApiId

The API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentHandlingStrategy

How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationId

The identifier of the [`aws_apigatewayv2_integration`](/docs/providers/aws/r/apigatewayv2_integration.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationResponseKey

The integration response key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTemplates

A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.

_Required_: No

_Type_: List of <a href="responsetemplatesdefinition.md">ResponseTemplatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSelectionExpression

The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration response.

_Required_: No

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

