# Terraform::AWS::Ec2ClientVpnEndpoint

Provides an AWS Client VPN endpoint for OpenVPN clients. For more information on usage, please see the
[AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Ec2ClientVpnEndpoint",
    "Properties" : {
        "<a href="#clientcidrblock" title="ClientCidrBlock">ClientCidrBlock</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dnsservers" title="DnsServers">DnsServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#servercertificatearn" title="ServerCertificateArn">ServerCertificateArn</a>" : <i>String</i>,
        "<a href="#splittunnel" title="SplitTunnel">SplitTunnel</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#transportprotocol" title="TransportProtocol">TransportProtocol</a>" : <i>String</i>,
        "<a href="#authenticationoptions" title="AuthenticationOptions">AuthenticationOptions</a>" : <i>[ <a href="authenticationoptions.md">AuthenticationOptions</a>, ... ]</i>,
        "<a href="#connectionlogoptions" title="ConnectionLogOptions">ConnectionLogOptions</a>" : <i>[ <a href="connectionlogoptions.md">ConnectionLogOptions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Ec2ClientVpnEndpoint
Properties:
    <a href="#clientcidrblock" title="ClientCidrBlock">ClientCidrBlock</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dnsservers" title="DnsServers">DnsServers</a>: <i>
      - String</i>
    <a href="#servercertificatearn" title="ServerCertificateArn">ServerCertificateArn</a>: <i>String</i>
    <a href="#splittunnel" title="SplitTunnel">SplitTunnel</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#transportprotocol" title="TransportProtocol">TransportProtocol</a>: <i>String</i>
    <a href="#authenticationoptions" title="AuthenticationOptions">AuthenticationOptions</a>: <i>
      - <a href="authenticationoptions.md">AuthenticationOptions</a></i>
    <a href="#connectionlogoptions" title="ConnectionLogOptions">ConnectionLogOptions</a>: <i>
      - <a href="connectionlogoptions.md">ConnectionLogOptions</a></i>
</pre>

## Properties

#### ClientCidrBlock

The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Name of the repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServers

Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateArn

The ARN of the ACM server certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnel

Indicates whether split-tunnel is enabled on VPN endpoint. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransportProtocol

The transport protocol to be used by the VPN session. Default value is `udp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationOptions

_Required_: No

_Type_: List of <a href="authenticationoptions.md">AuthenticationOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionLogOptions

_Required_: No

_Type_: List of <a href="connectionlogoptions.md">ConnectionLogOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DnsName

Returns the <code>DnsName</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

