# Terraform::AWS::DefaultVpc

CloudFormation equivalent of aws_default_vpc

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
</pre>

## Properties

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

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### AssignGeneratedIpv6CidrBlock

Returns the &lt;code&gt;AssignGeneratedIpv6CidrBlock&lt;/code&gt; value.

#### CidrBlock

Returns the &lt;code&gt;CidrBlock&lt;/code&gt; value.

#### DefaultNetworkAclId

Returns the &lt;code&gt;DefaultNetworkAclId&lt;/code&gt; value.

#### DefaultRouteTableId

Returns the &lt;code&gt;DefaultRouteTableId&lt;/code&gt; value.

#### DefaultSecurityGroupId

Returns the &lt;code&gt;DefaultSecurityGroupId&lt;/code&gt; value.

#### DhcpOptionsId

Returns the &lt;code&gt;DhcpOptionsId&lt;/code&gt; value.

#### InstanceTenancy

Returns the &lt;code&gt;InstanceTenancy&lt;/code&gt; value.

#### Ipv6AssociationId

Returns the &lt;code&gt;Ipv6AssociationId&lt;/code&gt; value.

#### Ipv6CidrBlock

Returns the &lt;code&gt;Ipv6CidrBlock&lt;/code&gt; value.

#### MainRouteTableId

Returns the &lt;code&gt;MainRouteTableId&lt;/code&gt; value.

#### OwnerId

Returns the &lt;code&gt;OwnerId&lt;/code&gt; value.

