# Terraform::AWS::ApiGatewayStage

Provides an API Gateway Stage.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayStage",
    "Properties" : {
        "<a href="#cacheclusterenabled" title="CacheClusterEnabled">CacheClusterEnabled</a>" : <i>Boolean</i>,
        "<a href="#cacheclustersize" title="CacheClusterSize">CacheClusterSize</a>" : <i>String</i>,
        "<a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>" : <i>String</i>,
        "<a href="#deploymentid" title="DeploymentId">DeploymentId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#documentationversion" title="DocumentationVersion">DocumentationVersion</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#stagename" title="StageName">StageName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#variables" title="Variables">Variables</a>" : <i>[ <a href="variables.md">Variables</a>, ... ]</i>,
        "<a href="#xraytracingenabled" title="XrayTracingEnabled">XrayTracingEnabled</a>" : <i>Boolean</i>,
        "<a href="#accesslogsettings" title="AccessLogSettings">AccessLogSettings</a>" : <i>[ <a href="accesslogsettings.md">AccessLogSettings</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayStage
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
      - <a href="tags.md">Tags</a></i>
    <a href="#variables" title="Variables">Variables</a>: <i>
      - <a href="variables.md">Variables</a></i>
    <a href="#xraytracingenabled" title="XrayTracingEnabled">XrayTracingEnabled</a>: <i>Boolean</i>
    <a href="#accesslogsettings" title="AccessLogSettings">AccessLogSettings</a>: <i>
      - <a href="accesslogsettings.md">AccessLogSettings</a></i>
</pre>

## Properties

#### CacheClusterEnabled

Specifies whether a cache cluster is enabled for the stage.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheClusterSize

The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

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

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variables

A map that defines the stage variables.

_Required_: No

_Type_: List of <a href="variables.md">Variables</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XrayTracingEnabled

Whether active tracing with X-ray is enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLogSettings

_Required_: No

_Type_: List of <a href="accesslogsettings.md">AccessLogSettings</a>

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

