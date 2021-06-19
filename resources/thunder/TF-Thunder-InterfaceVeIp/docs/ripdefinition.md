# TF::Thunder::InterfaceVeIp RipDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#receivepacket" title="ReceivePacket">ReceivePacket</a>" : <i>Double</i>,
    "<a href="#sendpacket" title="SendPacket">SendPacket</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authenticationdefinition.md">AuthenticationDefinition</a>, ... ]</i>,
    "<a href="#receivecfg" title="ReceiveCfg">ReceiveCfg</a>" : <i>[ <a href="receivecfgdefinition.md">ReceiveCfgDefinition</a>, ... ]</i>,
    "<a href="#sendcfg" title="SendCfg">SendCfg</a>" : <i>[ <a href="sendcfgdefinition.md">SendCfgDefinition</a>, ... ]</i>,
    "<a href="#splithorizoncfg" title="SplitHorizonCfg">SplitHorizonCfg</a>" : <i>[ <a href="splithorizoncfgdefinition.md">SplitHorizonCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#receivepacket" title="ReceivePacket">ReceivePacket</a>: <i>Double</i>
<a href="#sendpacket" title="SendPacket">SendPacket</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authenticationdefinition.md">AuthenticationDefinition</a></i>
<a href="#receivecfg" title="ReceiveCfg">ReceiveCfg</a>: <i>
      - <a href="receivecfgdefinition.md">ReceiveCfgDefinition</a></i>
<a href="#sendcfg" title="SendCfg">SendCfg</a>: <i>
      - <a href="sendcfgdefinition.md">SendCfgDefinition</a></i>
<a href="#splithorizoncfg" title="SplitHorizonCfg">SplitHorizonCfg</a>: <i>
      - <a href="splithorizoncfgdefinition.md">SplitHorizonCfgDefinition</a></i>
</pre>

## Properties

#### ReceivePacket

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendPacket

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authenticationdefinition.md">AuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveCfg

_Required_: No

_Type_: List of <a href="receivecfgdefinition.md">ReceiveCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCfg

_Required_: No

_Type_: List of <a href="sendcfgdefinition.md">SendCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitHorizonCfg

_Required_: No

_Type_: List of <a href="splithorizoncfgdefinition.md">SplitHorizonCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

