# TF::FortiOS::ExtendercontrollerExtender1 Modem1Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connstatus" title="ConnStatus">ConnStatus</a>" : <i>Double</i>,
    "<a href="#defaultsim" title="DefaultSim">DefaultSim</a>" : <i>String</i>,
    "<a href="#gps" title="Gps">Gps</a>" : <i>String</i>,
    "<a href="#ifname" title="Ifname">Ifname</a>" : <i>String</i>,
    "<a href="#preferredcarrier" title="PreferredCarrier">PreferredCarrier</a>" : <i>String</i>,
    "<a href="#redundantintf" title="RedundantIntf">RedundantIntf</a>" : <i>String</i>,
    "<a href="#redundantmode" title="RedundantMode">RedundantMode</a>" : <i>String</i>,
    "<a href="#sim1pin" title="Sim1Pin">Sim1Pin</a>" : <i>String</i>,
    "<a href="#sim1pincode" title="Sim1PinCode">Sim1PinCode</a>" : <i>String</i>,
    "<a href="#sim2pin" title="Sim2Pin">Sim2Pin</a>" : <i>String</i>,
    "<a href="#sim2pincode" title="Sim2PinCode">Sim2PinCode</a>" : <i>String</i>,
    "<a href="#autoswitch" title="AutoSwitch">AutoSwitch</a>" : <i>[ <a href="autoswitchdefinition.md">AutoSwitchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connstatus" title="ConnStatus">ConnStatus</a>: <i>Double</i>
<a href="#defaultsim" title="DefaultSim">DefaultSim</a>: <i>String</i>
<a href="#gps" title="Gps">Gps</a>: <i>String</i>
<a href="#ifname" title="Ifname">Ifname</a>: <i>String</i>
<a href="#preferredcarrier" title="PreferredCarrier">PreferredCarrier</a>: <i>String</i>
<a href="#redundantintf" title="RedundantIntf">RedundantIntf</a>: <i>String</i>
<a href="#redundantmode" title="RedundantMode">RedundantMode</a>: <i>String</i>
<a href="#sim1pin" title="Sim1Pin">Sim1Pin</a>: <i>String</i>
<a href="#sim1pincode" title="Sim1PinCode">Sim1PinCode</a>: <i>String</i>
<a href="#sim2pin" title="Sim2Pin">Sim2Pin</a>: <i>String</i>
<a href="#sim2pincode" title="Sim2PinCode">Sim2PinCode</a>: <i>String</i>
<a href="#autoswitch" title="AutoSwitch">AutoSwitch</a>: <i>
      - <a href="autoswitchdefinition.md">AutoSwitchDefinition</a></i>
</pre>

## Properties

#### ConnStatus

Connection status.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSim

Default SIM selection. Valid values: `sim1`, `sim2`, `carrier`, `cost`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gps

FortiExtender GPS enable/disable. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ifname

FortiExtender interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredCarrier

Preferred carrier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedundantIntf

Redundant interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedundantMode

FortiExtender mode. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sim1Pin

SIM #1 PIN status. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sim1PinCode

SIM #1 PIN password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sim2Pin

SIM #2 PIN status. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sim2PinCode

SIM #2 PIN password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSwitch

_Required_: No

_Type_: List of <a href="autoswitchdefinition.md">AutoSwitchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

