# Terraform::AWS::MskCluster

CloudFormation equivalent of aws_msk_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::MskCluster",
    "Properties" : {
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#enhancedmonitoring" title="EnhancedMonitoring">EnhancedMonitoring</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#kafkaversion" title="KafkaVersion">KafkaVersion</a>" : <i>String</i>,
        "<a href="#numberofbrokernodes" title="NumberOfBrokerNodes">NumberOfBrokerNodes</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#brokernodegroupinfo" title="BrokerNodeGroupInfo">BrokerNodeGroupInfo</a>" : <i>[ <a href="brokernodegroupinfo.md">BrokerNodeGroupInfo</a>, ... ]</i>,
        "<a href="#clientauthentication" title="ClientAuthentication">ClientAuthentication</a>" : <i>[ <a href="clientauthentication.md">ClientAuthentication</a>, ... ]</i>,
        "<a href="#configurationinfo" title="ConfigurationInfo">ConfigurationInfo</a>" : <i>[ <a href="configurationinfo.md">ConfigurationInfo</a>, ... ]</i>,
        "<a href="#encryptioninfo" title="EncryptionInfo">EncryptionInfo</a>" : <i>[ <a href="encryptioninfo.md">EncryptionInfo</a>, ... ]</i>,
        "<a href="#openmonitoring" title="OpenMonitoring">OpenMonitoring</a>" : <i>[ <a href="openmonitoring.md">OpenMonitoring</a>, ... ]</i>,
        "<a href="#tls" title="Tls">Tls</a>" : <i>[ <a href="tls.md">Tls</a>, ... ]</i>,
        "<a href="#encryptionintransit" title="EncryptionInTransit">EncryptionInTransit</a>" : <i>[ <a href="encryptionintransit.md">EncryptionInTransit</a>, ... ]</i>,
        "<a href="#prometheus" title="Prometheus">Prometheus</a>" : <i>[ <a href="prometheus.md">Prometheus</a>, ... ]</i>,
        "<a href="#jmxexporter" title="JmxExporter">JmxExporter</a>" : <i>[ <a href="jmxexporter.md">JmxExporter</a>, ... ]</i>,
        "<a href="#nodeexporter" title="NodeExporter">NodeExporter</a>" : <i>[ <a href="nodeexporter.md">NodeExporter</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::MskCluster
Properties:
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#enhancedmonitoring" title="EnhancedMonitoring">EnhancedMonitoring</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#kafkaversion" title="KafkaVersion">KafkaVersion</a>: <i>String</i>
    <a href="#numberofbrokernodes" title="NumberOfBrokerNodes">NumberOfBrokerNodes</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#brokernodegroupinfo" title="BrokerNodeGroupInfo">BrokerNodeGroupInfo</a>: <i>
      - <a href="brokernodegroupinfo.md">BrokerNodeGroupInfo</a></i>
    <a href="#clientauthentication" title="ClientAuthentication">ClientAuthentication</a>: <i>
      - <a href="clientauthentication.md">ClientAuthentication</a></i>
    <a href="#configurationinfo" title="ConfigurationInfo">ConfigurationInfo</a>: <i>
      - <a href="configurationinfo.md">ConfigurationInfo</a></i>
    <a href="#encryptioninfo" title="EncryptionInfo">EncryptionInfo</a>: <i>
      - <a href="encryptioninfo.md">EncryptionInfo</a></i>
    <a href="#openmonitoring" title="OpenMonitoring">OpenMonitoring</a>: <i>
      - <a href="openmonitoring.md">OpenMonitoring</a></i>
    <a href="#tls" title="Tls">Tls</a>: <i>
      - <a href="tls.md">Tls</a></i>
    <a href="#encryptionintransit" title="EncryptionInTransit">EncryptionInTransit</a>: <i>
      - <a href="encryptionintransit.md">EncryptionInTransit</a></i>
    <a href="#prometheus" title="Prometheus">Prometheus</a>: <i>
      - <a href="prometheus.md">Prometheus</a></i>
    <a href="#jmxexporter" title="JmxExporter">JmxExporter</a>: <i>
      - <a href="jmxexporter.md">JmxExporter</a></i>
    <a href="#nodeexporter" title="NodeExporter">NodeExporter</a>: <i>
      - <a href="nodeexporter.md">NodeExporter</a></i>
</pre>

## Properties

#### ClusterName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedMonitoring

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfBrokerNodes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrokerNodeGroupInfo

_Required_: No

_Type_: List of <a href="brokernodegroupinfo.md">BrokerNodeGroupInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthentication

_Required_: No

_Type_: List of <a href="clientauthentication.md">ClientAuthentication</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationInfo

_Required_: No

_Type_: List of <a href="configurationinfo.md">ConfigurationInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionInfo

_Required_: No

_Type_: List of <a href="encryptioninfo.md">EncryptionInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenMonitoring

_Required_: No

_Type_: List of <a href="openmonitoring.md">OpenMonitoring</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No

_Type_: List of <a href="tls.md">Tls</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionInTransit

_Required_: No

_Type_: List of <a href="encryptionintransit.md">EncryptionInTransit</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prometheus

_Required_: No

_Type_: List of <a href="prometheus.md">Prometheus</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JmxExporter

_Required_: No

_Type_: List of <a href="jmxexporter.md">JmxExporter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeExporter

_Required_: No

_Type_: List of <a href="nodeexporter.md">NodeExporter</a>

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

#### BootstrapBrokersTls

Returns the <code>BootstrapBrokersTls</code> value.

#### CurrentVersion

Returns the <code>CurrentVersion</code> value.

#### ZookeeperConnectString

Returns the <code>ZookeeperConnectString</code> value.

