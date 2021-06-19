# TF::Vultr::Instance

Provides a Vultr instance resource. This can be used to create, read, modify, and delete instances on your Vultr account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::Instance",
    "Properties" : {
        "<a href="#activationemail" title="ActivationEmail">ActivationEmail</a>" : <i>Boolean</i>,
        "<a href="#appid" title="AppId">AppId</a>" : <i>Double</i>,
        "<a href="#backups" title="Backups">Backups</a>" : <i>String</i>,
        "<a href="#ddosprotection" title="DdosProtection">DdosProtection</a>" : <i>Boolean</i>,
        "<a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>" : <i>Boolean</i>,
        "<a href="#enableprivatenetwork" title="EnablePrivateNetwork">EnablePrivateNetwork</a>" : <i>Boolean</i>,
        "<a href="#firewallgroupid" title="FirewallGroupId">FirewallGroupId</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#isoid" title="IsoId">IsoId</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#osid" title="OsId">OsId</a>" : <i>Double</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
        "<a href="#privatenetworkids" title="PrivateNetworkIds">PrivateNetworkIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#reservedipid" title="ReservedIpId">ReservedIpId</a>" : <i>String</i>,
        "<a href="#scriptid" title="ScriptId">ScriptId</a>" : <i>String</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#sshkeyids" title="SshKeyIds">SshKeyIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#backupsschedule" title="BackupsSchedule">BackupsSchedule</a>" : <i>[ <a href="backupsscheduledefinition.md">BackupsScheduleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::Instance
Properties:
    <a href="#activationemail" title="ActivationEmail">ActivationEmail</a>: <i>Boolean</i>
    <a href="#appid" title="AppId">AppId</a>: <i>Double</i>
    <a href="#backups" title="Backups">Backups</a>: <i>String</i>
    <a href="#ddosprotection" title="DdosProtection">DdosProtection</a>: <i>Boolean</i>
    <a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>: <i>Boolean</i>
    <a href="#enableprivatenetwork" title="EnablePrivateNetwork">EnablePrivateNetwork</a>: <i>Boolean</i>
    <a href="#firewallgroupid" title="FirewallGroupId">FirewallGroupId</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#isoid" title="IsoId">IsoId</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#osid" title="OsId">OsId</a>: <i>Double</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
    <a href="#privatenetworkids" title="PrivateNetworkIds">PrivateNetworkIds</a>: <i>
      - String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#reservedipid" title="ReservedIpId">ReservedIpId</a>: <i>String</i>
    <a href="#scriptid" title="ScriptId">ScriptId</a>: <i>String</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#sshkeyids" title="SshKeyIds">SshKeyIds</a>: <i>
      - String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#backupsschedule" title="BackupsSchedule">BackupsSchedule</a>: <i>
      - <a href="backupsscheduledefinition.md">BackupsScheduleDefinition</a></i>
</pre>

## Properties

#### ActivationEmail

Whether an activation email will be sent when the server is ready.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppId

The ID of the Vultr application to be installed on the server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

Whether automatic backups will be enabled for this server (these have an extra charge associated with them). Values can be enabled or disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdosProtection

Whether DDOS protection will be enabled on the server (there is an additional charge for this).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpv6

Whether the server has IPv6 networking activated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateNetwork

Whether the server has private networking support enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallGroupId

The ID of the firewall group to assign to the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The hostname to assign to the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsoId

The ID of the ISO file to be installed on the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

A label for the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsId

The ID of the operating system to be installed on the server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

The ID of the plan that you want the instance to subscribe to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetworkIds

A list of private network IDs to be attached to the server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The ID of the region that the instance is to be created in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedIpId

ID of the floating IP to use as the main IP of this server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptId

The ID of the startup script you want added to the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

The ID of the Vultr snapshot that the server will restore for the initial installation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyIds

A list of SSH key IDs to apply to the server on install (only valid for Linux/FreeBSD).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

The tag to assign to the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Generic data store, which some provisioning tools and cloud operating systems use as a configuration file. It is generally consumed only once after an instance has been launched, but individual needs may vary.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupsSchedule

_Required_: No

_Type_: List of <a href="backupsscheduledefinition.md">BackupsScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllowedBandwidth

Returns the <code>AllowedBandwidth</code> value.

#### DateCreated

Returns the <code>DateCreated</code> value.

#### DefaultPassword

Returns the <code>DefaultPassword</code> value.

#### Disk

Returns the <code>Disk</code> value.

#### Features

Returns the <code>Features</code> value.

#### GatewayV4

Returns the <code>GatewayV4</code> value.

#### Id

Returns the <code>Id</code> value.

#### InternalIp

Returns the <code>InternalIp</code> value.

#### Kvm

Returns the <code>Kvm</code> value.

#### MainIp

Returns the <code>MainIp</code> value.

#### NetmaskV4

Returns the <code>NetmaskV4</code> value.

#### Os

Returns the <code>Os</code> value.

#### PowerStatus

Returns the <code>PowerStatus</code> value.

#### Ram

Returns the <code>Ram</code> value.

#### ServerStatus

Returns the <code>ServerStatus</code> value.

#### Status

Returns the <code>Status</code> value.

#### V6MainIp

Returns the <code>V6MainIp</code> value.

#### V6Network

Returns the <code>V6Network</code> value.

#### V6NetworkSize

Returns the <code>V6NetworkSize</code> value.

#### VcpuCount

Returns the <code>VcpuCount</code> value.

