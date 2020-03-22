# Terraform::Google::EndpointsService

This resource creates and rolls out a Cloud Endpoints service using OpenAPI or gRPC.  View the relevant docs for [OpenAPI](https://cloud.google.com/endpoints/docs/openapi/) and [gRPC](https://cloud.google.com/endpoints/docs/grpc/).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::EndpointsService",
    "Properties" : {
        "<a href="#grpcconfig" title="GrpcConfig">GrpcConfig</a>" : <i>String</i>,
        "<a href="#openapiconfig" title="OpenapiConfig">OpenapiConfig</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#protocoutputbase64" title="ProtocOutputBase64">ProtocOutputBase64</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::EndpointsService
Properties:
    <a href="#grpcconfig" title="GrpcConfig">GrpcConfig</a>: <i>String</i>
    <a href="#openapiconfig" title="OpenapiConfig">OpenapiConfig</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#protocoutputbase64" title="ProtocOutputBase64">ProtocOutputBase64</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### GrpcConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenapiConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocOutputBase64

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Apis

Returns the <code>Apis</code> value.

#### ConfigId

Returns the <code>ConfigId</code> value.

#### DnsAddress

Returns the <code>DnsAddress</code> value.

#### Endpoints

Returns the <code>Endpoints</code> value.

#### Id

Returns the <code>Id</code> value.

