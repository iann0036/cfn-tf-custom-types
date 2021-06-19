# TF::MongoDBAtlas::NetworkContainer

`mongodbatlas_network_container` provides a Network Peering Container resource. The resource lets you create, edit and delete network peering containers. The resource requires your Project ID.  Each cloud provider requires slightly different attributes so read the argument reference carefully. 

 Network peering container is a general term used to describe any cloud providers' VPC/VNet concept.  Containers only need to be created if the peering connection to the cloud provider will be created before the first cluster that requires the container.  If the cluster has been/will be created first Atlas automatically creates the required container per the "containers per cloud provider" information that follows (in this case you can obtain the container id from the cluster resource attribute `container_id`).
 
The following is the maximum number of Network Peering containers per cloud provider:
<br> &#8226;  GCP -  One container per project.
<br> &#8226;  AWS and Azure - One container per cloud provider region....

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::NetworkContainer",
    "Properties" : {
        "<a href="#atlascidrblock" title="AtlasCidrBlock">AtlasCidrBlock</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#regionname" title="RegionName">RegionName</a>" : <i>String</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::NetworkContainer
Properties:
    <a href="#atlascidrblock" title="AtlasCidrBlock">AtlasCidrBlock</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#regionname" title="RegionName">RegionName</a>: <i>String</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
</pre>

## Properties

#### AtlasCidrBlock

CIDR block that Atlas uses for the Network Peering containers in your project.  Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following [private networks](https://tools.ietf.org/html/rfc1918.html#section-3):
* Lower bound: 10.0.0.0 -	Upper bound: 10.255.255.255 -	Prefix: 10/8
* Lower bound: 172.16.0.0 -	Upper bound:172.31.255.255 -	Prefix:	172.16/12
* Lower bound: 192.168.0.0 -	Upper bound:192.168.255.255 -	Prefix:	192.168/16.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Unique identifier for the Atlas project for this Network Peering Container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

Cloud provider for this Network Peering connection.  Accepted values are GCP, AWS, AZURE. If omitted, Atlas sets this parameter to AWS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Atlas region where the container resides, see the reference list for Atlas Azure region names [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionName

The Atlas AWS region name for where this container will exist, see the reference list for Atlas AWS region names [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

Atlas regions where the container resides. Provide this field only if you provide an `atlas_cidr_block` smaller than `/18`. [GCP Regions values](https://docs.atlas.mongodb.com/reference/api/vpc-create-container/#request-body-parameters).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AzureSubscriptionId

Returns the <code>AzureSubscriptionId</code> value.

#### ContainerId

Returns the <code>ContainerId</code> value.

#### GcpProjectId

Returns the <code>GcpProjectId</code> value.

#### Id

Returns the <code>Id</code> value.

#### NetworkName

Returns the <code>NetworkName</code> value.

#### Provisioned

Returns the <code>Provisioned</code> value.

#### VnetName

Returns the <code>VnetName</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

