# TF::Aiven::Kafka PrivatelinkAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kafka" title="Kafka">Kafka</a>" : <i>[ <a href="kafkadefinition.md">KafkaDefinition</a>, ... ]</i>,
    "<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>" : <i>String</i>,
    "<a href="#kafkarest" title="KafkaRest">KafkaRest</a>" : <i>String</i>,
    "<a href="#schemaregistry" title="SchemaRegistry">SchemaRegistry</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#kafka" title="Kafka">Kafka</a>: <i>
      - <a href="kafkadefinition.md">KafkaDefinition</a></i>
<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>: <i>String</i>
<a href="#kafkarest" title="KafkaRest">KafkaRest</a>: <i>String</i>
<a href="#schemaregistry" title="SchemaRegistry">SchemaRegistry</a>: <i>String</i>
</pre>

## Properties

#### Kafka

_Required_: No

_Type_: List of <a href="kafkadefinition.md">KafkaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaConnect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaRest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaRegistry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

