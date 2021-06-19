# TF::Rancher2::Cluster MasterAuthorizedNetworksConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>" : <i>[ <a href="cidrblocksdefinition.md">CidrBlocksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>: <i>
      - <a href="cidrblocksdefinition.md">CidrBlocksDefinition</a></i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlocks

_Required_: No

_Type_: List of <a href="cidrblocksdefinition.md">CidrBlocksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

