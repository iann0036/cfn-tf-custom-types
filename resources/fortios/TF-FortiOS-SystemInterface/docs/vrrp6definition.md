# TF::FortiOS::SystemInterface Vrrp6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceptmode" title="AcceptMode">AcceptMode</a>" : <i>String</i>,
    "<a href="#advinterval" title="AdvInterval">AdvInterval</a>" : <i>Double</i>,
    "<a href="#preempt" title="Preempt">Preempt</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#vrdst6" title="Vrdst6">Vrdst6</a>" : <i>String</i>,
    "<a href="#vrgrp" title="Vrgrp">Vrgrp</a>" : <i>Double</i>,
    "<a href="#vrid" title="Vrid">Vrid</a>" : <i>Double</i>,
    "<a href="#vrip6" title="Vrip6">Vrip6</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acceptmode" title="AcceptMode">AcceptMode</a>: <i>String</i>
<a href="#advinterval" title="AdvInterval">AdvInterval</a>: <i>Double</i>
<a href="#preempt" title="Preempt">Preempt</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#vrdst6" title="Vrdst6">Vrdst6</a>: <i>String</i>
<a href="#vrgrp" title="Vrgrp">Vrgrp</a>: <i>Double</i>
<a href="#vrid" title="Vrid">Vrid</a>: <i>Double</i>
<a href="#vrip6" title="Vrip6">Vrip6</a>: <i>String</i>
</pre>

## Properties

#### AcceptMode

Enable/disable accept mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvInterval

Advertisement interval (1 - 255 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preempt

Enable/disable preempt mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority of the virtual router (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Startup time (1 - 255 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable VRRP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrdst6

Monitor the route to this destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrgrp

VRRP group ID (1 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrid

Virtual router identifier (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrip6

IPv6 address of the virtual router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

