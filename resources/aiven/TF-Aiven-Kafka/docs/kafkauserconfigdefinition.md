# TF::Aiven::Kafka KafkaUserConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customdomain" title="CustomDomain">CustomDomain</a>" : <i>String</i>,
    "<a href="#ipfilter" title="IpFilter">IpFilter</a>" : <i>[ String, ... ]</i>,
    "<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>" : <i>String</i>,
    "<a href="#kafkarest" title="KafkaRest">KafkaRest</a>" : <i>String</i>,
    "<a href="#kafkaversion" title="KafkaVersion">KafkaVersion</a>" : <i>String</i>,
    "<a href="#schemaregistry" title="SchemaRegistry">SchemaRegistry</a>" : <i>String</i>,
    "<a href="#kafka" title="Kafka">Kafka</a>" : <i>[ <a href="kafkadefinition.md">KafkaDefinition</a>, ... ]</i>,
    "<a href="#kafkaauthenticationmethods" title="KafkaAuthenticationMethods">KafkaAuthenticationMethods</a>" : <i>[ <a href="kafkaauthenticationmethodsdefinition.md">KafkaAuthenticationMethodsDefinition</a>, ... ]</i>,
    "<a href="#kafkaconnectconfig" title="KafkaConnectConfig">KafkaConnectConfig</a>" : <i>[ <a href="kafkaconnectconfigdefinition.md">KafkaConnectConfigDefinition</a>, ... ]</i>,
    "<a href="#kafkarestconfig" title="KafkaRestConfig">KafkaRestConfig</a>" : <i>[ <a href="kafkarestconfigdefinition.md">KafkaRestConfigDefinition</a>, ... ]</i>,
    "<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>" : <i>[ <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>, ... ]</i>,
    "<a href="#privatelinkaccess" title="PrivatelinkAccess">PrivatelinkAccess</a>" : <i>[ <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a>, ... ]</i>,
    "<a href="#publicaccess" title="PublicAccess">PublicAccess</a>" : <i>[ <a href="publicaccessdefinition.md">PublicAccessDefinition</a>, ... ]</i>,
    "<a href="#schemaregistryconfig" title="SchemaRegistryConfig">SchemaRegistryConfig</a>" : <i>[ <a href="schemaregistryconfigdefinition.md">SchemaRegistryConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customdomain" title="CustomDomain">CustomDomain</a>: <i>String</i>
<a href="#ipfilter" title="IpFilter">IpFilter</a>: <i>
      - String</i>
<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>: <i>String</i>
<a href="#kafkarest" title="KafkaRest">KafkaRest</a>: <i>String</i>
<a href="#kafkaversion" title="KafkaVersion">KafkaVersion</a>: <i>String</i>
<a href="#schemaregistry" title="SchemaRegistry">SchemaRegistry</a>: <i>String</i>
<a href="#kafka" title="Kafka">Kafka</a>: <i>
      - <a href="kafkadefinition.md">KafkaDefinition</a></i>
<a href="#kafkaauthenticationmethods" title="KafkaAuthenticationMethods">KafkaAuthenticationMethods</a>: <i>
      - <a href="kafkaauthenticationmethodsdefinition.md">KafkaAuthenticationMethodsDefinition</a></i>
<a href="#kafkaconnectconfig" title="KafkaConnectConfig">KafkaConnectConfig</a>: <i>
      - <a href="kafkaconnectconfigdefinition.md">KafkaConnectConfigDefinition</a></i>
<a href="#kafkarestconfig" title="KafkaRestConfig">KafkaRestConfig</a>: <i>
      - <a href="kafkarestconfigdefinition.md">KafkaRestConfigDefinition</a></i>
<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>: <i>
      - <a href="privateaccessdefinition.md">PrivateAccessDefinition</a></i>
<a href="#privatelinkaccess" title="PrivatelinkAccess">PrivatelinkAccess</a>: <i>
      - <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a></i>
<a href="#publicaccess" title="PublicAccess">PublicAccess</a>: <i>
      - <a href="publicaccessdefinition.md">PublicAccessDefinition</a></i>
<a href="#schemaregistryconfig" title="SchemaRegistryConfig">SchemaRegistryConfig</a>: <i>
      - <a href="schemaregistryconfigdefinition.md">SchemaRegistryConfigDefinition</a></i>
</pre>

## Properties

#### CustomDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFilter

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaConnect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaRest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaRegistry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kafka

_Required_: No

_Type_: List of <a href="kafkadefinition.md">KafkaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaAuthenticationMethods

_Required_: No

_Type_: List of <a href="kafkaauthenticationmethodsdefinition.md">KafkaAuthenticationMethodsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaConnectConfig

_Required_: No

_Type_: List of <a href="kafkaconnectconfigdefinition.md">KafkaConnectConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaRestConfig

_Required_: No

_Type_: List of <a href="kafkarestconfigdefinition.md">KafkaRestConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAccess

_Required_: No

_Type_: List of <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivatelinkAccess

_Required_: No

_Type_: List of <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccess

_Required_: No

_Type_: List of <a href="publicaccessdefinition.md">PublicAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaRegistryConfig

_Required_: No

_Type_: List of <a href="schemaregistryconfigdefinition.md">SchemaRegistryConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

