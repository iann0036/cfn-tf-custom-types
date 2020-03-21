# Terraform::Consul::AutopilotConfig

CloudFormation equivalent of consul_autopilot_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Consul::AutopilotConfig",
    "Properties" : {
        "<a href="#cleanupdeadservers" title="CleanupDeadServers">CleanupDeadServers</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#disableupgrademigration" title="DisableUpgradeMigration">DisableUpgradeMigration</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
Type: Terraform::Consul::AutopilotConfig
Properties:
    <a href="#cleanupdeadservers" title="CleanupDeadServers">CleanupDeadServers</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#disableupgrademigration" title="DisableUpgradeMigration">DisableUpgradeMigration</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#lastcontactthreshold" title="LastContactThreshold">LastContactThreshold</a>: <i>String</i>
    <a href="#maxtrailinglogs" title="MaxTrailingLogs">MaxTrailingLogs</a>: <i>Double</i>
    <a href="#redundancyzonetag" title="RedundancyZoneTag">RedundancyZoneTag</a>: <i>String</i>
    <a href="#serverstabilizationtime" title="ServerStabilizationTime">ServerStabilizationTime</a>: <i>String</i>
    <a href="#upgradeversiontag" title="UpgradeVersionTag">UpgradeVersionTag</a>: <i>String</i>
</pre>

## Properties

#### CleanupDeadServers

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableUpgradeMigration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastContactThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTrailingLogs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedundancyZoneTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerStabilizationTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeVersionTag

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

