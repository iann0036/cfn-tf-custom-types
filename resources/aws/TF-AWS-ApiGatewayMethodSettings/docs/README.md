# TF::AWS::ApiGatewayMethodSettings

Manages API Gateway Stage Method Settings. For example, CloudWatch logging and metrics.

~> **NOTE:** It is recommended to use this resource in conjunction with the [`aws_api_gateway_stage` resource](api_gateway_stage.html) instead of a stage managed by the [`aws_api_gateway_deployment` resource](api_gateway_deployment.html) optional `stage_name` argument. Stages managed by the `aws_api_gateway_deployment` resource are recreated on redeployment and this resource will require a second apply to recreate the method settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApiGatewayMethodSettings",
    "Properties" : {
        "<a href="#methodpath" title="MethodPath">MethodPath</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#stagename" title="StageName">StageName</a>" : <i>String</i>,
        "<a href="#settings" title="Settings">Settings</a>" : <i>[ <a href="settingsdefinition.md">SettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApiGatewayMethodSettings
Properties:
    <a href="#methodpath" title="MethodPath">MethodPath</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#stagename" title="StageName">StageName</a>: <i>String</i>
    <a href="#settings" title="Settings">Settings</a>: <i>
      - <a href="settingsdefinition.md">SettingsDefinition</a></i>
</pre>

## Properties

#### MethodPath

Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*/*` for overriding all methods in the stage. Ensure to trim any leading forward slashes in the path (e.g. `trimprefix(aws_api_gateway_resource.example.path, "/")`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the REST API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageName

The name of the stage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of <a href="settingsdefinition.md">SettingsDefinition</a>

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

