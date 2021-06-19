# TF::AWS::Apigatewayv2Stage

Manages an Amazon API Gateway Version 2 stage.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2Stage",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#autodeploy" title="AutoDeploy">AutoDeploy</a>" : <i>Boolean</i>,
        "<a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>" : <i>String</i>,
        "<a href="#deploymentid" title="DeploymentId">DeploymentId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#stagevariables" title="StageVariables">StageVariables</a>" : <i>[ <a href="stagevariablesdefinition.md">StageVariablesDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#accesslogsettings" title="AccessLogSettings">AccessLogSettings</a>" : <i>[ <a href="accesslogsettingsdefinition.md">AccessLogSettingsDefinition</a>, ... ]</i>,
        "<a href="#defaultroutesettings" title="DefaultRouteSettings">DefaultRouteSettings</a>" : <i>[ <a href="defaultroutesettingsdefinition.md">DefaultRouteSettingsDefinition</a>, ... ]</i>,
        "<a href="#routesettings" title="RouteSettings">RouteSettings</a>" : <i>[ <a href="routesettingsdefinition.md">RouteSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2Stage
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#autodeploy" title="AutoDeploy">AutoDeploy</a>: <i>Boolean</i>
    <a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>: <i>String</i>
    <a href="#deploymentid" title="DeploymentId">DeploymentId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#stagevariables" title="StageVariables">StageVariables</a>: <i>
      - <a href="stagevariablesdefinition.md">StageVariablesDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#accesslogsettings" title="AccessLogSettings">AccessLogSettings</a>: <i>
      - <a href="accesslogsettingsdefinition.md">AccessLogSettingsDefinition</a></i>
    <a href="#defaultroutesettings" title="DefaultRouteSettings">DefaultRouteSettings</a>: <i>
      - <a href="defaultroutesettingsdefinition.md">DefaultRouteSettingsDefinition</a></i>
    <a href="#routesettings" title="RouteSettings">RouteSettings</a>: <i>
      - <a href="routesettingsdefinition.md">RouteSettingsDefinition</a></i>
</pre>

## Properties

#### ApiId

The API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoDeploy

Whether updates to an API automatically trigger a new deployment. Defaults to `false`. Applicable for HTTP APIs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateId

The identifier of a client certificate for the stage. Use the [`aws_api_gateway_client_certificate`](/docs/providers/aws/r/api_gateway_client_certificate.html) resource to configure a client certificate.
Supported only for WebSocket APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentId

The deployment identifier of the stage. Use the [`aws_apigatewayv2_deployment`](/docs/providers/aws/r/apigatewayv2_deployment.html) resource to configure a deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the stage. Must be less than or equal to 1024 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the stage. Must be between 1 and 128 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageVariables

A map that defines the stage variables for the stage.

_Required_: No

_Type_: List of <a href="stagevariablesdefinition.md">StageVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the stage. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLogSettings

_Required_: No

_Type_: List of <a href="accesslogsettingsdefinition.md">AccessLogSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRouteSettings

_Required_: No

_Type_: List of <a href="defaultroutesettingsdefinition.md">DefaultRouteSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteSettings

_Required_: No

_Type_: List of <a href="routesettingsdefinition.md">RouteSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ExecutionArn

Returns the <code>ExecutionArn</code> value.

#### Id

Returns the <code>Id</code> value.

#### InvokeUrl

Returns the <code>InvokeUrl</code> value.

