# Terraform::Linode::Instance

CloudFormation equivalent of linode_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Linode::Instance",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#authorizedkeys" title="AuthorizedKeys">AuthorizedKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizedusers" title="AuthorizedUsers">AuthorizedUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupid" title="BackupId">BackupId</a>" : <i>Double</i>,
        "<a href="#backups" title="Backups">Backups</a>" : <i>[ &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;, ... ]</i>,
        "<a href="#backupsenabled" title="BackupsEnabled">BackupsEnabled</a>" : <i>Boolean</i>,
        "<a href="#bootconfiglabel" title="BootConfigLabel">BootConfigLabel</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#ipv4" title="Ipv4">Ipv4</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>Boolean</i>,
        "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rootpass" title="RootPass">RootPass</a>" : <i>String</i>,
        "<a href="#specs" title="Specs">Specs</a>" : <i>[ &lt;a href=&#34;specs.md&#34;&gt;Specs&lt;/a&gt;, ... ]</i>,
        "<a href="#stackscriptdata" title="StackscriptData">StackscriptData</a>" : <i>[ &lt;a href=&#34;stackscriptdata.md&#34;&gt;StackscriptData&lt;/a&gt;, ... ]</i>,
        "<a href="#stackscriptid" title="StackscriptId">StackscriptId</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#swapsize" title="SwapSize">SwapSize</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#watchdogenabled" title="WatchdogEnabled">WatchdogEnabled</a>" : <i>Boolean</i>,
        "<a href="#alerts" title="Alerts">Alerts</a>" : <i>[ &lt;a href=&#34;alerts.md&#34;&gt;Alerts&lt;/a&gt;, ... ]</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ &lt;a href=&#34;config.md&#34;&gt;Config&lt;/a&gt;, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#devices" title="Devices">Devices</a>" : <i>[ &lt;a href=&#34;devices.md&#34;&gt;Devices&lt;/a&gt;, ... ]</i>,
        "<a href="#helpers" title="Helpers">Helpers</a>" : <i>[ &lt;a href=&#34;helpers.md&#34;&gt;Helpers&lt;/a&gt;, ... ]</i>,
        "<a href="#sda" title="Sda">Sda</a>" : <i>[ &lt;a href=&#34;sda.md&#34;&gt;Sda&lt;/a&gt;, ... ]</i>,
        "<a href="#sdb" title="Sdb">Sdb</a>" : <i>[ &lt;a href=&#34;sdb.md&#34;&gt;Sdb&lt;/a&gt;, ... ]</i>,
        "<a href="#sdc" title="Sdc">Sdc</a>" : <i>[ &lt;a href=&#34;sdc.md&#34;&gt;Sdc&lt;/a&gt;, ... ]</i>,
        "<a href="#sdd" title="Sdd">Sdd</a>" : <i>[ &lt;a href=&#34;sdd.md&#34;&gt;Sdd&lt;/a&gt;, ... ]</i>,
        "<a href="#sde" title="Sde">Sde</a>" : <i>[ &lt;a href=&#34;sde.md&#34;&gt;Sde&lt;/a&gt;, ... ]</i>,
        "<a href="#sdf" title="Sdf">Sdf</a>" : <i>[ &lt;a href=&#34;sdf.md&#34;&gt;Sdf&lt;/a&gt;, ... ]</i>,
        "<a href="#sdg" title="Sdg">Sdg</a>" : <i>[ &lt;a href=&#34;sdg.md&#34;&gt;Sdg&lt;/a&gt;, ... ]</i>,
        "<a href="#sdh" title="Sdh">Sdh</a>" : <i>[ &lt;a href=&#34;sdh.md&#34;&gt;Sdh&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Linode::Instance
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#authorizedkeys" title="AuthorizedKeys">AuthorizedKeys</a>: <i>
      - String</i>
    <a href="#authorizedusers" title="AuthorizedUsers">AuthorizedUsers</a>: <i>
      - String</i>
    <a href="#backupid" title="BackupId">BackupId</a>: <i>Double</i>
    <a href="#backups" title="Backups">Backups</a>: <i>
      - &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;</i>
    <a href="#backupsenabled" title="BackupsEnabled">BackupsEnabled</a>: <i>Boolean</i>
    <a href="#bootconfiglabel" title="BootConfigLabel">BootConfigLabel</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#ipv4" title="Ipv4">Ipv4</a>: <i>
      - String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>Boolean</i>
    <a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rootpass" title="RootPass">RootPass</a>: <i>String</i>
    <a href="#specs" title="Specs">Specs</a>: <i>
      - &lt;a href=&#34;specs.md&#34;&gt;Specs&lt;/a&gt;</i>
    <a href="#stackscriptdata" title="StackscriptData">StackscriptData</a>: <i>
      - &lt;a href=&#34;stackscriptdata.md&#34;&gt;StackscriptData&lt;/a&gt;</i>
    <a href="#stackscriptid" title="StackscriptId">StackscriptId</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#swapsize" title="SwapSize">SwapSize</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#watchdogenabled" title="WatchdogEnabled">WatchdogEnabled</a>: <i>Boolean</i>
    <a href="#alerts" title="Alerts">Alerts</a>: <i>
      - &lt;a href=&#34;alerts.md&#34;&gt;Alerts&lt;/a&gt;</i>
    <a href="#config" title="Config">Config</a>: <i>
      - &lt;a href=&#34;config.md&#34;&gt;Config&lt;/a&gt;</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#devices" title="Devices">Devices</a>: <i>
      - &lt;a href=&#34;devices.md&#34;&gt;Devices&lt;/a&gt;</i>
    <a href="#helpers" title="Helpers">Helpers</a>: <i>
      - &lt;a href=&#34;helpers.md&#34;&gt;Helpers&lt;/a&gt;</i>
    <a href="#sda" title="Sda">Sda</a>: <i>
      - &lt;a href=&#34;sda.md&#34;&gt;Sda&lt;/a&gt;</i>
    <a href="#sdb" title="Sdb">Sdb</a>: <i>
      - &lt;a href=&#34;sdb.md&#34;&gt;Sdb&lt;/a&gt;</i>
    <a href="#sdc" title="Sdc">Sdc</a>: <i>
      - &lt;a href=&#34;sdc.md&#34;&gt;Sdc&lt;/a&gt;</i>
    <a href="#sdd" title="Sdd">Sdd</a>: <i>
      - &lt;a href=&#34;sdd.md&#34;&gt;Sdd&lt;/a&gt;</i>
    <a href="#sde" title="Sde">Sde</a>: <i>
      - &lt;a href=&#34;sde.md&#34;&gt;Sde&lt;/a&gt;</i>
    <a href="#sdf" title="Sdf">Sdf</a>: <i>
      - &lt;a href=&#34;sdf.md&#34;&gt;Sdf&lt;/a&gt;</i>
    <a href="#sdg" title="Sdg">Sdg</a>: <i>
      - &lt;a href=&#34;sdg.md&#34;&gt;Sdg&lt;/a&gt;</i>
    <a href="#sdh" title="Sdh">Sdh</a>: <i>
      - &lt;a href=&#34;sdh.md&#34;&gt;Sdh&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Backups

_Required_: No

_Type_: List of &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;

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

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

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

#### PrivateIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootPass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Specs

_Required_: No

_Type_: List of &lt;a href=&#34;specs.md&#34;&gt;Specs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackscriptData

_Required_: No

_Type_: List of &lt;a href=&#34;stackscriptdata.md&#34;&gt;StackscriptData&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackscriptId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

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

_Type_: List of &lt;a href=&#34;alerts.md&#34;&gt;Alerts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of &lt;a href=&#34;config.md&#34;&gt;Config&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of &lt;a href=&#34;devices.md&#34;&gt;Devices&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Helpers

_Required_: No

_Type_: List of &lt;a href=&#34;helpers.md&#34;&gt;Helpers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sda

_Required_: No

_Type_: List of &lt;a href=&#34;sda.md&#34;&gt;Sda&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdb

_Required_: No

_Type_: List of &lt;a href=&#34;sdb.md&#34;&gt;Sdb&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdc

_Required_: No

_Type_: List of &lt;a href=&#34;sdc.md&#34;&gt;Sdc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdd

_Required_: No

_Type_: List of &lt;a href=&#34;sdd.md&#34;&gt;Sdd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sde

_Required_: No

_Type_: List of &lt;a href=&#34;sde.md&#34;&gt;Sde&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdf

_Required_: No

_Type_: List of &lt;a href=&#34;sdf.md&#34;&gt;Sdf&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdg

_Required_: No

_Type_: List of &lt;a href=&#34;sdg.md&#34;&gt;Sdg&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdh

_Required_: No

_Type_: List of &lt;a href=&#34;sdh.md&#34;&gt;Sdh&lt;/a&gt;

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

Returns the &lt;code&gt;Backups&lt;/code&gt; value.

#### IpAddress

Returns the &lt;code&gt;IpAddress&lt;/code&gt; value.

#### Ipv4

Returns the &lt;code&gt;Ipv4&lt;/code&gt; value.

#### Ipv6

Returns the &lt;code&gt;Ipv6&lt;/code&gt; value.

#### PrivateIpAddress

Returns the &lt;code&gt;PrivateIpAddress&lt;/code&gt; value.

#### Specs

Returns the &lt;code&gt;Specs&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

