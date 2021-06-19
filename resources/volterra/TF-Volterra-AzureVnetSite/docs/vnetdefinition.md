# TF::Volterra::AzureVnetSite VnetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#existingvnet" title="ExistingVnet">ExistingVnet</a>" : <i>[ <a href="existingvnetdefinition.md">ExistingVnetDefinition</a>, ... ]</i>,
    "<a href="#newvnet" title="NewVnet">NewVnet</a>" : <i>[ <a href="newvnetdefinition.md">NewVnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#existingvnet" title="ExistingVnet">ExistingVnet</a>: <i>
      - <a href="existingvnetdefinition.md">ExistingVnetDefinition</a></i>
<a href="#newvnet" title="NewVnet">NewVnet</a>: <i>
      - <a href="newvnetdefinition.md">NewVnetDefinition</a></i>
</pre>

## Properties

#### ExistingVnet

_Required_: No

_Type_: List of <a href="existingvnetdefinition.md">ExistingVnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewVnet

_Required_: No

_Type_: List of <a href="newvnetdefinition.md">NewVnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

