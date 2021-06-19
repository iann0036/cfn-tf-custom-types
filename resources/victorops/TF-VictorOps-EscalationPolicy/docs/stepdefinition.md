# TF::VictorOps::EscalationPolicy StepDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#entries" title="Entries">Entries</a>" : <i>[ [ <a href="entriesdefinition.md">EntriesDefinition</a>, ... ], ... ]</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#entries" title="Entries">Entries</a>: <i>
      - 
      - <a href="entriesdefinition.md">EntriesDefinition</a></i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
</pre>

## Properties

#### Entries

_Required_: Yes

_Type_: List of List of <a href="entriesdefinition.md">EntriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

