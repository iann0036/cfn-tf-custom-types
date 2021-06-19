# TF::Volterra::AwsTgwSite NewTgwDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#systemgenerated" title="SystemGenerated">SystemGenerated</a>" : <i>Boolean</i>,
    "<a href="#userassigned" title="UserAssigned">UserAssigned</a>" : <i>[ <a href="userassigneddefinition.md">UserAssignedDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#systemgenerated" title="SystemGenerated">SystemGenerated</a>: <i>Boolean</i>
<a href="#userassigned" title="UserAssigned">UserAssigned</a>: <i>
      - <a href="userassigneddefinition.md">UserAssignedDefinition</a></i>
</pre>

## Properties

#### SystemGenerated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAssigned

_Required_: No

_Type_: List of <a href="userassigneddefinition.md">UserAssignedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

