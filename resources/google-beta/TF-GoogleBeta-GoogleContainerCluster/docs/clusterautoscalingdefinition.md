# TF::GoogleBeta::GoogleContainerCluster ClusterAutoscalingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalingprofile" title="AutoscalingProfile">AutoscalingProfile</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>" : <i>[ <a href="autoprovisioningdefaultsdefinition.md">AutoProvisioningDefaultsDefinition</a>, ... ]</i>,
    "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalingprofile" title="AutoscalingProfile">AutoscalingProfile</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>: <i>
      - <a href="autoprovisioningdefaultsdefinition.md">AutoProvisioningDefaultsDefinition</a></i>
<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a></i>
</pre>

## Properties

#### AutoscalingProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoProvisioningDefaults

_Required_: No

_Type_: List of <a href="autoprovisioningdefaultsdefinition.md">AutoProvisioningDefaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

