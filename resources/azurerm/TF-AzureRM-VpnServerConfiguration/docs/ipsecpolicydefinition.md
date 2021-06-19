# TF::AzureRM::VpnServerConfiguration IpsecPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dhgroup" title="DhGroup">DhGroup</a>" : <i>String</i>,
    "<a href="#ikeencryption" title="IkeEncryption">IkeEncryption</a>" : <i>String</i>,
    "<a href="#ikeintegrity" title="IkeIntegrity">IkeIntegrity</a>" : <i>String</i>,
    "<a href="#ipsecencryption" title="IpsecEncryption">IpsecEncryption</a>" : <i>String</i>,
    "<a href="#ipsecintegrity" title="IpsecIntegrity">IpsecIntegrity</a>" : <i>String</i>,
    "<a href="#pfsgroup" title="PfsGroup">PfsGroup</a>" : <i>String</i>,
    "<a href="#sadatasizekilobytes" title="SaDataSizeKilobytes">SaDataSizeKilobytes</a>" : <i>Double</i>,
    "<a href="#salifetimeseconds" title="SaLifetimeSeconds">SaLifetimeSeconds</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dhgroup" title="DhGroup">DhGroup</a>: <i>String</i>
<a href="#ikeencryption" title="IkeEncryption">IkeEncryption</a>: <i>String</i>
<a href="#ikeintegrity" title="IkeIntegrity">IkeIntegrity</a>: <i>String</i>
<a href="#ipsecencryption" title="IpsecEncryption">IpsecEncryption</a>: <i>String</i>
<a href="#ipsecintegrity" title="IpsecIntegrity">IpsecIntegrity</a>: <i>String</i>
<a href="#pfsgroup" title="PfsGroup">PfsGroup</a>: <i>String</i>
<a href="#sadatasizekilobytes" title="SaDataSizeKilobytes">SaDataSizeKilobytes</a>: <i>Double</i>
<a href="#salifetimeseconds" title="SaLifetimeSeconds">SaLifetimeSeconds</a>: <i>Double</i>
</pre>

## Properties

#### DhGroup

The DH Group, used in IKE Phase 1. Possible values include `DHGroup1`, `DHGroup2`, `DHGroup14`, `DHGroup24`, `DHGroup2048`, `ECP256`, `ECP384` and `None`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeEncryption

The IKE encryption algorithm, used for IKE Phase 2. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128` and `GCMAES256`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeIntegrity

The IKE encryption integrity algorithm, used for IKE Phase 2. Possible values include `GCMAES128`, `GCMAES256`, `MD5`, `SHA1`, `SHA256` and `SHA384`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncryption

The IPSec encryption algorithm, used for IKE phase 1. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256` and `None`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecIntegrity

The IPSec integrity algorithm, used for IKE phase 1. Possible values include `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1` and `SHA256`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PfsGroup

The Pfs Group, used in IKE Phase 2. Possible values include `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS14`, `PFS24`, `PFS2048`, `PFSMM` and `None`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaDataSizeKilobytes

The IPSec Security Association payload size in KB for a Site-to-Site VPN tunnel.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaLifetimeSeconds

The IPSec Security Association lifetime in seconds for a Site-to-Site VPN tunnel.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

