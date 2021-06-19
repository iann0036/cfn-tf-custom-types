# TF::Thunder::InterfaceVeIp OspfGlobalDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>" : <i>String</i>,
    "<a href="#cost" title="Cost">Cost</a>" : <i>Double</i>,
    "<a href="#deadinterval" title="DeadInterval">DeadInterval</a>" : <i>Double</i>,
    "<a href="#disable" title="Disable">Disable</a>" : <i>String</i>,
    "<a href="#hellointerval" title="HelloInterval">HelloInterval</a>" : <i>Double</i>,
    "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
    "<a href="#mtuignore" title="MtuIgnore">MtuIgnore</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>" : <i>Double</i>,
    "<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#authenticationcfg" title="AuthenticationCfg">AuthenticationCfg</a>" : <i>[ <a href="authenticationcfgdefinition.md">AuthenticationCfgDefinition</a>, ... ]</i>,
    "<a href="#bfdcfg" title="BfdCfg">BfdCfg</a>" : <i>[ <a href="bfdcfgdefinition.md">BfdCfgDefinition</a>, ... ]</i>,
    "<a href="#databasefiltercfg" title="DatabaseFilterCfg">DatabaseFilterCfg</a>" : <i>[ <a href="databasefiltercfgdefinition.md">DatabaseFilterCfgDefinition</a>, ... ]</i>,
    "<a href="#messagedigestcfg" title="MessageDigestCfg">MessageDigestCfg</a>" : <i>[ <a href="messagedigestcfgdefinition.md">MessageDigestCfgDefinition</a>, ... ]</i>,
    "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>: <i>String</i>
<a href="#cost" title="Cost">Cost</a>: <i>Double</i>
<a href="#deadinterval" title="DeadInterval">DeadInterval</a>: <i>Double</i>
<a href="#disable" title="Disable">Disable</a>: <i>String</i>
<a href="#hellointerval" title="HelloInterval">HelloInterval</a>: <i>Double</i>
<a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
<a href="#mtuignore" title="MtuIgnore">MtuIgnore</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#retransmitinterval" title="RetransmitInterval">RetransmitInterval</a>: <i>Double</i>
<a href="#transmitdelay" title="TransmitDelay">TransmitDelay</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#authenticationcfg" title="AuthenticationCfg">AuthenticationCfg</a>: <i>
      - <a href="authenticationcfgdefinition.md">AuthenticationCfgDefinition</a></i>
<a href="#bfdcfg" title="BfdCfg">BfdCfg</a>: <i>
      - <a href="bfdcfgdefinition.md">BfdCfgDefinition</a></i>
<a href="#databasefiltercfg" title="DatabaseFilterCfg">DatabaseFilterCfg</a>: <i>
      - <a href="databasefiltercfgdefinition.md">DatabaseFilterCfgDefinition</a></i>
<a href="#messagedigestcfg" title="MessageDigestCfg">MessageDigestCfg</a>: <i>
      - <a href="messagedigestcfgdefinition.md">MessageDigestCfgDefinition</a></i>
<a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
</pre>

## Properties

#### AuthenticationKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cost

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MtuIgnore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetransmitInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransmitDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationCfg

_Required_: No

_Type_: List of <a href="authenticationcfgdefinition.md">AuthenticationCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdCfg

_Required_: No

_Type_: List of <a href="bfdcfgdefinition.md">BfdCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseFilterCfg

_Required_: No

_Type_: List of <a href="databasefiltercfgdefinition.md">DatabaseFilterCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageDigestCfg

_Required_: No

_Type_: List of <a href="messagedigestcfgdefinition.md">MessageDigestCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

