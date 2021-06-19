# TF::MongoDBAtlas::PrivatelinkEndpoint

`mongodbatlas_privatelink_endpoint` provides a Private Endpoint resource. This represents a Private Endpoint Service that can be created in an Atlas project.

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
    "Type" : "TF::MongoDBAtlas::PrivatelinkEndpoint",
    "Properties" : {
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::PrivatelinkEndpoint
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
Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws) and [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure).

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

#### PrivateEndpoints

Returns the <code>PrivateEndpoints</code> value.

#### PrivateLinkId

Returns the <code>PrivateLinkId</code> value.

#### PrivateLinkServiceName

Returns the <code>PrivateLinkServiceName</code> value.

#### PrivateLinkServiceResourceId

Returns the <code>PrivateLinkServiceResourceId</code> value.

#### Status

Returns the <code>Status</code> value.

