# Terraform::Google::ContainerCluster NodePool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>" : <i>Double</i>,
    "<a href="#maxpodspernode" title="MaxPodsPerNode">MaxPodsPerNode</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
    "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#autoscaling" title="Autoscaling">Autoscaling</a>" : <i>[ &lt;a href=&#34;nodepool-autoscaling.md&#34;&gt;Autoscaling&lt;/a&gt;, ... ]</i>,
    "<a href="#management" title="Management">Management</a>" : <i>[ &lt;a href=&#34;nodepool-management.md&#34;&gt;Management&lt;/a&gt;, ... ]</i>,
    "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ &lt;a href=&#34;nodepool-nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>: <i>Double</i>
<a href="#maxpodspernode" title="MaxPodsPerNode">MaxPodsPerNode</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
<a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#autoscaling" title="Autoscaling">Autoscaling</a>: <i>
      - &lt;a href=&#34;nodepool-autoscaling.md&#34;&gt;Autoscaling&lt;/a&gt;</i>
<a href="#management" title="Management">Management</a>: <i>
      - &lt;a href=&#34;nodepool-management.md&#34;&gt;Management&lt;/a&gt;</i>
<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - &lt;a href=&#34;nodepool-nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;</i>
</pre>

## Properties

#### InitialNodeCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPodsPerNode

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaling

_Required_: No
_Type_: List of &lt;a href=&#34;nodepool-autoscaling.md&#34;&gt;Autoscaling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No
_Type_: List of &lt;a href=&#34;nodepool-management.md&#34;&gt;Management&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No
_Type_: List of &lt;a href=&#34;nodepool-nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

