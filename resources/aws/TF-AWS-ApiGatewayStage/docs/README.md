# TF::AWS::ApiGatewayStage

Manages an API Gateway Stage. A stage is a named reference to a deployment, which can be done via the [`aws_api_gateway_deployment` resource](api_gateway_deployment.html). Stages can be optionally managed further with the [`aws_api_gateway_base_path_mapping` resource](api_gateway_base_path_mapping.html), [`aws_api_gateway_domain_name` resource](api_gateway_domain_name.html), and [`aws_api_method_settings` resource](api_gateway_method_settings.html). For more information, see the [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApiGatewayStage",
    "Properties" : {
        "<a href="#cacheclusterenabled" title="CacheClusterEnabled">CacheClusterEnabled</a>" : <i>Boolean</i>,
        "<a href="#cacheclustersize" title="CacheClusterSize">CacheClusterSize</a>" : <i>String</i>,
        "<a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>" : <i>String</i>,
        "<a href="#deploymentid" title="DeploymentId">DeploymentId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#documentationversion" title="DocumentationVersion">DocumentationVersion</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#stagename" title="StageName">StageName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#variables" title="Variables">Variables</a>" : <i>[ <a href="variablesdefinition.md">VariablesDefinition</a>, ... ]</i>,
        "<a href="#xraytracingenabled" title="XrayTracingEnabled">XrayTracingEnabled</a>" : <i>Boolean</i>,
        "<a href="#accesslogsettings" title="AccessLogSettings">AccessLogSettings</a>" : <i>[ <a href="accesslogsettingsdefinition.md">AccessLogSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApiGatewayStage
Properties:
    <a href="#cacheclusterenabled" title="CacheClusterEnabled">CacheClusterEnabled</a>: <i>Boolean</i>
    <a href="#cacheclustersize" title="CacheClusterSize">CacheClusterSize</a>: <i>String</i>
    <a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>: <i>String</i>
    <a href="#deploymentid" title="DeploymentId">DeploymentId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#documentationversion" title="DocumentationVersion">DocumentationVersion</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#stagename" title="StageName">StageName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#variables" title="Variables">Variables</a>: <i>
      - <a href="variablesdefinition.md">VariablesDefinition</a></i>
    <a href="#xraytracingenabled" title="XrayTracingEnabled">XrayTracingEnabled</a>: <i>Boolean</i>
    <a href="#accesslogsettings" title="AccessLogSettings">AccessLogSettings</a>: <i>
      - <a href="accesslogsettingsdefinition.md">AccessLogSettingsDefinition</a></i>
</pre>

## Properties

#### CacheClusterEnabled

Specifies whether a cache cluster is enabled for the stage.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheClusterSize

The size of the cache cluster for the stage, if enabled. Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateId

The identifier of a client certificate for the stage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentId

The ID of the deployment that the stage points to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the stage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentationVersion

The version of the associated API documentation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the associated REST API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageName

The name of the stage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variables

A map that defines the stage variables.

_Required_: No

_Type_: List of <a href="variablesdefinition.md">VariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XrayTracingEnabled

Whether active tracing with X-ray is enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLogSettings

_Required_: No

_Type_: List of <a href="accesslogsettingsdefinition.md">AccessLogSettingsDefinition</a>

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

