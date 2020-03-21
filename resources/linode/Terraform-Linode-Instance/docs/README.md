# Terraform::Linode::Instance

CloudFormation equivalent of linode_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Linode::Instance",
    "Properties" : {
        "<a href="#authorizedkeys" title="AuthorizedKeys">AuthorizedKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizedusers" title="AuthorizedUsers">AuthorizedUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupid" title="BackupId">BackupId</a>" : <i>Double</i>,
        "<a href="#backupsenabled" title="BackupsEnabled">BackupsEnabled</a>" : <i>Boolean</i>,
        "<a href="#bootconfiglabel" title="BootConfigLabel">BootConfigLabel</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rootpass" title="RootPass">RootPass</a>" : <i>String</i>,
        "<a href="#stackscriptdata" title="StackscriptData">StackscriptData</a>" : <i>[ <a href="stackscriptdata.md">StackscriptData</a>, ... ]</i>,
        "<a href="#stackscriptid" title="StackscriptId">StackscriptId</a>" : <i>Double</i>,
        "<a href="#swapsize" title="SwapSize">SwapSize</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#watchdogenabled" title="WatchdogEnabled">WatchdogEnabled</a>" : <i>Boolean</i>,
        "<a href="#alerts" title="Alerts">Alerts</a>" : <i>[ <a href="alerts.md">Alerts</a>, ... ]</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="disk.md">Disk</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#devices" title="Devices">Devices</a>" : <i>[ <a href="devices.md">Devices</a>, ... ]</i>,
        "<a href="#helpers" title="Helpers">Helpers</a>" : <i>[ <a href="helpers.md">Helpers</a>, ... ]</i>,
        "<a href="#sda" title="Sda">Sda</a>" : <i>[ <a href="sda.md">Sda</a>, ... ]</i>,
        "<a href="#sdb" title="Sdb">Sdb</a>" : <i>[ <a href="sdb.md">Sdb</a>, ... ]</i>,
        "<a href="#sdc" title="Sdc">Sdc</a>" : <i>[ <a href="sdc.md">Sdc</a>, ... ]</i>,
        "<a href="#sdd" title="Sdd">Sdd</a>" : <i>[ <a href="sdd.md">Sdd</a>, ... ]</i>,
        "<a href="#sde" title="Sde">Sde</a>" : <i>[ <a href="sde.md">Sde</a>, ... ]</i>,
        "<a href="#sdf" title="Sdf">Sdf</a>" : <i>[ <a href="sdf.md">Sdf</a>, ... ]</i>,
        "<a href="#sdg" title="Sdg">Sdg</a>" : <i>[ <a href="sdg.md">Sdg</a>, ... ]</i>,
        "<a href="#sdh" title="Sdh">Sdh</a>" : <i>[ <a href="sdh.md">Sdh</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Linode::Instance
Properties:
    <a href="#authorizedkeys" title="AuthorizedKeys">AuthorizedKeys</a>: <i>
      - String</i>
    <a href="#authorizedusers" title="AuthorizedUsers">AuthorizedUsers</a>: <i>
      - String</i>
    <a href="#backupid" title="BackupId">BackupId</a>: <i>Double</i>
    <a href="#backupsenabled" title="BackupsEnabled">BackupsEnabled</a>: <i>Boolean</i>
    <a href="#bootconfiglabel" title="BootConfigLabel">BootConfigLabel</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rootpass" title="RootPass">RootPass</a>: <i>String</i>
    <a href="#stackscriptdata" title="StackscriptData">StackscriptData</a>: <i>
      - <a href="stackscriptdata.md">StackscriptData</a></i>
    <a href="#stackscriptid" title="StackscriptId">StackscriptId</a>: <i>Double</i>
    <a href="#swapsize" title="SwapSize">SwapSize</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#watchdogenabled" title="WatchdogEnabled">WatchdogEnabled</a>: <i>Boolean</i>
    <a href="#alerts" title="Alerts">Alerts</a>: <i>
      - <a href="alerts.md">Alerts</a></i>
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="config.md">Config</a></i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="disk.md">Disk</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#devices" title="Devices">Devices</a>: <i>
      - <a href="devices.md">Devices</a></i>
    <a href="#helpers" title="Helpers">Helpers</a>: <i>
      - <a href="helpers.md">Helpers</a></i>
    <a href="#sda" title="Sda">Sda</a>: <i>
      - <a href="sda.md">Sda</a></i>
    <a href="#sdb" title="Sdb">Sdb</a>: <i>
      - <a href="sdb.md">Sdb</a></i>
    <a href="#sdc" title="Sdc">Sdc</a>: <i>
      - <a href="sdc.md">Sdc</a></i>
    <a href="#sdd" title="Sdd">Sdd</a>: <i>
      - <a href="sdd.md">Sdd</a></i>
    <a href="#sde" title="Sde">Sde</a>: <i>
      - <a href="sde.md">Sde</a></i>
    <a href="#sdf" title="Sdf">Sdf</a>: <i>
      - <a href="sdf.md">Sdf</a></i>
    <a href="#sdg" title="Sdg">Sdg</a>: <i>
      - <a href="sdg.md">Sdg</a></i>
    <a href="#sdh" title="Sdh">Sdh</a>: <i>
      - <a href="sdh.md">Sdh</a></i>
</pre>

## Properties

#### AuthorizedKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedUsers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootConfigLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootPass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackscriptData

_Required_: No

_Type_: List of <a href="stackscriptdata.md">StackscriptData</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackscriptId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwapSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatchdogEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alerts

_Required_: No

_Type_: List of <a href="alerts.md">Alerts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="disk.md">Disk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of <a href="devices.md">Devices</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Helpers

_Required_: No

_Type_: List of <a href="helpers.md">Helpers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sda

_Required_: No

_Type_: List of <a href="sda.md">Sda</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdb

_Required_: No

_Type_: List of <a href="sdb.md">Sdb</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdc

_Required_: No

_Type_: List of <a href="sdc.md">Sdc</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdd

_Required_: No

_Type_: List of <a href="sdd.md">Sdd</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sde

_Required_: No

_Type_: List of <a href="sde.md">Sde</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdf

_Required_: No

_Type_: List of <a href="sdf.md">Sdf</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdg

_Required_: No

_Type_: List of <a href="sdg.md">Sdg</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdh

_Required_: No

_Type_: List of <a href="sdh.md">Sdh</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Backups

Returns the <code>Backups</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### Ipv4

Returns the <code>Ipv4</code> value.

#### Ipv6

Returns the <code>Ipv6</code> value.

#### PrivateIpAddress

Returns the <code>PrivateIpAddress</code> value.

#### Specs

Returns the <code>Specs</code> value.

#### Status

Returns the <code>Status</code> value.

