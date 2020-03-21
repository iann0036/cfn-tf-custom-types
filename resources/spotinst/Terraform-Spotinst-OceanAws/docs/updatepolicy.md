# Terraform::Spotinst::OceanAws UpdatePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#shouldroll" title="ShouldRoll">ShouldRoll</a>" : <i>Boolean</i>,
    "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ &lt;a href=&#34;updatepolicy-rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#shouldroll" title="ShouldRoll">ShouldRoll</a>: <i>Boolean</i>
<a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - &lt;a href=&#34;updatepolicy-rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;</i>
</pre>

## Properties

#### ShouldRoll

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollConfig

_Required_: No
_Type_: List of &lt;a href=&#34;updatepolicy-rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

