# TF::MongoDBAtlas::PrivatelinkEndpointService

`mongodbatlas_privatelink_endpoint_service` provides a Private Endpoint Interface Link resource. This represents a Private Endpoint Interface Link, which adds one interface endpoint to a private endpoint connection in an Atlas project.

~> **IMPORTANT:**You must have one of the following roles to successfully handle the resource:
  * Organization Owner
  * Project Owner

-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::PrivatelinkEndpointService",
    "Properties" : {
        "<a href="#endpointserviceid" title="EndpointServiceId">EndpointServiceId</a>" : <i>String</i>,
        "<a href="#privateendpointipaddress" title="PrivateEndpointIpAddress">PrivateEndpointIpAddress</a>" : <i>String</i>,
        "<a href="#privatelinkid" title="PrivateLinkId">PrivateLinkId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::PrivatelinkEndpointService
Properties:
    <a href="#endpointserviceid" title="EndpointServiceId">EndpointServiceId</a>: <i>String</i>
    <a href="#privateendpointipaddress" title="PrivateEndpointIpAddress">PrivateEndpointIpAddress</a>: <i>String</i>
    <a href="#privatelinkid" title="PrivateLinkId">PrivateLinkId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
</pre>

## Properties

#### EndpointServiceId

Unique identifier of the interface endpoint you created in your VPC with the `AWS` or `AZURE` resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEndpointIpAddress

Private IP address of the private endpoint network interface you created in your Azure VNet. Only for `AZURE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateLinkId

Unique identifier of the `AWS` or `AZURE` PrivateLink connection which is created by `mongodbatlas_privatelink_endpoint` resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Unique identifier for the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

Cloud provider for which you want to create a private endpoint. Atlas accepts `AWS` or `AZURE`.

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

#### AwsConnectionStatus

Returns the <code>AwsConnectionStatus</code> value.

#### AzureStatus

Returns the <code>AzureStatus</code> value.

#### DeleteRequested

Returns the <code>DeleteRequested</code> value.

#### ErrorMessage

Returns the <code>ErrorMessage</code> value.

#### Id

Returns the <code>Id</code> value.

#### InterfaceEndpointId

Returns the <code>InterfaceEndpointId</code> value.

#### PrivateEndpointConnectionName

Returns the <code>PrivateEndpointConnectionName</code> value.

#### PrivateEndpointResourceId

Returns the <code>PrivateEndpointResourceId</code> value.

