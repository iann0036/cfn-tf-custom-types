# TF::Aiven::KafkaConnect PublicAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>" : <i>[ <a href="kafkaconnectdefinition.md">KafkaConnectDefinition</a>, ... ]</i>,
    "<a href="#prometheus" title="Prometheus">Prometheus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#kafkaconnect" title="KafkaConnect">KafkaConnect</a>: <i>
      - <a href="kafkaconnectdefinition.md">KafkaConnectDefinition</a></i>
<a href="#prometheus" title="Prometheus">Prometheus</a>: <i>String</i>
</pre>

## Properties

#### KafkaConnect

_Required_: No

_Type_: List of <a href="kafkaconnectdefinition.md">KafkaConnectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prometheus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
