# TF::AWS::MqBroker

Provides an Amazon MQ broker resource. This resources also manages users for the broker.

-> For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

~> **NOTE:** Amazon MQ currently places limits on **RabbitMQ** brokers. For example, a RabbitMQ broker cannot have: instances with an associated IP address of an ENI attached to the broker, an associated LDAP server to authenticate and authorize broker connections, storage type `EFS`, audit logging, or `configuration` blocks. Although this resource allows you to create RabbitMQ users, RabbitMQ users cannot have console access or groups. Also, Amazon MQ does not return information about RabbitMQ users so drift detection is not possible.

~> **NOTE:** Changes to an MQ Broker can occur when you change a parameter, such as `configuration` or `user`, and are reflected in the next maintenance window. Because of this, Terraform may report a difference in its planning phase because ...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::MqBroker",
    "Properties" : {
        "<a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>" : <i>Boolean</i>,
        "<a href="#authenticationstrategy" title="AuthenticationStrategy">AuthenticationStrategy</a>" : <i>String</i>,
        "<a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>" : <i>Boolean</i>,
        "<a href="#brokername" title="BrokerName">BrokerName</a>" : <i>String</i>,
        "<a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>" : <i>String</i>,
        "<a href="#enginetype" title="EngineType">EngineType</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>" : <i>String</i>,
        "<a href="#publiclyaccessible" title="PubliclyAccessible">PubliclyAccessible</a>" : <i>Boolean</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#configuration" title="Configuration">Configuration</a>" : <i>[ <a href="configurationdefinition.md">ConfigurationDefinition</a>, ... ]</i>,
        "<a href="#encryptionoptions" title="EncryptionOptions">EncryptionOptions</a>" : <i>[ <a href="encryptionoptionsdefinition.md">EncryptionOptionsDefinition</a>, ... ]</i>,
        "<a href="#ldapservermetadata" title="LdapServerMetadata">LdapServerMetadata</a>" : <i>[ <a href="ldapservermetadatadefinition.md">LdapServerMetadataDefinition</a>, ... ]</i>,
        "<a href="#logs" title="Logs">Logs</a>" : <i>[ <a href="logsdefinition.md">LogsDefinition</a>, ... ]</i>,
        "<a href="#maintenancewindowstarttime" title="MaintenanceWindowStartTime">MaintenanceWindowStartTime</a>" : <i>[ <a href="maintenancewindowstarttimedefinition.md">MaintenanceWindowStartTimeDefinition</a>, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>[ <a href="userdefinition.md">UserDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::MqBroker
Properties:
    <a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>: <i>Boolean</i>
    <a href="#authenticationstrategy" title="AuthenticationStrategy">AuthenticationStrategy</a>: <i>String</i>
    <a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>: <i>Boolean</i>
    <a href="#brokername" title="BrokerName">BrokerName</a>: <i>String</i>
    <a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>: <i>String</i>
    <a href="#enginetype" title="EngineType">EngineType</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>: <i>String</i>
    <a href="#publiclyaccessible" title="PubliclyAccessible">PubliclyAccessible</a>: <i>Boolean</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#configuration" title="Configuration">Configuration</a>: <i>
      - <a href="configurationdefinition.md">ConfigurationDefinition</a></i>
    <a href="#encryptionoptions" title="EncryptionOptions">EncryptionOptions</a>: <i>
      - <a href="encryptionoptionsdefinition.md">EncryptionOptionsDefinition</a></i>
    <a href="#ldapservermetadata" title="LdapServerMetadata">LdapServerMetadata</a>: <i>
      - <a href="ldapservermetadatadefinition.md">LdapServerMetadataDefinition</a></i>
    <a href="#logs" title="Logs">Logs</a>: <i>
      - <a href="logsdefinition.md">LogsDefinition</a></i>
    <a href="#maintenancewindowstarttime" title="MaintenanceWindowStartTime">MaintenanceWindowStartTime</a>: <i>
      - <a href="maintenancewindowstarttimedefinition.md">MaintenanceWindowStartTimeDefinition</a></i>
    <a href="#user" title="User">User</a>: <i>
      - <a href="userdefinition.md">UserDefinition</a></i>
</pre>

## Properties

#### ApplyImmediately

Specifies whether any broker modifications are applied immediately, or during the next maintenance window. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationStrategy

Authentication strategy used to secure the broker. Valid values are `simple` and `ldap`. `ldap` is not supported for `engine_type` `RabbitMQ`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMinorVersionUpgrade

Whether to automatically upgrade to new minor versions of brokers as Amazon MQ makes releases available.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrokerName

Name of the broker.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMode

Deployment mode of the broker. Valid values are `SINGLE_INSTANCE`, `ACTIVE_STANDBY_MULTI_AZ`, and `CLUSTER_MULTI_AZ`. Default is `SINGLE_INSTANCE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineType

Type of broker engine. Valid values are `ActiveMQ` and `RabbitMQ`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

Version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions. For example, `5.15.0`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostInstanceType

Broker's instance type. For example, `mq.t3.micro`, `mq.m5.large`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PubliclyAccessible

Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

List of security group IDs assigned to the broker.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

Storage type of the broker. For `engine_type` `ActiveMQ`, the valid values are `efs` and `ebs`, and the AWS-default is `efs`. For `engine_type` `RabbitMQ`, only `ebs` is supported. When using `ebs`, only the `mq.m5` broker instance type family is supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

List of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires multiple subnets.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the broker. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

_Required_: No

_Type_: List of <a href="configurationdefinition.md">ConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionOptions

_Required_: No

_Type_: List of <a href="encryptionoptionsdefinition.md">EncryptionOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapServerMetadata

_Required_: No

_Type_: List of <a href="ldapservermetadatadefinition.md">LdapServerMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logs

_Required_: No

_Type_: List of <a href="logsdefinition.md">LogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowStartTime

_Required_: No

_Type_: List of <a href="maintenancewindowstarttimedefinition.md">MaintenanceWindowStartTimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: List of <a href="userdefinition.md">UserDefinition</a>

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

