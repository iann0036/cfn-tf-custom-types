# TF::Spotinst::ElastigroupAws IntegrationKubernetesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apiserver" title="ApiServer">ApiServer</a>" : <i>String</i>,
    "<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>" : <i>Double</i>,
    "<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>" : <i>Boolean</i>,
    "<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>" : <i>Boolean</i>,
    "<a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>" : <i>String</i>,
    "<a href="#integrationmode" title="IntegrationMode">IntegrationMode</a>" : <i>String</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>,
    "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>, ... ]</i>,
    "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>, ... ]</i>,
    "<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>" : <i>[ <a href="autoscalelabelsdefinition.md">AutoscaleLabelsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#apiserver" title="ApiServer">ApiServer</a>: <i>String</i>
<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>: <i>Double</i>
<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>: <i>Boolean</i>
<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>: <i>Boolean</i>
<a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>: <i>String</i>
<a href="#integrationmode" title="IntegrationMode">IntegrationMode</a>: <i>String</i>
<a href="#token" title="Token">Token</a>: <i>String</i>
<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a></i>
<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a></i>
<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>: <i>
      - <a href="autoscalelabelsdefinition.md">AutoscaleLabelsDefinition</a></i>
</pre>

## Properties

#### ApiServer

_Required_: No

_Type_: String

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

#### ClusterIdentifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleLabels

_Required_: No

_Type_: List of <a href="autoscalelabelsdefinition.md">AutoscaleLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

