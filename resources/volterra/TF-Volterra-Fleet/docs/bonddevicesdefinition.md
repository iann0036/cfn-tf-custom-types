# TF::Volterra::Fleet BondDevicesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activebackup" title="ActiveBackup">ActiveBackup</a>" : <i>Boolean</i>,
    "<a href="#devices" title="Devices">Devices</a>" : <i>[ String, ... ]</i>,
    "<a href="#linkpollinginterval" title="LinkPollingInterval">LinkPollingInterval</a>" : <i>Double</i>,
    "<a href="#linkupdelay" title="LinkUpDelay">LinkUpDelay</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#lacp" title="Lacp">Lacp</a>" : <i>[ <a href="lacpdefinition.md">LacpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#activebackup" title="ActiveBackup">ActiveBackup</a>: <i>Boolean</i>
<a href="#devices" title="Devices">Devices</a>: <i>
      - String</i>
<a href="#linkpollinginterval" title="LinkPollingInterval">LinkPollingInterval</a>: <i>Double</i>
<a href="#linkupdelay" title="LinkUpDelay">LinkUpDelay</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#lacp" title="Lacp">Lacp</a>: <i>
      - <a href="lacpdefinition.md">LacpDefinition</a></i>
</pre>

## Properties

#### ActiveBackup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkPollingInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkUpDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lacp

_Required_: No

_Type_: List of <a href="lacpdefinition.md">LacpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

