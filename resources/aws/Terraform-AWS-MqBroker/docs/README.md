# Terraform::AWS::MqBroker

Provides an MQ Broker Resource. This resources also manages users for the broker.

For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

Changes to an MQ Broker can occur when you change a
parameter, such as `configuration` or `user`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `apply_immediately` can result in a
brief downtime as the broker reboots.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::MqBroker",
    "Properties" : {
        "<a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>" : <i>Boolean</i>,
        "<a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>" : <i>Boolean</i>,
        "<a href="#brokername" title="BrokerName">BrokerName</a>" : <i>String</i>,
        "<a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>" : <i>String</i>,
        "<a href="#enginetype" title="EngineType">EngineType</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>" : <i>String</i>,
        "<a href="#publiclyaccessible" title="PubliclyAccessible">PubliclyAccessible</a>" : <i>Boolean</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#configuration" title="Configuration">Configuration</a>" : <i>[ <a href="configuration.md">Configuration</a>, ... ]</i>,
        "<a href="#encryptionoptions" title="EncryptionOptions">EncryptionOptions</a>" : <i>[ <a href="encryptionoptions.md">EncryptionOptions</a>, ... ]</i>,
        "<a href="#logs" title="Logs">Logs</a>" : <i>[ <a href="logs.md">Logs</a>, ... ]</i>,
        "<a href="#maintenancewindowstarttime" title="MaintenanceWindowStartTime">MaintenanceWindowStartTime</a>" : <i>[ <a href="maintenancewindowstarttime.md">MaintenanceWindowStartTime</a>, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>[ <a href="user.md">User</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::MqBroker
Properties:
    <a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>: <i>Boolean</i>
    <a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>: <i>Boolean</i>
    <a href="#brokername" title="BrokerName">BrokerName</a>: <i>String</i>
    <a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>: <i>String</i>
    <a href="#enginetype" title="EngineType">EngineType</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>: <i>String</i>
    <a href="#publiclyaccessible" title="PubliclyAccessible">PubliclyAccessible</a>: <i>Boolean</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#configuration" title="Configuration">Configuration</a>: <i>
      - <a href="configuration.md">Configuration</a></i>
    <a href="#encryptionoptions" title="EncryptionOptions">EncryptionOptions</a>: <i>
      - <a href="encryptionoptions.md">EncryptionOptions</a></i>
    <a href="#logs" title="Logs">Logs</a>: <i>
      - <a href="logs.md">Logs</a></i>
    <a href="#maintenancewindowstarttime" title="MaintenanceWindowStartTime">MaintenanceWindowStartTime</a>: <i>
      - <a href="maintenancewindowstarttime.md">MaintenanceWindowStartTime</a></i>
    <a href="#user" title="User">User</a>: <i>
      - <a href="user.md">User</a></i>
</pre>

## Properties

#### ApplyImmediately

Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMinorVersionUpgrade

Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrokerName

The name of the broker.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMode

The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineType

The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostInstanceType

The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PubliclyAccessible

Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

The list of security group IDs assigned to the broker.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

_Required_: No

_Type_: List of <a href="configuration.md">Configuration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionOptions

_Required_: No

_Type_: List of <a href="encryptionoptions.md">EncryptionOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logs

_Required_: No

_Type_: List of <a href="logs.md">Logs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowStartTime

_Required_: No

_Type_: List of <a href="maintenancewindowstarttime.md">MaintenanceWindowStartTime</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: List of <a href="user.md">User</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Instances

Returns the <code>Instances</code> value.

