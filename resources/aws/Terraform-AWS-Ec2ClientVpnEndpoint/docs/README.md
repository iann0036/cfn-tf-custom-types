# Terraform::AWS::Ec2ClientVpnEndpoint

CloudFormation equivalent of aws_ec2_client_vpn_endpoint

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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnel

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransportProtocol

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

