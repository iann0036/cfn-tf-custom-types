# Terraform::Spotinst::ElastigroupAzure UpdatePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#shouldroll" title="ShouldRoll">ShouldRoll</a>" : <i>Boolean</i>,
    "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ <a href="updatepolicy-rollconfig.md">RollConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#shouldroll" title="ShouldRoll">ShouldRoll</a>: <i>Boolean</i>
<a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - <a href="updatepolicy-rollconfig.md">RollConfig</a></i>
</pre>

## Properties

#### ShouldRoll

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollConfig

_Required_: No
_Type_: List of <a href="updatepolicy-rollconfig.md">RollConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

