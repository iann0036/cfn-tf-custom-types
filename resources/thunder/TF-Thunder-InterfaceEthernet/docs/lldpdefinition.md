# TF::Thunder::InterfaceEthernet LldpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#enablecfg" title="EnableCfg">EnableCfg</a>" : <i>[ <a href="enablecfgdefinition.md">EnableCfgDefinition</a>, ... ]</i>,
    "<a href="#notificationcfg" title="NotificationCfg">NotificationCfg</a>" : <i>[ <a href="notificationcfgdefinition.md">NotificationCfgDefinition</a>, ... ]</i>,
    "<a href="#txdot1cfg" title="TxDot1Cfg">TxDot1Cfg</a>" : <i>[ <a href="txdot1cfgdefinition.md">TxDot1CfgDefinition</a>, ... ]</i>,
    "<a href="#txtlvscfg" title="TxTlvsCfg">TxTlvsCfg</a>" : <i>[ <a href="txtlvscfgdefinition.md">TxTlvsCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#enablecfg" title="EnableCfg">EnableCfg</a>: <i>
      - <a href="enablecfgdefinition.md">EnableCfgDefinition</a></i>
<a href="#notificationcfg" title="NotificationCfg">NotificationCfg</a>: <i>
      - <a href="notificationcfgdefinition.md">NotificationCfgDefinition</a></i>
<a href="#txdot1cfg" title="TxDot1Cfg">TxDot1Cfg</a>: <i>
      - <a href="txdot1cfgdefinition.md">TxDot1CfgDefinition</a></i>
<a href="#txtlvscfg" title="TxTlvsCfg">TxTlvsCfg</a>: <i>
      - <a href="txtlvscfgdefinition.md">TxTlvsCfgDefinition</a></i>
</pre>

## Properties

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCfg

_Required_: No

_Type_: List of <a href="enablecfgdefinition.md">EnableCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationCfg

_Required_: No

_Type_: List of <a href="notificationcfgdefinition.md">NotificationCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxDot1Cfg

_Required_: No

_Type_: List of <a href="txdot1cfgdefinition.md">TxDot1CfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxTlvsCfg

_Required_: No

_Type_: List of <a href="txtlvscfgdefinition.md">TxTlvsCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

