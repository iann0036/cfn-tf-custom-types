# TF::FortiOS::WirelesscontrollerVap MpskKeyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#concurrentclients" title="ConcurrentClients">ConcurrentClients</a>" : <i>String</i>,
    "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
    "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
    "<a href="#mpskschedules" title="MpskSchedules">MpskSchedules</a>" : <i>[ <a href="mpskschedulesdefinition.md">MpskSchedulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#concurrentclients" title="ConcurrentClients">ConcurrentClients</a>: <i>String</i>
<a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
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

#### ConcurrentClients

Number of clients that can connect using this pre-shared key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

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

