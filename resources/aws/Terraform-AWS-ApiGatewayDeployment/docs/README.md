# Terraform::AWS::ApiGatewayDeployment

Provides an API Gateway REST Deployment.

-> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api (which in turn depends on `aws_api_gateway_method`). To avoid race conditions
you might need to add an explicit `depends_on = ["aws_api_gateway_integration.name"]`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayDeployment",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#stagedescription" title="StageDescription">StageDescription</a>" : <i>String</i>,
        "<a href="#stagename" title="StageName">StageName</a>" : <i>String</i>,
        "<a href="#variables" title="Variables">Variables</a>" : <i>[ <a href="variables.md">Variables</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayDeployment
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#stagedescription" title="StageDescription">StageDescription</a>: <i>String</i>
    <a href="#stagename" title="StageName">StageName</a>: <i>String</i>
    <a href="#variables" title="Variables">Variables</a>: <i>
      - <a href="variables.md">Variables</a></i>
</pre>

## Properties

#### Description

The description of the deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the associated REST API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageDescription

The description of the stage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageName

The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variables

A map that defines variables for the stage.

_Required_: No

_Type_: List of <a href="variables.md">Variables</a>

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

