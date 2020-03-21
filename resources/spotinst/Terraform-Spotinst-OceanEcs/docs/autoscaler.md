# Terraform::Spotinst::OceanEcs Autoscaler

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldown" title="Cooldown">Cooldown</a>" : <i>Double</i>,
    "<a href="#isautoconfig" title="IsAutoConfig">IsAutoConfig</a>" : <i>Boolean</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#down" title="Down">Down</a>" : <i>[ &lt;a href=&#34;autoscaler-down.md&#34;&gt;Down&lt;/a&gt;, ... ]</i>,
    "<a href="#headroom" title="Headroom">Headroom</a>" : <i>[ &lt;a href=&#34;autoscaler-headroom.md&#34;&gt;Headroom&lt;/a&gt;, ... ]</i>,
    "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ &lt;a href=&#34;autoscaler-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cooldown" title="Cooldown">Cooldown</a>: <i>Double</i>
<a href="#isautoconfig" title="IsAutoConfig">IsAutoConfig</a>: <i>Boolean</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#down" title="Down">Down</a>: <i>
      - &lt;a href=&#34;autoscaler-down.md&#34;&gt;Down&lt;/a&gt;</i>
<a href="#headroom" title="Headroom">Headroom</a>: <i>
      - &lt;a href=&#34;autoscaler-headroom.md&#34;&gt;Headroom&lt;/a&gt;</i>
<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - &lt;a href=&#34;autoscaler-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;autoscaler-down.md&#34;&gt;Down&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headroom

_Required_: No
_Type_: List of &lt;a href=&#34;autoscaler-headroom.md&#34;&gt;Headroom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No
_Type_: List of &lt;a href=&#34;autoscaler-resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

