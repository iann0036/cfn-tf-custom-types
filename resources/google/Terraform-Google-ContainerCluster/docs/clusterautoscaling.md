# Terraform::Google::ContainerCluster ClusterAutoscaling

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>" : <i>[ &lt;a href=&#34;clusterautoscaling-autoprovisioningdefaults.md&#34;&gt;AutoProvisioningDefaults&lt;/a&gt;, ... ]</i>,
    "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ &lt;a href=&#34;clusterautoscaling-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>: <i>
      - &lt;a href=&#34;clusterautoscaling-autoprovisioningdefaults.md&#34;&gt;AutoProvisioningDefaults&lt;/a&gt;</i>
<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - &lt;a href=&#34;clusterautoscaling-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;</i>
</pre>

## Properties

#### Enabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoProvisioningDefaults

_Required_: No
_Type_: List of &lt;a href=&#34;clusterautoscaling-autoprovisioningdefaults.md&#34;&gt;AutoProvisioningDefaults&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No
_Type_: List of &lt;a href=&#34;clusterautoscaling-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

