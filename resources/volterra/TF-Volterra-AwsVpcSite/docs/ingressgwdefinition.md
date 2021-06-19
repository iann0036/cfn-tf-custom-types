# TF::Volterra::AwsVpcSite IngressGwDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awscertifiedhw" title="AwsCertifiedHw">AwsCertifiedHw</a>" : <i>String</i>,
    "<a href="#allowedvipport" title="AllowedVipPort">AllowedVipPort</a>" : <i>[ <a href="allowedvipportdefinition.md">AllowedVipPortDefinition</a>, ... ]</i>,
    "<a href="#aznodes" title="AzNodes">AzNodes</a>" : <i>[ <a href="aznodesdefinition.md">AzNodesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awscertifiedhw" title="AwsCertifiedHw">AwsCertifiedHw</a>: <i>String</i>
<a href="#allowedvipport" title="AllowedVipPort">AllowedVipPort</a>: <i>
      - <a href="allowedvipportdefinition.md">AllowedVipPortDefinition</a></i>
<a href="#aznodes" title="AzNodes">AzNodes</a>: <i>
      - <a href="aznodesdefinition.md">AzNodesDefinition</a></i>
</pre>

## Properties

#### AwsCertifiedHw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedVipPort

_Required_: No

_Type_: List of <a href="allowedvipportdefinition.md">AllowedVipPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzNodes

_Required_: No

_Type_: List of <a href="aznodesdefinition.md">AzNodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

