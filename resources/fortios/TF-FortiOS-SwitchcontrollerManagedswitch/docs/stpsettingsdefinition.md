# TF::FortiOS::SwitchcontrollerManagedswitch StpSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#forwardtime" title="ForwardTime">ForwardTime</a>" : <i>Double</i>,
    "<a href="#hellotime" title="HelloTime">HelloTime</a>" : <i>Double</i>,
    "<a href="#localoverride" title="LocalOverride">LocalOverride</a>" : <i>String</i>,
    "<a href="#maxage" title="MaxAge">MaxAge</a>" : <i>Double</i>,
    "<a href="#maxhops" title="MaxHops">MaxHops</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#pendingtimer" title="PendingTimer">PendingTimer</a>" : <i>Double</i>,
    "<a href="#revision" title="Revision">Revision</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#forwardtime" title="ForwardTime">ForwardTime</a>: <i>Double</i>
<a href="#hellotime" title="HelloTime">HelloTime</a>: <i>Double</i>
<a href="#localoverride" title="LocalOverride">LocalOverride</a>: <i>String</i>
<a href="#maxage" title="MaxAge">MaxAge</a>: <i>Double</i>
<a href="#maxhops" title="MaxHops">MaxHops</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#pendingtimer" title="PendingTimer">PendingTimer</a>: <i>Double</i>
<a href="#revision" title="Revision">Revision</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### ForwardTime

Period of time a port is in listening and learning state (4 - 30 sec, default = 15).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloTime

Period of time between successive STP frame Bridge Protocol Data Units (BPDUs) sent on a port (1 - 10 sec, default = 2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalOverride

Enable to configure local STP settings that override global STP settings. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAge

Maximum time before a bridge port saves its configuration BPDU information (6 - 40 sec, default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHops

Maximum number of hops between the root bridge and the furthest bridge (1- 40, default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of local STP settings configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingTimer

Pending time (1 - 15 sec, default = 4).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

STP revision number (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable STP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

