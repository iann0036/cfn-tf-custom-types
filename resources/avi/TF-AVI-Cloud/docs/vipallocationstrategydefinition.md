# TF::AVI::Cloud VipAllocationStrategyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#ilb" title="Ilb">Ilb</a>" : <i>[ <a href="ilbdefinition.md">IlbDefinition</a>, ... ]</i>,
    "<a href="#routes" title="Routes">Routes</a>" : <i>[ <a href="routesdefinition.md">RoutesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#ilb" title="Ilb">Ilb</a>: <i>
      - <a href="ilbdefinition.md">IlbDefinition</a></i>
<a href="#routes" title="Routes">Routes</a>: <i>
      - <a href="routesdefinition.md">RoutesDefinition</a></i>
</pre>

## Properties

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ilb

_Required_: No

_Type_: List of <a href="ilbdefinition.md">IlbDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No

_Type_: List of <a href="routesdefinition.md">RoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

