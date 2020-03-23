# Terraform::AWS::DefaultVpc

Provides a resource to manage the [default AWS VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html)
in the current region.

For AWS accounts created after 2013-12-04, each region comes with a Default VPC.
**This is an advanced resource**, and has special caveats to be aware of when
using it. Please read this document in its entirety before using this resource.

The `aws_default_vpc` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DefaultVpc",
    "Properties" : {
        "<a href="#enableclassiclink" title="EnableClassiclink">EnableClassiclink</a>" : <i>Boolean</i>,
        "<a href="#enableclassiclinkdnssupport" title="EnableClassiclinkDnsSupport">EnableClassiclinkDnsSupport</a>" : <i>Boolean</i>,
        "<a href="#enablednshostnames" title="EnableDnsHostnames">EnableDnsHostnames</a>" : <i>Boolean</i>,
        "<a href="#enablednssupport" title="EnableDnsSupport">EnableDnsSupport</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DefaultVpc
Properties:
    <a href="#enableclassiclink" title="EnableClassiclink">EnableClassiclink</a>: <i>Boolean</i>
    <a href="#enableclassiclinkdnssupport" title="EnableClassiclinkDnsSupport">EnableClassiclinkDnsSupport</a>: <i>Boolean</i>
    <a href="#enablednshostnames" title="EnableDnsHostnames">EnableDnsHostnames</a>: <i>Boolean</i>
    <a href="#enablednssupport" title="EnableDnsSupport">EnableDnsSupport</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### EnableClassiclink

A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClassiclinkDnsSupport

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDnsHostnames

A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDnsSupport

A boolean flag to enable/disable DNS support in the VPC. Defaults true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

#### AssignGeneratedIpv6CidrBlock

Returns the <code>AssignGeneratedIpv6CidrBlock</code> value.

#### CidrBlock

Returns the <code>CidrBlock</code> value.

#### DefaultNetworkAclId

Returns the <code>DefaultNetworkAclId</code> value.

#### DefaultRouteTableId

Returns the <code>DefaultRouteTableId</code> value.

#### DefaultSecurityGroupId

Returns the <code>DefaultSecurityGroupId</code> value.

#### DhcpOptionsId

Returns the <code>DhcpOptionsId</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceTenancy

Returns the <code>InstanceTenancy</code> value.

#### Ipv6AssociationId

Returns the <code>Ipv6AssociationId</code> value.

#### Ipv6CidrBlock

Returns the <code>Ipv6CidrBlock</code> value.

#### MainRouteTableId

Returns the <code>MainRouteTableId</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

