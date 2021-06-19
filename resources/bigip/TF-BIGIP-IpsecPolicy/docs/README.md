# TF::BIGIP::IpsecPolicy

`bigip_ipsec_policy` Manage IPSec policies on a BIG-IP

Resources should be named with their "full path". The full path is the combination of the partition + name (example: /Common/test-policy)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::IpsecPolicy",
    "Properties" : {
        "<a href="#authalgorithm" title="AuthAlgorithm">AuthAlgorithm</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encryptalgorithm" title="EncryptAlgorithm">EncryptAlgorithm</a>" : <i>String</i>,
        "<a href="#ipcomp" title="Ipcomp">Ipcomp</a>" : <i>String</i>,
        "<a href="#kblifetime" title="KbLifetime">KbLifetime</a>" : <i>Double</i>,
        "<a href="#lifetime" title="Lifetime">Lifetime</a>" : <i>Double</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#perfectforwardsecrecy" title="PerfectForwardSecrecy">PerfectForwardSecrecy</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#tunnellocaladdress" title="TunnelLocalAddress">TunnelLocalAddress</a>" : <i>String</i>,
        "<a href="#tunnelremoteaddress" title="TunnelRemoteAddress">TunnelRemoteAddress</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::IpsecPolicy
Properties:
    <a href="#authalgorithm" title="AuthAlgorithm">AuthAlgorithm</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encryptalgorithm" title="EncryptAlgorithm">EncryptAlgorithm</a>: <i>String</i>
    <a href="#ipcomp" title="Ipcomp">Ipcomp</a>: <i>String</i>
    <a href="#kblifetime" title="KbLifetime">KbLifetime</a>: <i>Double</i>
    <a href="#lifetime" title="Lifetime">Lifetime</a>: <i>Double</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#perfectforwardsecrecy" title="PerfectForwardSecrecy">PerfectForwardSecrecy</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#tunnellocaladdress" title="TunnelLocalAddress">TunnelLocalAddress</a>: <i>String</i>
    <a href="#tunnelremoteaddress" title="TunnelRemoteAddress">TunnelRemoteAddress</a>: <i>String</i>
</pre>

## Properties

#### AuthAlgorithm

Specifies the algorithm to use for IKE authentication. Valid choices are: `sha1, sha256, sha384, sha512, aes-gcm128,
aes-gcm192, aes-gcm256, aes-gmac128, aes-gmac192, aes-gmac256`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the IPSec policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptAlgorithm

Specifies the algorithm to use for IKE encryption. Valid choices are: `null, 3des, aes128, aes192, aes256, aes-gmac256,
aes-gmac192, aes-gmac128, aes-gcm256, aes-gcm192, aes-gcm256, aes-gcm128`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipcomp

Specifies whether to use IPComp encapsulation. Valid choices are: `none", null", deflate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KbLifetime

Specifies the length of time before the IKE security association expires, in kilobytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifetime

Specifies the length of time before the IKE security association expires, in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Specifies the processing mode. Valid choices are: `transport, interface, isession, tunnel`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the IPSec policy,it should be "full path".The full path is the combination of the partition + name of the IPSec policy.(For example `/Common/test-policy`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerfectForwardSecrecy

Specifies the Diffie-Hellman group to use for IKE Phase 2 negotiation. Valid choices are: `none, modp768, modp1024, modp1536, modp2048, modp3072,
modp4096, modp6144, modp8192`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Specifies the IPsec protocol. Valid choices are: `ah, esp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelLocalAddress

Specifies the local endpoint IP address of the IPsec tunnel. This parameter is only valid when mode is tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelRemoteAddress

Specifies the remote endpoint IP address of the IPsec tunnel. This parameter is only valid when mode is tunnel.

_Required_: No

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

