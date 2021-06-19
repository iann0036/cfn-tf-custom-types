# TF::MongoDBAtlas::PrivateEndpoint

`mongodbatlas_private_endpoint` provides a Private Endpoint resource. This represents a Private Endpoint Connection that can be created in an Atlas project.

!> **WARNING:** This resource is deprecated and will be removed in the next major version
                Please transition to privatelink_endpoint as soon as possible. [PrivateLink Endpoints] (https://docs.atlas.mongodb.com/reference/api/private-endpoints/)

~> **IMPORTANT:**You must have one of the following roles to successfully handle the resource:
  * Organization Owner
  * Project Owner

-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

-> **NOTE:** A network container is created for a private endpoint to reside in if one does not yet exist in the project.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::PrivateEndpoint",
    "Properties" : {
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::PrivateEndpoint
Properties:
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### ProjectId

Required 	Unique identifier for the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Cloud provider region in which you want to create the private endpoint connection.
Accepted values are:
* `us-east-1`
* `us-east-2`
* `us-west-1`
* `us-west-2`
* `ca-central-1`
* `sa-east-1`
* `eu-north-1`
* `eu-west-1`
* `eu-west-2`
* `eu-west-3`
* `eu-central-1`
* `me-south-1`
* `ap-northeast-1`
* `ap-northeast-2`
* `ap-south-1`
* `ap-southeast-1`
* `ap-southeast-2`
* `ap-east-1`.

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

#### EndpointServiceName

Returns the <code>EndpointServiceName</code> value.

#### ErrorMessage

Returns the <code>ErrorMessage</code> value.

#### Id

Returns the <code>Id</code> value.

#### InterfaceEndpoints

Returns the <code>InterfaceEndpoints</code> value.

#### PrivateLinkId

Returns the <code>PrivateLinkId</code> value.

#### Status

Returns the <code>Status</code> value.

