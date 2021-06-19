# TF::Volterra::AzureVnetSite IngressGwDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#azurecertifiedhw" title="AzureCertifiedHw">AzureCertifiedHw</a>" : <i>String</i>,
    "<a href="#aznodes" title="AzNodes">AzNodes</a>" : <i>[ <a href="aznodesdefinition.md">AzNodesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#azurecertifiedhw" title="AzureCertifiedHw">AzureCertifiedHw</a>: <i>String</i>
<a href="#aznodes" title="AzNodes">AzNodes</a>: <i>
      - <a href="aznodesdefinition.md">AzNodesDefinition</a></i>
</pre>

## Properties

#### AzureCertifiedHw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzNodes

_Required_: No

_Type_: List of <a href="aznodesdefinition.md">AzNodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

