# TF::Thunder::RouterOspf NetworkListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#networkipv4" title="NetworkIpv4">NetworkIpv4</a>" : <i>String</i>,
    "<a href="#networkipv4cidr" title="NetworkIpv4Cidr">NetworkIpv4Cidr</a>" : <i>String</i>,
    "<a href="#networkipv4mask" title="NetworkIpv4Mask">NetworkIpv4Mask</a>" : <i>String</i>,
    "<a href="#networkarea" title="NetworkArea">NetworkArea</a>" : <i>[ <a href="networkareadefinition.md">NetworkAreaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#networkipv4" title="NetworkIpv4">NetworkIpv4</a>: <i>String</i>
<a href="#networkipv4cidr" title="NetworkIpv4Cidr">NetworkIpv4Cidr</a>: <i>String</i>
<a href="#networkipv4mask" title="NetworkIpv4Mask">NetworkIpv4Mask</a>: <i>String</i>
<a href="#networkarea" title="NetworkArea">NetworkArea</a>: <i>
      - <a href="networkareadefinition.md">NetworkAreaDefinition</a></i>
</pre>

## Properties

#### NetworkIpv4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIpv4Cidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIpv4Mask

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkArea

_Required_: No

_Type_: List of <a href="networkareadefinition.md">NetworkAreaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

