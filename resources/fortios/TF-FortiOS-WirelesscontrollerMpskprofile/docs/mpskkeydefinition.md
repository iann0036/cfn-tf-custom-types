# TF::FortiOS::WirelesscontrollerMpskprofile MpskKeyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#concurrentclientlimittype" title="ConcurrentClientLimitType">ConcurrentClientLimitType</a>" : <i>String</i>,
    "<a href="#concurrentclients" title="ConcurrentClients">ConcurrentClients</a>" : <i>Double</i>,
    "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
    "<a href="#mpskschedules" title="MpskSchedules">MpskSchedules</a>" : <i>[ <a href="mpskschedulesdefinition.md">MpskSchedulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#concurrentclientlimittype" title="ConcurrentClientLimitType">ConcurrentClientLimitType</a>: <i>String</i>
<a href="#concurrentclients" title="ConcurrentClients">ConcurrentClients</a>: <i>Double</i>
<a href="#mac" title="Mac">Mac</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#passphrase" title="Passphrase">Passphrase</a>: <i>String</i>
<a href="#mpskschedules" title="MpskSchedules">MpskSchedules</a>: <i>
      - <a href="mpskschedulesdefinition.md">MpskSchedulesDefinition</a></i>
</pre>

## Properties

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConcurrentClientLimitType

MPSK client limit type options. Valid values: `default`, `unlimited`, `specified`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConcurrentClients

Number of clients that can connect using this pre-shared key (1 - 65535, default is 256).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

MAC address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Pre-shared key name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passphrase

WPA Pre-shared key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MpskSchedules

_Required_: No

_Type_: List of <a href="mpskschedulesdefinition.md">MpskSchedulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

