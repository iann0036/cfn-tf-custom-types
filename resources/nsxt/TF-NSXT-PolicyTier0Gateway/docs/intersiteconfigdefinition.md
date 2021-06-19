# TF::NSXT::PolicyTier0Gateway IntersiteConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fallbacksitepaths" title="FallbackSitePaths">FallbackSitePaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#primarysitepath" title="PrimarySitePath">PrimarySitePath</a>" : <i>String</i>,
    "<a href="#transitsubnet" title="TransitSubnet">TransitSubnet</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fallbacksitepaths" title="FallbackSitePaths">FallbackSitePaths</a>: <i>
      - String</i>
<a href="#primarysitepath" title="PrimarySitePath">PrimarySitePath</a>: <i>String</i>
<a href="#transitsubnet" title="TransitSubnet">TransitSubnet</a>: <i>String</i>
</pre>

## Properties

#### FallbackSitePaths

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimarySitePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

