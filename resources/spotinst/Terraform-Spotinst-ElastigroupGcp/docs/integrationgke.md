# Terraform::Spotinst::ElastigroupGcp IntegrationGke

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoupdate" title="AutoUpdate">AutoUpdate</a>" : <i>Boolean</i>,
    "<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>" : <i>Double</i>,
    "<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>" : <i>Boolean</i>,
    "<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>" : <i>Boolean</i>,
    "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ &lt;a href=&#34;integrationgke-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;, ... ]</i>,
    "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ &lt;a href=&#34;integrationgke-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;, ... ]</i>,
    "<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>" : <i>[ &lt;a href=&#34;integrationgke-autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoupdate" title="AutoUpdate">AutoUpdate</a>: <i>Boolean</i>
<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>: <i>Double</i>
<a href="#autoscaleisautoconfig" title="AutoscaleIsAutoConfig">AutoscaleIsAutoConfig</a>: <i>Boolean</i>
<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>: <i>Boolean</i>
<a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - &lt;a href=&#34;integrationgke-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;</i>
<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - &lt;a href=&#34;integrationgke-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;</i>
<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>: <i>
      - &lt;a href=&#34;integrationgke-autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;</i>
</pre>

## Properties

#### AutoUpdate

_Required_: No
_Type_: Boolean

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

#### ClusterId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No
_Type_: List of &lt;a href=&#34;integrationgke-autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No
_Type_: List of &lt;a href=&#34;integrationgke-autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleLabels

_Required_: No
_Type_: List of &lt;a href=&#34;integrationgke-autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

