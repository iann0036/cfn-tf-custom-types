# TF::FortiOS::RouterRip InterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authkeychain" title="AuthKeychain">AuthKeychain</a>" : <i>String</i>,
    "<a href="#authmode" title="AuthMode">AuthMode</a>" : <i>String</i>,
    "<a href="#authstring" title="AuthString">AuthString</a>" : <i>String</i>,
    "<a href="#flags" title="Flags">Flags</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#receiveversion" title="ReceiveVersion">ReceiveVersion</a>" : <i>String</i>,
    "<a href="#sendversion" title="SendVersion">SendVersion</a>" : <i>String</i>,
    "<a href="#sendversion2broadcast" title="SendVersion2Broadcast">SendVersion2Broadcast</a>" : <i>String</i>,
    "<a href="#splithorizon" title="SplitHorizon">SplitHorizon</a>" : <i>String</i>,
    "<a href="#splithorizonstatus" title="SplitHorizonStatus">SplitHorizonStatus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authkeychain" title="AuthKeychain">AuthKeychain</a>: <i>String</i>
<a href="#authmode" title="AuthMode">AuthMode</a>: <i>String</i>
<a href="#authstring" title="AuthString">AuthString</a>: <i>String</i>
<a href="#flags" title="Flags">Flags</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#receiveversion" title="ReceiveVersion">ReceiveVersion</a>: <i>String</i>
<a href="#sendversion" title="SendVersion">SendVersion</a>: <i>String</i>
<a href="#sendversion2broadcast" title="SendVersion2Broadcast">SendVersion2Broadcast</a>: <i>String</i>
<a href="#splithorizon" title="SplitHorizon">SplitHorizon</a>: <i>String</i>
<a href="#splithorizonstatus" title="SplitHorizonStatus">SplitHorizonStatus</a>: <i>String</i>
</pre>

## Properties

#### AuthKeychain

Authentication key-chain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthMode

Authentication mode. Valid values: `none`, `text`, `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthString

Authentication string/password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flags

flags.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveVersion

Receive version. Valid values: `1`, `2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendVersion

Send version. Valid values: `1`, `2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendVersion2Broadcast

Enable/disable broadcast version 1 compatible packets. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitHorizon

Enable/disable split horizon. Valid values: `poisoned`, `regular`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitHorizonStatus

Enable/disable split horizon. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

