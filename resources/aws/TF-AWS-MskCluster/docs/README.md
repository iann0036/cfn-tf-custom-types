# TF::AWS::MskCluster

Manages AWS Managed Streaming for Kafka cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::MskCluster",
    "Properties" : {
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#enhancedmonitoring" title="EnhancedMonitoring">EnhancedMonitoring</a>" : <i>String</i>,
        "<a href="#kafkaversion" title="KafkaVersion">KafkaVersion</a>" : <i>String</i>,
        "<a href="#numberofbrokernodes" title="NumberOfBrokerNodes">NumberOfBrokerNodes</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#brokernodegroupinfo" title="BrokerNodeGroupInfo">BrokerNodeGroupInfo</a>" : <i>[ <a href="brokernodegroupinfodefinition.md">BrokerNodeGroupInfoDefinition</a>, ... ]</i>,
        "<a href="#clientauthentication" title="ClientAuthentication">ClientAuthentication</a>" : <i>[ <a href="clientauthenticationdefinition.md">ClientAuthenticationDefinition</a>, ... ]</i>,
        "<a href="#configurationinfo" title="ConfigurationInfo">ConfigurationInfo</a>" : <i>[ <a href="configurationinfodefinition.md">ConfigurationInfoDefinition</a>, ... ]</i>,
        "<a href="#encryptioninfo" title="EncryptionInfo">EncryptionInfo</a>" : <i>[ <a href="encryptioninfodefinition.md">EncryptionInfoDefinition</a>, ... ]</i>,
        "<a href="#logginginfo" title="LoggingInfo">LoggingInfo</a>" : <i>[ <a href="logginginfodefinition.md">LoggingInfoDefinition</a>, ... ]</i>,
        "<a href="#openmonitoring" title="OpenMonitoring">OpenMonitoring</a>" : <i>[ <a href="openmonitoringdefinition.md">OpenMonitoringDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::MskCluster
Properties:
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#enhancedmonitoring" title="EnhancedMonitoring">EnhancedMonitoring</a>: <i>String</i>
    <a href="#kafkaversion" title="KafkaVersion">KafkaVersion</a>: <i>String</i>
    <a href="#numberofbrokernodes" title="NumberOfBrokerNodes">NumberOfBrokerNodes</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#brokernodegroupinfo" title="BrokerNodeGroupInfo">BrokerNodeGroupInfo</a>: <i>
      - <a href="brokernodegroupinfodefinition.md">BrokerNodeGroupInfoDefinition</a></i>
    <a href="#clientauthentication" title="ClientAuthentication">ClientAuthentication</a>: <i>
      - <a href="clientauthenticationdefinition.md">ClientAuthenticationDefinition</a></i>
    <a href="#configurationinfo" title="ConfigurationInfo">ConfigurationInfo</a>: <i>
      - <a href="configurationinfodefinition.md">ConfigurationInfoDefinition</a></i>
    <a href="#encryptioninfo" title="EncryptionInfo">EncryptionInfo</a>: <i>
      - <a href="encryptioninfodefinition.md">EncryptionInfoDefinition</a></i>
    <a href="#logginginfo" title="LoggingInfo">LoggingInfo</a>: <i>
      - <a href="logginginfodefinition.md">LoggingInfoDefinition</a></i>
    <a href="#openmonitoring" title="OpenMonitoring">OpenMonitoring</a>: <i>
      - <a href="openmonitoringdefinition.md">OpenMonitoringDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ClusterName

Name of the MSK cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedMonitoring

Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaVersion

Specify the desired Kafka software version.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfBrokerNodes

The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrokerNodeGroupInfo

_Required_: No

_Type_: List of <a href="brokernodegroupinfodefinition.md">BrokerNodeGroupInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthentication

_Required_: No

_Type_: List of <a href="clientauthenticationdefinition.md">ClientAuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationInfo

_Required_: No

_Type_: List of <a href="configurationinfodefinition.md">ConfigurationInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionInfo

_Required_: No

_Type_: List of <a href="encryptioninfodefinition.md">EncryptionInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingInfo

_Required_: No

_Type_: List of <a href="logginginfodefinition.md">LoggingInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenMonitoring

_Required_: No

_Type_: List of <a href="openmonitoringdefinition.md">OpenMonitoringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### BootstrapBrokers

Returns the <code>BootstrapBrokers</code> value.

#### BootstrapBrokersSaslIam

Returns the <code>BootstrapBrokersSaslIam</code> value.

#### BootstrapBrokersSaslScram

Returns the <code>BootstrapBrokersSaslScram</code> value.

#### BootstrapBrokersTls

Returns the <code>BootstrapBrokersTls</code> value.

#### CurrentVersion

Returns the <code>CurrentVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### ZookeeperConnectString

Returns the <code>ZookeeperConnectString</code> value.

