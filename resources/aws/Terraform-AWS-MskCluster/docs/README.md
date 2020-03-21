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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#brokernodegroupinfo" title="BrokerNodeGroupInfo">BrokerNodeGroupInfo</a>" : <i>[ &lt;a href=&#34;brokernodegroupinfo.md&#34;&gt;BrokerNodeGroupInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#clientauthentication" title="ClientAuthentication">ClientAuthentication</a>" : <i>[ &lt;a href=&#34;clientauthentication.md&#34;&gt;ClientAuthentication&lt;/a&gt;, ... ]</i>,
        "<a href="#configurationinfo" title="ConfigurationInfo">ConfigurationInfo</a>" : <i>[ &lt;a href=&#34;configurationinfo.md&#34;&gt;ConfigurationInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#encryptioninfo" title="EncryptionInfo">EncryptionInfo</a>" : <i>[ &lt;a href=&#34;encryptioninfo.md&#34;&gt;EncryptionInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#openmonitoring" title="OpenMonitoring">OpenMonitoring</a>" : <i>[ &lt;a href=&#34;openmonitoring.md&#34;&gt;OpenMonitoring&lt;/a&gt;, ... ]</i>,
        "<a href="#tls" title="Tls">Tls</a>" : <i>[ &lt;a href=&#34;tls.md&#34;&gt;Tls&lt;/a&gt;, ... ]</i>,
        "<a href="#encryptionintransit" title="EncryptionInTransit">EncryptionInTransit</a>" : <i>[ &lt;a href=&#34;encryptionintransit.md&#34;&gt;EncryptionInTransit&lt;/a&gt;, ... ]</i>,
        "<a href="#prometheus" title="Prometheus">Prometheus</a>" : <i>[ &lt;a href=&#34;prometheus.md&#34;&gt;Prometheus&lt;/a&gt;, ... ]</i>,
        "<a href="#jmxexporter" title="JmxExporter">JmxExporter</a>" : <i>[ &lt;a href=&#34;jmxexporter.md&#34;&gt;JmxExporter&lt;/a&gt;, ... ]</i>,
        "<a href="#nodeexporter" title="NodeExporter">NodeExporter</a>" : <i>[ &lt;a href=&#34;nodeexporter.md&#34;&gt;NodeExporter&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#brokernodegroupinfo" title="BrokerNodeGroupInfo">BrokerNodeGroupInfo</a>: <i>
      - &lt;a href=&#34;brokernodegroupinfo.md&#34;&gt;BrokerNodeGroupInfo&lt;/a&gt;</i>
    <a href="#clientauthentication" title="ClientAuthentication">ClientAuthentication</a>: <i>
      - &lt;a href=&#34;clientauthentication.md&#34;&gt;ClientAuthentication&lt;/a&gt;</i>
    <a href="#configurationinfo" title="ConfigurationInfo">ConfigurationInfo</a>: <i>
      - &lt;a href=&#34;configurationinfo.md&#34;&gt;ConfigurationInfo&lt;/a&gt;</i>
    <a href="#encryptioninfo" title="EncryptionInfo">EncryptionInfo</a>: <i>
      - &lt;a href=&#34;encryptioninfo.md&#34;&gt;EncryptionInfo&lt;/a&gt;</i>
    <a href="#openmonitoring" title="OpenMonitoring">OpenMonitoring</a>: <i>
      - &lt;a href=&#34;openmonitoring.md&#34;&gt;OpenMonitoring&lt;/a&gt;</i>
    <a href="#tls" title="Tls">Tls</a>: <i>
      - &lt;a href=&#34;tls.md&#34;&gt;Tls&lt;/a&gt;</i>
    <a href="#encryptionintransit" title="EncryptionInTransit">EncryptionInTransit</a>: <i>
      - &lt;a href=&#34;encryptionintransit.md&#34;&gt;EncryptionInTransit&lt;/a&gt;</i>
    <a href="#prometheus" title="Prometheus">Prometheus</a>: <i>
      - &lt;a href=&#34;prometheus.md&#34;&gt;Prometheus&lt;/a&gt;</i>
    <a href="#jmxexporter" title="JmxExporter">JmxExporter</a>: <i>
      - &lt;a href=&#34;jmxexporter.md&#34;&gt;JmxExporter&lt;/a&gt;</i>
    <a href="#nodeexporter" title="NodeExporter">NodeExporter</a>: <i>
      - &lt;a href=&#34;nodeexporter.md&#34;&gt;NodeExporter&lt;/a&gt;</i>
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

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrokerNodeGroupInfo

_Required_: No

_Type_: List of &lt;a href=&#34;brokernodegroupinfo.md&#34;&gt;BrokerNodeGroupInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthentication

_Required_: No

_Type_: List of &lt;a href=&#34;clientauthentication.md&#34;&gt;ClientAuthentication&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationInfo

_Required_: No

_Type_: List of &lt;a href=&#34;configurationinfo.md&#34;&gt;ConfigurationInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionInfo

_Required_: No

_Type_: List of &lt;a href=&#34;encryptioninfo.md&#34;&gt;EncryptionInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenMonitoring

_Required_: No

_Type_: List of &lt;a href=&#34;openmonitoring.md&#34;&gt;OpenMonitoring&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No

_Type_: List of &lt;a href=&#34;tls.md&#34;&gt;Tls&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionInTransit

_Required_: No

_Type_: List of &lt;a href=&#34;encryptionintransit.md&#34;&gt;EncryptionInTransit&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prometheus

_Required_: No

_Type_: List of &lt;a href=&#34;prometheus.md&#34;&gt;Prometheus&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JmxExporter

_Required_: No

_Type_: List of &lt;a href=&#34;jmxexporter.md&#34;&gt;JmxExporter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeExporter

_Required_: No

_Type_: List of &lt;a href=&#34;nodeexporter.md&#34;&gt;NodeExporter&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### BootstrapBrokers

Returns the &lt;code&gt;BootstrapBrokers&lt;/code&gt; value.

#### BootstrapBrokersTls

Returns the &lt;code&gt;BootstrapBrokersTls&lt;/code&gt; value.

#### CurrentVersion

Returns the &lt;code&gt;CurrentVersion&lt;/code&gt; value.

#### ZookeeperConnectString

Returns the &lt;code&gt;ZookeeperConnectString&lt;/code&gt; value.

