# TF::Google::ContainerCluster ClusterAutoscalingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>" : <i>[ <a href="autoprovisioningdefaultsdefinition.md">AutoProvisioningDefaultsDefinition</a>, ... ]</i>,
    "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>: <i>
      - <a href="autoprovisioningdefaultsdefinition.md">AutoProvisioningDefaultsDefinition</a></i>
<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a></i>
</pre>

## Properties

#### Enabled

Whether node auto-provisioning is enabled. Resource
limits for `cpu` and `memory` must be defined to enable node auto-provisioning.

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

