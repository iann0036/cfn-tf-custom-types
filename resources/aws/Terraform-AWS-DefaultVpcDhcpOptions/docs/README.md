# Terraform::AWS::DefaultVpcDhcpOptions

Provides a resource to manage the [default AWS DHCP Options Set](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html#AmazonDNS)
in the current region.

Each AWS region comes with a default set of DHCP options.
**This is an advanced resource**, and has special caveats to be aware of when
using it. Please read this document in its entirety before using this resource.

The `aws_default_vpc_dhcp_options` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DefaultVpcDhcpOptions",
    "Properties" : {
        "<a href="#netbiosnameservers" title="NetbiosNameServers">NetbiosNameServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#netbiosnodetype" title="NetbiosNodeType">NetbiosNodeType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DefaultVpcDhcpOptions
Properties:
    <a href="#netbiosnameservers" title="NetbiosNameServers">NetbiosNameServers</a>: <i>
      - String</i>
    <a href="#netbiosnodetype" title="NetbiosNodeType">NetbiosNodeType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### NetbiosNameServers

List of NETBIOS name servers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetbiosNodeType

The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

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

#### DomainName

Returns the <code>DomainName</code> value.

#### DomainNameServers

Returns the <code>DomainNameServers</code> value.

#### Id

Returns the <code>Id</code> value.

#### NtpServers

Returns the <code>NtpServers</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

