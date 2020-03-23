# Terraform::AWS::Vpc

Provides a VPC resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Vpc",
    "Properties" : {
        "<a href="#assigngeneratedipv6cidrblock" title="AssignGeneratedIpv6CidrBlock">AssignGeneratedIpv6CidrBlock</a>" : <i>Boolean</i>,
        "<a href="#cidrblock" title="CidrBlock">CidrBlock</a>" : <i>String</i>,
        "<a href="#enableclassiclink" title="EnableClassiclink">EnableClassiclink</a>" : <i>Boolean</i>,
        "<a href="#enableclassiclinkdnssupport" title="EnableClassiclinkDnsSupport">EnableClassiclinkDnsSupport</a>" : <i>Boolean</i>,
        "<a href="#enablednshostnames" title="EnableDnsHostnames">EnableDnsHostnames</a>" : <i>Boolean</i>,
        "<a href="#enablednssupport" title="EnableDnsSupport">EnableDnsSupport</a>" : <i>Boolean</i>,
        "<a href="#instancetenancy" title="InstanceTenancy">InstanceTenancy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Vpc
Properties:
    <a href="#assigngeneratedipv6cidrblock" title="AssignGeneratedIpv6CidrBlock">AssignGeneratedIpv6CidrBlock</a>: <i>Boolean</i>
    <a href="#cidrblock" title="CidrBlock">CidrBlock</a>: <i>String</i>
    <a href="#enableclassiclink" title="EnableClassiclink">EnableClassiclink</a>: <i>Boolean</i>
    <a href="#enableclassiclinkdnssupport" title="EnableClassiclinkDnsSupport">EnableClassiclinkDnsSupport</a>: <i>Boolean</i>
    <a href="#enablednshostnames" title="EnableDnsHostnames">EnableDnsHostnames</a>: <i>Boolean</i>
    <a href="#enablednssupport" title="EnableDnsSupport">EnableDnsSupport</a>: <i>Boolean</i>
    <a href="#instancetenancy" title="InstanceTenancy">InstanceTenancy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### AssignGeneratedIpv6CidrBlock

Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlock

The CIDR block for the VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClassiclink

A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClassiclinkDnsSupport

A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.

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

#### InstanceTenancy

A tenancy option for instances launched into the VPC.

_Required_: No

_Type_: String

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

#### Ipv6AssociationId

Returns the <code>Ipv6AssociationId</code> value.

#### Ipv6CidrBlock

Returns the <code>Ipv6CidrBlock</code> value.

#### MainRouteTableId

Returns the <code>MainRouteTableId</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

