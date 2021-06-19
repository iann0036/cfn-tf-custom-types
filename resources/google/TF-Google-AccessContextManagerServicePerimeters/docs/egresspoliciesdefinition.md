# TF::Google::AccessContextManagerServicePerimeters EgressPoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#egressfrom" title="EgressFrom">EgressFrom</a>" : <i>[ <a href="egressfromdefinition.md">EgressFromDefinition</a>, ... ]</i>,
    "<a href="#egressto" title="EgressTo">EgressTo</a>" : <i>[ <a href="egresstodefinition.md">EgressToDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#egressfrom" title="EgressFrom">EgressFrom</a>: <i>
      - <a href="egressfromdefinition.md">EgressFromDefinition</a></i>
<a href="#egressto" title="EgressTo">EgressTo</a>: <i>
      - <a href="egresstodefinition.md">EgressToDefinition</a></i>
</pre>

## Properties

#### EgressFrom

_Required_: No

_Type_: List of <a href="egressfromdefinition.md">EgressFromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressTo

_Required_: No

_Type_: List of <a href="egresstodefinition.md">EgressToDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

