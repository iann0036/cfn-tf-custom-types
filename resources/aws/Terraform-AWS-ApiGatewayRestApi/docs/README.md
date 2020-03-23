# Terraform::AWS::ApiGatewayRestApi

Provides an API Gateway REST API.

-> **Note:** Amazon API Gateway Version 1 resources are used for creating and deploying REST APIs. To create and deploy WebSocket and HTTP APIs, use Amazon API Gateway Version 2 [resources](https://www.terraform.io/docs/providers/aws/r/apigatewayv2_api.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayRestApi",
    "Properties" : {
        "<a href="#apikeysource" title="ApiKeySource">ApiKeySource</a>" : <i>String</i>,
        "<a href="#binarymediatypes" title="BinaryMediaTypes">BinaryMediaTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#body" title="Body">Body</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#minimumcompressionsize" title="MinimumCompressionSize">MinimumCompressionSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>" : <i>[ <a href="endpointconfiguration.md">EndpointConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayRestApi
Properties:
    <a href="#apikeysource" title="ApiKeySource">ApiKeySource</a>: <i>String</i>
    <a href="#binarymediatypes" title="BinaryMediaTypes">BinaryMediaTypes</a>: <i>
      - String</i>
    <a href="#body" title="Body">Body</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#minimumcompressionsize" title="MinimumCompressionSize">MinimumCompressionSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>: <i>
      - <a href="endpointconfiguration.md">EndpointConfiguration</a></i>
</pre>

## Properties

#### ApiKeySource

The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BinaryMediaTypes

The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Body

An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the REST API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumCompressionSize

Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the REST API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

JSON formatted policy document that controls access to the API Gateway. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfiguration

_Required_: No

_Type_: List of <a href="endpointconfiguration.md">EndpointConfiguration</a>

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

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### ExecutionArn

Returns the <code>ExecutionArn</code> value.

#### Id

Returns the <code>Id</code> value.

#### RootResourceId

Returns the <code>RootResourceId</code> value.

