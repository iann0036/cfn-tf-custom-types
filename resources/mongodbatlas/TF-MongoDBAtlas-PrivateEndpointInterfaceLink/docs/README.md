# TF::MongoDBAtlas::PrivateEndpointInterfaceLink

`mongodbatlas_private_endpoint_interface_link` provides a Private Endpoint Interface Link resource. This represents a Private Endpoint Interface Link, which adds one interface endpoint to a private endpoint connection in an Atlas project.

!> **WARNING:** This resource is deprecated and will be removed in the next major version
                Please transition to privatelink_endpoint_service as soon as possible. [PrivateLink Endpoints] (https://docs.atlas.mongodb.com/reference/api/private-endpoints-endpoint-create-one/)

~> **IMPORTANT:**You must have one of the following roles to successfully handle the resource:
  * Organization Owner
  * Project Owner

-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::PrivateEndpointInterfaceLink",
    "Properties" : {
        "<a href="#interfaceendpointid" title="InterfaceEndpointId">InterfaceEndpointId</a>" : <i>String</i>,
        "<a href="#privatelinkid" title="PrivateLinkId">PrivateLinkId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::PrivateEndpointInterfaceLink
Properties:
    <a href="#interfaceendpointid" title="InterfaceEndpointId">InterfaceEndpointId</a>: <i>String</i>
    <a href="#privatelinkid" title="PrivateLinkId">PrivateLinkId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
</pre>

## Properties

#### InterfaceEndpointId

Unique identifier of the interface endpoint you created in your VPC with the AWS resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateLinkId

Unique identifier of the AWS PrivateLink connection which is created by `mongodbatlas_private_endpoint` resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Unique identifier for the project.

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

#### ConnectionStatus

Returns the <code>ConnectionStatus</code> value.

#### DeleteRequested

Returns the <code>DeleteRequested</code> value.

#### ErrorMessage

Returns the <code>ErrorMessage</code> value.

#### Id

Returns the <code>Id</code> value.

