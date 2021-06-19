# TF::FortiOS::RouterOspf6 VirtualLinkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
    "<a href="#deadinterval" title="DeadInterval">DeadInterval</a>" : <i>Double</i>,
    "<a href="#hellointerval" title="HelloInterval">HelloInterval</a>" : <i>Double</i>,
    "<a href="#ipsecauthalg" title="IpsecAuthAlg">IpsecAuthAlg</a>" : <i>String</i>,
    "<a href="#ipsecencalg" title="IpsecEncAlg">IpsecEncAlg</a>" : <i>String</i>,
    "<a href="#keyrolloverinterval" title="KeyRolloverInterval">KeyRolloverInterval</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#peer" title="Peer">Peer</a>" : <i>String</i>,
    "<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>" : <i>Double</i>,
    "<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>" : <i>Double</i>,
    "<a href="#ipseckeys" title="IpsecKeys">IpsecKeys</a>" : <i>[ <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
<a href="#deadinterval" title="DeadInterval">DeadInterval</a>: <i>Double</i>
<a href="#hellointerval" title="HelloInterval">HelloInterval</a>: <i>Double</i>
<a href="#ipsecauthalg" title="IpsecAuthAlg">IpsecAuthAlg</a>: <i>String</i>
<a href="#ipsecencalg" title="IpsecEncAlg">IpsecEncAlg</a>: <i>String</i>
<a href="#keyrolloverinterval" title="KeyRolloverInterval">KeyRolloverInterval</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#peer" title="Peer">Peer</a>: <i>String</i>
<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>: <i>Double</i>
<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>: <i>Double</i>
<a href="#ipseckeys" title="IpsecKeys">IpsecKeys</a>: <i>
      - <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a></i>
</pre>

## Properties

#### Authentication

Authentication mode. Valid values: `none`, `ah`, `esp`, `area`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadInterval

Dead interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloInterval

Hello interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecAuthAlg

Authentication algorithm. Valid values: `md5`, `sha1`, `sha256`, `sha384`, `sha512`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncAlg

Encryption algorithm. Valid values: `null`, `des`, `3des`, `aes128`, `aes192`, `aes256`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyRolloverInterval

Key roll-over interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Virtual link entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peer

A.B.C.D, peer router ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetransmitInterval

Retransmit interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransmitDelay

Transmit delay.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecKeys

_Required_: No

_Type_: List of <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

