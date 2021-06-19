# TF::Spotinst::OceanEcs AutoscalerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldown" title="Cooldown">Cooldown</a>" : <i>Double</i>,
    "<a href="#isautoconfig" title="IsAutoConfig">IsAutoConfig</a>" : <i>Boolean</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#down" title="Down">Down</a>" : <i>[ <a href="downdefinition.md">DownDefinition</a>, ... ]</i>,
    "<a href="#headroom" title="Headroom">Headroom</a>" : <i>[ <a href="headroomdefinition.md">HeadroomDefinition</a>, ... ]</i>,
    "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cooldown" title="Cooldown">Cooldown</a>: <i>Double</i>
<a href="#isautoconfig" title="IsAutoConfig">IsAutoConfig</a>: <i>Boolean</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#down" title="Down">Down</a>: <i>
      - <a href="downdefinition.md">DownDefinition</a></i>
<a href="#headroom" title="Headroom">Headroom</a>: <i>
      - <a href="headroomdefinition.md">HeadroomDefinition</a></i>
<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a></i>
</pre>

## Properties

#### Cooldown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Down

_Required_: No

_Type_: List of <a href="downdefinition.md">DownDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headroom

_Required_: No

_Type_: List of <a href="headroomdefinition.md">HeadroomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

