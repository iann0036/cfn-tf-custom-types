# TF::MongoDBAtlas::CustomDnsConfigurationClusterAws

`mongodbatlas_custom_dns_configuration_cluster_aws` provides a Custom DNS Configuration for Atlas Clusters on AWS resource. This represents a Custom DNS Configuration for Atlas Clusters on AWS that can be updated in an Atlas project.

~> **IMPORTANT:**You must have one of the following roles to successfully handle the resource:
  * Organization Owner
  * Project Owner

-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::CustomDnsConfigurationClusterAws",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::CustomDnsConfigurationClusterAws
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Indicates whether the project's clusters deployed to AWS use custom DNS. If `true`, the `Get All Clusters` and `Get One Cluster` endpoints return the `connectionStrings.private` and `connectionStrings.privateSrv` fields for clusters deployed to AWS .

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Required 	Unique identifier for the project.

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

#### Id

Returns the <code>Id</code> value.

