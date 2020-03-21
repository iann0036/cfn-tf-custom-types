# Terraform::Spotinst::ElastigroupAws UpdatePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoapplytags" title="AutoApplyTags">AutoApplyTags</a>" : <i>Boolean</i>,
    "<a href="#shouldresumestateful" title="ShouldResumeStateful">ShouldResumeStateful</a>" : <i>Boolean</i>,
    "<a href="#shouldroll" title="ShouldRoll">ShouldRoll</a>" : <i>Boolean</i>,
    "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ &lt;a href=&#34;updatepolicy-rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoapplytags" title="AutoApplyTags">AutoApplyTags</a>: <i>Boolean</i>
<a href="#shouldresumestateful" title="ShouldResumeStateful">ShouldResumeStateful</a>: <i>Boolean</i>
<a href="#shouldroll" title="ShouldRoll">ShouldRoll</a>: <i>Boolean</i>
<a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - &lt;a href=&#34;updatepolicy-rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;</i>
</pre>

## Properties

#### AutoApplyTags

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldResumeStateful

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldRoll

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollConfig

_Required_: No
_Type_: List of &lt;a href=&#34;updatepolicy-rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

