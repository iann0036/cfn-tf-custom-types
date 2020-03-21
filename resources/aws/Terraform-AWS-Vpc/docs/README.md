# Terraform::AWS::Vpc

CloudFormation equivalent of aws_vpc

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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlock

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClassiclink

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClassiclinkDnsSupport

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDnsHostnames

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDnsSupport

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTenancy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

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

#### Ipv6AssociationId

Returns the <code>Ipv6AssociationId</code> value.

#### Ipv6CidrBlock

Returns the <code>Ipv6CidrBlock</code> value.

#### MainRouteTableId

Returns the <code>MainRouteTableId</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

