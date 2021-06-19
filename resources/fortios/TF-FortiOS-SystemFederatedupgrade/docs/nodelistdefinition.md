# TF::FortiOS::SystemFederatedupgrade NodeListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#serial" title="Serial">Serial</a>" : <i>String</i>,
    "<a href="#setuptime" title="SetupTime">SetupTime</a>" : <i>String</i>,
    "<a href="#time" title="Time">Time</a>" : <i>String</i>,
    "<a href="#timing" title="Timing">Timing</a>" : <i>String</i>,
    "<a href="#upgradepath" title="UpgradePath">UpgradePath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#serial" title="Serial">Serial</a>: <i>String</i>
<a href="#setuptime" title="SetupTime">SetupTime</a>: <i>String</i>
<a href="#time" title="Time">Time</a>: <i>String</i>
<a href="#timing" title="Timing">Timing</a>: <i>String</i>
<a href="#upgradepath" title="UpgradePath">UpgradePath</a>: <i>String</i>
</pre>

## Properties

#### Serial

Serial number of the node to include.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetupTime

When the upgrade was configured. Format hh:mm yyyy/mm/dd UTC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

Scheduled time for the upgrade. Format hh:mm yyyy/mm/dd UTC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timing

Whether the upgrade should be run immediately, or at a scheduled time. Valid values: `immediate`, `scheduled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradePath

Image IDs to upgrade through.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

