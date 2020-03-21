# Terraform::UCloud::VpnConnection IkeConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationalgorithm" title="AuthenticationAlgorithm">AuthenticationAlgorithm</a>" : <i>String</i>,
    "<a href="#dhgroup" title="DhGroup">DhGroup</a>" : <i>String</i>,
    "<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>" : <i>String</i>,
    "<a href="#exchangemode" title="ExchangeMode">ExchangeMode</a>" : <i>String</i>,
    "<a href="#ikeversion" title="IkeVersion">IkeVersion</a>" : <i>String</i>,
    "<a href="#localid" title="LocalId">LocalId</a>" : <i>String</i>,
    "<a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>" : <i>String</i>,
    "<a href="#remoteid" title="RemoteId">RemoteId</a>" : <i>String</i>,
    "<a href="#salifetime" title="SaLifeTime">SaLifeTime</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationalgorithm" title="AuthenticationAlgorithm">AuthenticationAlgorithm</a>: <i>String</i>
<a href="#dhgroup" title="DhGroup">DhGroup</a>: <i>String</i>
<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>: <i>String</i>
<a href="#exchangemode" title="ExchangeMode">ExchangeMode</a>: <i>String</i>
<a href="#ikeversion" title="IkeVersion">IkeVersion</a>: <i>String</i>
<a href="#localid" title="LocalId">LocalId</a>: <i>String</i>
<a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>: <i>String</i>
<a href="#remoteid" title="RemoteId">RemoteId</a>: <i>String</i>
<a href="#salifetime" title="SaLifeTime">SaLifeTime</a>: <i>Double</i>
</pre>

## Properties

#### AuthenticationAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExchangeMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSharedKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaLifeTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

