# TF::AWS::ApiGatewayDeployment

Manages an API Gateway REST Deployment. A deployment is a snapshot of the REST API configuration. The deployment can then be published to callable endpoints via the [`aws_api_gateway_stage` resource](api_gateway_stage.html) and optionally managed further with the [`aws_api_gateway_base_path_mapping` resource](api_gateway_base_path_mapping.html), [`aws_api_gateway_domain_name` resource](api_gateway_domain_name.html), and [`aws_api_method_settings` resource](api_gateway_method_settings.html). For more information, see the [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html).

To properly capture all REST API configuration in a deployment, this resource must have dependencies on all prior Terraform resources that manage resources/paths, methods, integrations, etc.

* For REST APIs that are configured via OpenAPI specification ([`aws_api_gateway_rest_api` resource](api_gateway_rest_api.html) `body` argument), no special dependency setup is needed b...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApiGatewayDeployment",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#stagedescription" title="StageDescription">StageDescription</a>" : <i>String</i>,
        "<a href="#stagename" title="StageName">StageName</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ <a href="triggersdefinition.md">TriggersDefinition</a>, ... ]</i>,
        "<a href="#variables" title="Variables">Variables</a>" : <i>[ <a href="variablesdefinition.md">VariablesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApiGatewayDeployment
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#stagedescription" title="StageDescription">StageDescription</a>: <i>String</i>
    <a href="#stagename" title="StageName">StageName</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - <a href="triggersdefinition.md">TriggersDefinition</a></i>
    <a href="#variables" title="Variables">Variables</a>: <i>
      - <a href="variablesdefinition.md">VariablesDefinition</a></i>
</pre>

## Properties

#### Description

Description of the deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

REST API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageDescription

Description to set on the stage managed by the `stage_name` argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageName

Name of the stage to create with this deployment. If the specified stage already exists, it will be updated to point to the new deployment. It is recommended to use the [`aws_api_gateway_stage` resource](api_gateway_stage.html) instead to manage stages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

Map of arbitrary keys and values that, when changed, will trigger a redeployment. To force a redeployment without changing these keys/values, use the [`terraform taint` command](https://www.terraform.io/docs/commands/taint.html).

_Required_: No

_Type_: List of <a href="triggersdefinition.md">TriggersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variables

Map to set on the stage managed by the `stage_name` argument.

_Required_: No

_Type_: List of <a href="variablesdefinition.md">VariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### ExecutionArn

Returns the <code>ExecutionArn</code> value.

#### Id

Returns the <code>Id</code> value.

#### InvokeUrl

Returns the <code>InvokeUrl</code> value.

