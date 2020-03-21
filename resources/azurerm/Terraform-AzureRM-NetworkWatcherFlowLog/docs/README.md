# Terraform::AzureRM::NetworkWatcherFlowLog

Manages a Network Watcher Flow Log.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::NetworkWatcherFlowLog",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>" : <i>String</i>,
        "<a href="#networkwatchername" title="NetworkWatcherName">NetworkWatcherName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="retentionpolicy.md">RetentionPolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#trafficanalytics" title="TrafficAnalytics">TrafficAnalytics</a>" : <i>[ <a href="trafficanalytics.md">TrafficAnalytics</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::NetworkWatcherFlowLog
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>: <i>String</i>
    <a href="#networkwatchername" title="NetworkWatcherName">NetworkWatcherName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="retentionpolicy.md">RetentionPolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#trafficanalytics" title="TrafficAnalytics">TrafficAnalytics</a>: <i>
      - <a href="trafficanalytics.md">TrafficAnalytics</a></i>
</pre>

## Properties

#### Enabled

Should Network Flow Logging be Enabled?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupId

The ID of the Network Security Group for which to enable flow logs for. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkWatcherName

The name of the Network Watcher. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which the Network Watcher was deployed. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

The ID of the Storage Account where flow logs are stored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version (revision) of the flow log. Possible values are `1` and `2`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No

_Type_: List of <a href="retentionpolicy.md">RetentionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficAnalytics

_Required_: No

_Type_: List of <a href="trafficanalytics.md">TrafficAnalytics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

