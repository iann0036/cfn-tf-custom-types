# Terraform::AzureRM::VirtualNetworkGatewayConnection IpsecPolicy

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
    "<a href="#sadatasize" title="SaDatasize">SaDatasize</a>" : <i>Double</i>,
    "<a href="#salifetime" title="SaLifetime">SaLifetime</a>" : <i>Double</i>
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
<a href="#sadatasize" title="SaDatasize">SaDatasize</a>: <i>Double</i>
<a href="#salifetime" title="SaLifetime">SaLifetime</a>: <i>Double</i>
</pre>

## Properties

#### DhGroup

The DH group used in IKE phase 1 for initial SA. Valid
options are `DHGroup1`, `DHGroup14`, `DHGroup2`, `DHGroup2048`, `DHGroup24`,
`ECP256`, `ECP384`, or `None`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeEncryption

The IKE encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, or `DES3`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeIntegrity

The IKE integrity algorithm. Valid
options are `MD5`, `SHA1`, `SHA256`, or `SHA384`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncryption

The IPSec encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256`, or `None`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecIntegrity

The IPSec integrity algorithm. Valid
options are `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1`, or `SHA256`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PfsGroup

The DH group used in IKE phase 2 for new child SA.
Valid options are `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS2048`, `PFS24`,
or `None`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaDatasize

The IPSec SA payload size in KB. Must be at least
`1024` KB. Defaults to `102400000` KB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaLifetime

The IPSec SA lifetime in seconds. Must be at least
`300` seconds. Defaults to `27000` seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

