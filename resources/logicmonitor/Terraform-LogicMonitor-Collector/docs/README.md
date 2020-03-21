# Terraform::LogicMonitor::Collector

CloudFormation equivalent of logicmonitor_collector

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::LogicMonitor::Collector",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#backupcollectorid" title="BackupCollectorId">BackupCollectorId</a>" : <i>Double</i>,
        "<a href="#collectorgroupid" title="CollectorGroupId">CollectorGroupId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablecollectordevicefailover" title="EnableCollectorDeviceFailover">EnableCollectorDeviceFailover</a>" : <i>Boolean</i>,
        "<a href="#enablefailback" title="EnableFailback">EnableFailback</a>" : <i>Boolean</i>,
        "<a href="#escalationchainid" title="EscalationChainId">EscalationChainId</a>" : <i>Double</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ &lt;a href=&#34;properties.md&#34;&gt;Properties&lt;/a&gt;, ... ]</i>,
        "<a href="#resendinterval" title="ResendInterval">ResendInterval</a>" : <i>Double</i>,
        "<a href="#suppressalertclear" title="SuppressAlertClear">SuppressAlertClear</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::LogicMonitor::Collector
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#backupcollectorid" title="BackupCollectorId">BackupCollectorId</a>: <i>Double</i>
    <a href="#collectorgroupid" title="CollectorGroupId">CollectorGroupId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablecollectordevicefailover" title="EnableCollectorDeviceFailover">EnableCollectorDeviceFailover</a>: <i>Boolean</i>
    <a href="#enablefailback" title="EnableFailback">EnableFailback</a>: <i>Boolean</i>
    <a href="#escalationchainid" title="EscalationChainId">EscalationChainId</a>: <i>Double</i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - &lt;a href=&#34;properties.md&#34;&gt;Properties&lt;/a&gt;</i>
    <a href="#resendinterval" title="ResendInterval">ResendInterval</a>: <i>Double</i>
    <a href="#suppressalertclear" title="SuppressAlertClear">SuppressAlertClear</a>: <i>Boolean</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupCollectorId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CollectorGroupId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCollectorDeviceFailover

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFailback

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationChainId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of &lt;a href=&#34;properties.md&#34;&gt;Properties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResendInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressAlertClear

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

