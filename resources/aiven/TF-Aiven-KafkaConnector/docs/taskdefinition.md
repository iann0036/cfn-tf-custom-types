# TF::Aiven::KafkaConnector TaskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connector" title="Connector">Connector</a>" : <i>String</i>,
    "<a href="#task" title="Task">Task</a>" : <i>[ <a href="taskdefinition.md">TaskDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connector" title="Connector">Connector</a>: <i>String</i>
<a href="#task" title="Task">Task</a>: <i>
      - <a href="taskdefinition.md">TaskDefinition</a></i>
</pre>

## Properties

#### Connector

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Task

_Required_: No

_Type_: List of <a href="taskdefinition.md">TaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

