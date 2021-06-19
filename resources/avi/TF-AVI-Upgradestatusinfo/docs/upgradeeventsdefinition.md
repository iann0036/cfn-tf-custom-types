# TF::AVI::Upgradestatusinfo UpgradeEventsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#task" title="Task">Task</a>" : <i>String</i>,
    "<a href="#taskname" title="TaskName">TaskName</a>" : <i>String</i>,
    "<a href="#nodesevents" title="NodesEvents">NodesEvents</a>" : <i>[ <a href="nodeseventsdefinition.md">NodesEventsDefinition</a>, ... ]</i>,
    "<a href="#subevents" title="SubEvents">SubEvents</a>" : <i>[ <a href="subeventsdefinition.md">SubEventsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#task" title="Task">Task</a>: <i>String</i>
<a href="#taskname" title="TaskName">TaskName</a>: <i>String</i>
<a href="#nodesevents" title="NodesEvents">NodesEvents</a>: <i>
      - <a href="nodeseventsdefinition.md">NodesEventsDefinition</a></i>
<a href="#subevents" title="SubEvents">SubEvents</a>: <i>
      - <a href="subeventsdefinition.md">SubEventsDefinition</a></i>
</pre>

## Properties

#### Task

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodesEvents

_Required_: No

_Type_: List of <a href="nodeseventsdefinition.md">NodesEventsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubEvents

_Required_: No

_Type_: List of <a href="subeventsdefinition.md">SubEventsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

