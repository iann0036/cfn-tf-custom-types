# TF::Spotinst::ElastigroupAws IntegrationEcsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>" : <i>Double</i>,
    "<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>" : <i>Boolean</i>,
    "<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>" : <i>Boolean</i>,
    "<a href="#autoscalescaledownnonservicetasks" title="AutoscaleScaleDownNonServiceTasks">AutoscaleScaleDownNonServiceTasks</a>" : <i>Boolean</i>,
    "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
    "<a href="#autoscaleattributes" title="AutoscaleAttributes">AutoscaleAttributes</a>" : <i>[ <a href="autoscaleattributesdefinition.md">AutoscaleAttributesDefinition</a>, ... ]</i>,
    "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>, ... ]</i>,
    "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>, ... ]</i>,
    "<a href="#batch" title="Batch">Batch</a>" : <i>[ <a href="batchdefinition.md">BatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>: <i>Double</i>
<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>: <i>Boolean</i>
<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>: <i>Boolean</i>
<a href="#autoscalescaledownnonservicetasks" title="AutoscaleScaleDownNonServiceTasks">AutoscaleScaleDownNonServiceTasks</a>: <i>Boolean</i>
<a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
<a href="#autoscaleattributes" title="AutoscaleAttributes">AutoscaleAttributes</a>: <i>
      - <a href="autoscaleattributesdefinition.md">AutoscaleAttributesDefinition</a></i>
<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a></i>
<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a></i>
<a href="#batch" title="Batch">Batch</a>: <i>
      - <a href="batchdefinition.md">BatchDefinition</a></i>
</pre>

## Properties

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

#### AutoscaleScaleDownNonServiceTasks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleAttributes

_Required_: No

_Type_: List of <a href="autoscaleattributesdefinition.md">AutoscaleAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Batch

_Required_: No

_Type_: List of <a href="batchdefinition.md">BatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

