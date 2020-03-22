# Terraform::LogicMonitor::Collector

Provides a LogicMonitor collector resource. This can be used to create and manage LogicMonitor collectors.

*Note:* This resource will only create the collector device in your account. See [Downloading a Collector Installer](https://www.logicmonitor.com/support/rest-api-developers-guide/collectors/downloading-a-collector-installer/) for
information on how to download and install an existing collector.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::LogicMonitor::Collector",
    "Properties" : {
        "<a href="#backupcollectorid" title="BackupCollectorId">BackupCollectorId</a>" : <i>Double</i>,
        "<a href="#collectorgroupid" title="CollectorGroupId">CollectorGroupId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablecollectordevicefailover" title="EnableCollectorDeviceFailover">EnableCollectorDeviceFailover</a>" : <i>Boolean</i>,
        "<a href="#enablefailback" title="EnableFailback">EnableFailback</a>" : <i>Boolean</i>,
        "<a href="#escalationchainid" title="EscalationChainId">EscalationChainId</a>" : <i>Double</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="properties.md">Properties</a>, ... ]</i>,
        "<a href="#resendinterval" title="ResendInterval">ResendInterval</a>" : <i>Double</i>,
        "<a href="#suppressalertclear" title="SuppressAlertClear">SuppressAlertClear</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::LogicMonitor::Collector
Properties:
    <a href="#backupcollectorid" title="BackupCollectorId">BackupCollectorId</a>: <i>Double</i>
    <a href="#collectorgroupid" title="CollectorGroupId">CollectorGroupId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablecollectordevicefailover" title="EnableCollectorDeviceFailover">EnableCollectorDeviceFailover</a>: <i>Boolean</i>
    <a href="#enablefailback" title="EnableFailback">EnableFailback</a>: <i>Boolean</i>
    <a href="#escalationchainid" title="EscalationChainId">EscalationChainId</a>: <i>Double</i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="properties.md">Properties</a></i>
    <a href="#resendinterval" title="ResendInterval">ResendInterval</a>: <i>Double</i>
    <a href="#suppressalertclear" title="SuppressAlertClear">SuppressAlertClear</a>: <i>Boolean</i>
</pre>

## Properties

#### BackupCollectorId

The Id of the failover Collector configured for this Collector.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CollectorGroupId

The Id of the group the Collector is in.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The Collector's description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCollectorDeviceFailover

Whether or not the device the Collector is installed on is enabled for fail over.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFailback

Whether or not automatic failback is enabled for the Collector.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationChainId

The Id of the escalation chain associated with this Collector.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="properties.md">Properties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResendInterval

The interval, in minutes, after which alert notifications for the Collector will be resent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressAlertClear

Whether alert clear notifications are suppressed for the Collector.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

