# Terraform::Spotinst::ElastigroupAws IntegrationDockerSwarm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>" : <i>Double</i>,
    "<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>" : <i>Boolean</i>,
    "<a href="#masterhost" title="MasterHost">MasterHost</a>" : <i>String</i>,
    "<a href="#masterport" title="MasterPort">MasterPort</a>" : <i>Double</i>,
    "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ &lt;a href=&#34;integrationdockerswarm-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;, ... ]</i>,
    "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ &lt;a href=&#34;integrationdockerswarm-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>: <i>Double</i>
<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>: <i>Boolean</i>
<a href="#masterhost" title="MasterHost">MasterHost</a>: <i>String</i>
<a href="#masterport" title="MasterPort">MasterPort</a>: <i>Double</i>
<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - &lt;a href=&#34;integrationdockerswarm-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;</i>
<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - &lt;a href=&#34;integrationdockerswarm-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;</i>
</pre>

## Properties

#### AutoscaleCooldown

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleIsEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterHost

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterPort

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No
_Type_: List of &lt;a href=&#34;integrationdockerswarm-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No
_Type_: List of &lt;a href=&#34;integrationdockerswarm-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

