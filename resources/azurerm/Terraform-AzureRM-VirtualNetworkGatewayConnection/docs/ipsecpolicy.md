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

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeEncryption

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeIntegrity

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncryption

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecIntegrity

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PfsGroup

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaDatasize

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaLifetime

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

