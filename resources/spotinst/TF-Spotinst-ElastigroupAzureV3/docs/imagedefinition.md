# TF::Spotinst::ElastigroupAzureV3 ImageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#custom" title="Custom">Custom</a>" : <i>[ <a href="customdefinition.md">CustomDefinition</a>, ... ]</i>,
    "<a href="#marketplace" title="Marketplace">Marketplace</a>" : <i>[ <a href="marketplacedefinition.md">MarketplaceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#custom" title="Custom">Custom</a>: <i>
      - <a href="customdefinition.md">CustomDefinition</a></i>
<a href="#marketplace" title="Marketplace">Marketplace</a>: <i>
      - <a href="marketplacedefinition.md">MarketplaceDefinition</a></i>
</pre>

## Properties

#### Custom

_Required_: No

_Type_: List of <a href="customdefinition.md">CustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marketplace

_Required_: No

_Type_: List of <a href="marketplacedefinition.md">MarketplaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

