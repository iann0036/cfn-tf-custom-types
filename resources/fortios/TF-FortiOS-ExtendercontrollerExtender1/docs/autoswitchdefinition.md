# TF::FortiOS::ExtendercontrollerExtender1 AutoSwitchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dataplan" title="Dataplan">Dataplan</a>" : <i>String</i>,
    "<a href="#disconnect" title="Disconnect">Disconnect</a>" : <i>String</i>,
    "<a href="#disconnectperiod" title="DisconnectPeriod">DisconnectPeriod</a>" : <i>Double</i>,
    "<a href="#disconnectthreshold" title="DisconnectThreshold">DisconnectThreshold</a>" : <i>Double</i>,
    "<a href="#signal" title="Signal">Signal</a>" : <i>String</i>,
    "<a href="#switchback" title="SwitchBack">SwitchBack</a>" : <i>String</i>,
    "<a href="#switchbacktime" title="SwitchBackTime">SwitchBackTime</a>" : <i>String</i>,
    "<a href="#switchbacktimer" title="SwitchBackTimer">SwitchBackTimer</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dataplan" title="Dataplan">Dataplan</a>: <i>String</i>
<a href="#disconnect" title="Disconnect">Disconnect</a>: <i>String</i>
<a href="#disconnectperiod" title="DisconnectPeriod">DisconnectPeriod</a>: <i>Double</i>
<a href="#disconnectthreshold" title="DisconnectThreshold">DisconnectThreshold</a>: <i>Double</i>
<a href="#signal" title="Signal">Signal</a>: <i>String</i>
<a href="#switchback" title="SwitchBack">SwitchBack</a>: <i>String</i>
<a href="#switchbacktime" title="SwitchBackTime">SwitchBackTime</a>: <i>String</i>
<a href="#switchbacktimer" title="SwitchBackTimer">SwitchBackTimer</a>: <i>Double</i>
</pre>

## Properties

#### Dataplan

Automatically switch based on data usage. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disconnect

Auto switch by disconnect. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisconnectPeriod

Automatically switch based on disconnect period.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisconnectThreshold

Automatically switch based on disconnect threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signal

Automatically switch based on signal strength. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchBack

Auto switch with switch back multi-options. Valid values: `time`, `timer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchBackTime

Automatically switch over to preferred SIM/carrier at a specified time in UTC (HH:MM).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchBackTimer

Automatically switch over to preferred SIM/carrier after the given time (3600 - 2147483647 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

