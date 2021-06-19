# TF::Consul::AutopilotConfig

Provides access to the [Autopilot Configuration](https://www.consul.io/docs/guides/autopilot.html)
of Consul to automatically manage Consul servers.

It includes to automatically cleanup dead servers, monitor the status of the Raft
cluster and stable server introduction.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Consul::AutopilotConfig",
    "Properties" : {
        "<a href="#cleanupdeadservers" title="CleanupDeadServers">CleanupDeadServers</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#disableupgrademigration" title="DisableUpgradeMigration">DisableUpgradeMigration</a>" : <i>Boolean</i>,
        "<a href="#lastcontactthreshold" title="LastContactThreshold">LastContactThreshold</a>" : <i>String</i>,
        "<a href="#maxtrailinglogs" title="MaxTrailingLogs">MaxTrailingLogs</a>" : <i>Double</i>,
        "<a href="#redundancyzonetag" title="RedundancyZoneTag">RedundancyZoneTag</a>" : <i>String</i>,
        "<a href="#serverstabilizationtime" title="ServerStabilizationTime">ServerStabilizationTime</a>" : <i>String</i>,
        "<a href="#upgradeversiontag" title="UpgradeVersionTag">UpgradeVersionTag</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Consul::AutopilotConfig
Properties:
    <a href="#cleanupdeadservers" title="CleanupDeadServers">CleanupDeadServers</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#disableupgrademigration" title="DisableUpgradeMigration">DisableUpgradeMigration</a>: <i>Boolean</i>
    <a href="#lastcontactthreshold" title="LastContactThreshold">LastContactThreshold</a>: <i>String</i>
    <a href="#maxtrailinglogs" title="MaxTrailingLogs">MaxTrailingLogs</a>: <i>Double</i>
    <a href="#redundancyzonetag" title="RedundancyZoneTag">RedundancyZoneTag</a>: <i>String</i>
    <a href="#serverstabilizationtime" title="ServerStabilizationTime">ServerStabilizationTime</a>: <i>String</i>
    <a href="#upgradeversiontag" title="UpgradeVersionTag">UpgradeVersionTag</a>: <i>String</i>
</pre>

## Properties

#### CleanupDeadServers

Whether to remove failing servers when a
replacement comes online. Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

The datacenter to use. This overrides the agent's
default datacenter and the datacenter in the provider setup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableUpgradeMigration

Whether to disable [upgrade migrations](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones).
Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastContactThreshold

The time after which a server is
considered as unhealthy and will be removed. Defaults to `"200ms"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTrailingLogs

The maximum number of Raft log entries a
server can trail the leader. Defaults to 250.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedundancyZoneTag

The [redundancy zone](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones)
tag to use. Consul will try to keep one voting server by zone to take advantage
of isolated failure domains. Defaults to an empty string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerStabilizationTime

The period to wait for a server to be
healthy and stable before being promoted to a full, voting member. Defaults to
`"10s"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeVersionTag

The tag to override the version information
used during a migration. Defaults to an empty string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

