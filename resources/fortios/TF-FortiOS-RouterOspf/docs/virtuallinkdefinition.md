# TF::FortiOS::RouterOspf VirtualLinkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
    "<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>" : <i>String</i>,
    "<a href="#deadinterval" title="DeadInterval">DeadInterval</a>" : <i>Double</i>,
    "<a href="#hellointerval" title="HelloInterval">HelloInterval</a>" : <i>Double</i>,
    "<a href="#md5key" title="Md5Key">Md5Key</a>" : <i>String</i>,
    "<a href="#md5keychain" title="Md5Keychain">Md5Keychain</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#peer" title="Peer">Peer</a>" : <i>String</i>,
    "<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>" : <i>Double</i>,
    "<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>" : <i>Double</i>,
    "<a href="#md5keys" title="Md5Keys">Md5Keys</a>" : <i>[ <a href="md5keysdefinition.md">Md5KeysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>: <i>String</i>
<a href="#deadinterval" title="DeadInterval">DeadInterval</a>: <i>Double</i>
<a href="#hellointerval" title="HelloInterval">HelloInterval</a>: <i>Double</i>
<a href="#md5key" title="Md5Key">Md5Key</a>: <i>String</i>
<a href="#md5keychain" title="Md5Keychain">Md5Keychain</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#peer" title="Peer">Peer</a>: <i>String</i>
<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>: <i>Double</i>
<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>: <i>Double</i>
<a href="#md5keys" title="Md5Keys">Md5Keys</a>: <i>
      - <a href="md5keysdefinition.md">Md5KeysDefinition</a></i>
</pre>

## Properties

#### Authentication

Authentication type. Valid values: `none`, `text`, `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationKey

Authentication key.

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

#### Md5Key

MD5 key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5Keychain

Authentication MD5 key-chain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Virtual link entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peer

Peer IP.

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

#### Md5Keys

_Required_: No

_Type_: List of <a href="md5keysdefinition.md">Md5KeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

