# TF::Spotinst::OceanAws AutoscalerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoheadroompercentage" title="AutoHeadroomPercentage">AutoHeadroomPercentage</a>" : <i>Double</i>,
    "<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>" : <i>Double</i>,
    "<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>" : <i>Boolean</i>,
    "<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>" : <i>Boolean</i>,
    "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>, ... ]</i>,
    "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>, ... ]</i>,
    "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoheadroompercentage" title="AutoHeadroomPercentage">AutoHeadroomPercentage</a>: <i>Double</i>
<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>: <i>Double</i>
<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>: <i>Boolean</i>
<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>: <i>Boolean</i>
<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a></i>
<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a></i>
<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a></i>
</pre>

## Properties

#### AutoHeadroomPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleCooldown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleIsAutoConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleIsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
