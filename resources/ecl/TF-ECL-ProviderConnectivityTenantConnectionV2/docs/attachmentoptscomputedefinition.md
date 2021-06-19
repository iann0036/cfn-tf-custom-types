# TF::ECL::ProviderConnectivityTenantConnectionV2 AttachmentOptsComputeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>" : <i>[ <a href="allowedaddresspairsdefinition.md">AllowedAddressPairsDefinition</a>, ... ]</i>,
    "<a href="#fixedips" title="FixedIps">FixedIps</a>" : <i>[ <a href="fixedipsdefinition.md">FixedIpsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>: <i>
      - <a href="allowedaddresspairsdefinition.md">AllowedAddressPairsDefinition</a></i>
<a href="#fixedips" title="FixedIps">FixedIps</a>: <i>
      - <a href="fixedipsdefinition.md">FixedIpsDefinition</a></i>
</pre>

## Properties

#### AllowedAddressPairs

_Required_: No

_Type_: List of <a href="allowedaddresspairsdefinition.md">AllowedAddressPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedIps

_Required_: No

_Type_: List of <a href="fixedipsdefinition.md">FixedIpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

