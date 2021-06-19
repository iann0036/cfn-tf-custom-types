# TF::Thunder::InterfaceEthernetLldp

`thunder_interface_ethernet_lldp` Provides details about thunder interface ethernet lldp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::InterfaceEthernetLldp",
    "Properties" : {
        "<a href="#ifnum" title="Ifnum">Ifnum</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#enablecfg" title="EnableCfg">EnableCfg</a>" : <i>[ <a href="enablecfgdefinition.md">EnableCfgDefinition</a>, ... ]</i>,
        "<a href="#notificationcfg" title="NotificationCfg">NotificationCfg</a>" : <i>[ <a href="notificationcfgdefinition.md">NotificationCfgDefinition</a>, ... ]</i>,
        "<a href="#txdot1cfg" title="TxDot1Cfg">TxDot1Cfg</a>" : <i>[ <a href="txdot1cfgdefinition.md">TxDot1CfgDefinition</a>, ... ]</i>,
        "<a href="#txtlvscfg" title="TxTlvsCfg">TxTlvsCfg</a>" : <i>[ <a href="txtlvscfgdefinition.md">TxTlvsCfgDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::InterfaceEthernetLldp
Properties:
    <a href="#ifnum" title="Ifnum">Ifnum</a>: <i>Double</i>
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

#### Ifnum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

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

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

