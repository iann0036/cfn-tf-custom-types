# Terraform::VCD::EdgegatewayVpn

Provides a vCloud Director IPsec VPN. This can be used to create,
modify, and delete VPN settings and rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::EdgegatewayVpn",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#encryptionprotocol" title="EncryptionProtocol">EncryptionProtocol</a>" : <i>String</i>,
        "<a href="#localid" title="LocalId">LocalId</a>" : <i>String</i>,
        "<a href="#localipaddress" title="LocalIpAddress">LocalIpAddress</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#peerid" title="PeerId">PeerId</a>" : <i>String</i>,
        "<a href="#peeripaddress" title="PeerIpAddress">PeerIpAddress</a>" : <i>String</i>,
        "<a href="#sharedsecret" title="SharedSecret">SharedSecret</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#localsubnets" title="LocalSubnets">LocalSubnets</a>" : <i>[ <a href="localsubnets.md">LocalSubnets</a>, ... ]</i>,
        "<a href="#peersubnets" title="PeerSubnets">PeerSubnets</a>" : <i>[ <a href="peersubnets.md">PeerSubnets</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::EdgegatewayVpn
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#encryptionprotocol" title="EncryptionProtocol">EncryptionProtocol</a>: <i>String</i>
    <a href="#localid" title="LocalId">LocalId</a>: <i>String</i>
    <a href="#localipaddress" title="LocalIpAddress">LocalIpAddress</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#peerid" title="PeerId">PeerId</a>: <i>String</i>
    <a href="#peeripaddress" title="PeerIpAddress">PeerIpAddress</a>: <i>String</i>
    <a href="#sharedsecret" title="SharedSecret">SharedSecret</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#localsubnets" title="LocalSubnets">LocalSubnets</a>: <i>
      - <a href="localsubnets.md">LocalSubnets</a></i>
    <a href="#peersubnets" title="PeerSubnets">PeerSubnets</a>: <i>
      - <a href="peersubnets.md">PeerSubnets</a></i>
</pre>

## Properties

#### Description

A description for the VPN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeGateway

The name of the edge gateway on which to apply the Firewall Rules.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionProtocol

- E.g. `AES256`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalId

- Local ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpAddress

- Local IP Address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

- The MTU setting.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the VPN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerId

- Peer ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIpAddress

- Peer IP Address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedSecret

- Shared Secret.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSubnets

_Required_: No

_Type_: List of <a href="localsubnets.md">LocalSubnets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerSubnets

_Required_: No

_Type_: List of <a href="peersubnets.md">PeerSubnets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

