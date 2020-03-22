# Terraform::Linode::Instance

Provides a Linode Instance resource.  This can be used to create, modify, and delete Linodes.
For more information, see [Getting Started with Linode](https://linode.com/docs/getting-started/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createLinodeInstance).

The Linode Guide, [Use Terraform to Provision Linode Environments](https://www.linode.com/docs/applications/configuration-management/how-to-build-your-infrastructure-using-terraform-and-linode/), provides step-by-step guidance and additional examples.

Linode Instances can also use [provisioners](/docs/provisioners/index.html).

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

If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootConfigLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

The display group of the Linode instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The Linode's label is for display purposes only. If no label is provided for a Linode, a default will be assigned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode's region. It can be enabled on an existing Linode but it can't be disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

This is the location where the Linode is deployed. Examples are `"us-east"`, `"us-west"`, `"ap-south"`, etc. See all regions [here](https://api.linode.com/v4/regions). *Changing `region` forces the creation of a new Linode Instance.*.

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

A list of tags applied to this object. Tags are for organizational purposes only.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The Linode type defines the pricing, CPU, disk, and RAM specs of the instance. Examples are `"g6-nanode-1"`, `"g6-standard-2"`, `"g6-highmem-16"`, `"g6-dedicated-16"`, etc. See all types [here](https://api.linode.com/v4/linode/types).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatchdogEnabled

The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Backups

Returns the <code>Backups</code> value.

#### Id

Returns the <code>Id</code> value.

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

