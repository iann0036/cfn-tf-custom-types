# TF::AVI::Ipamdnsproviderprofile CustomProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customipamdnsprofileref" title="CustomIpamDnsProfileRef">CustomIpamDnsProfileRef</a>" : <i>String</i>,
    "<a href="#usabledomains" title="UsableDomains">UsableDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#dynamicparams" title="DynamicParams">DynamicParams</a>" : <i>[ <a href="dynamicparamsdefinition.md">DynamicParamsDefinition</a>, ... ]</i>,
    "<a href="#usablesubnets" title="UsableSubnets">UsableSubnets</a>" : <i>[ <a href="usablesubnetsdefinition.md">UsableSubnetsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customipamdnsprofileref" title="CustomIpamDnsProfileRef">CustomIpamDnsProfileRef</a>: <i>String</i>
<a href="#usabledomains" title="UsableDomains">UsableDomains</a>: <i>
      - String</i>
<a href="#dynamicparams" title="DynamicParams">DynamicParams</a>: <i>
      - <a href="dynamicparamsdefinition.md">DynamicParamsDefinition</a></i>
<a href="#usablesubnets" title="UsableSubnets">UsableSubnets</a>: <i>
      - <a href="usablesubnetsdefinition.md">UsableSubnetsDefinition</a></i>
</pre>

## Properties

#### CustomIpamDnsProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicParams

_Required_: No

_Type_: List of <a href="dynamicparamsdefinition.md">DynamicParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableSubnets

_Required_: No

_Type_: List of <a href="usablesubnetsdefinition.md">UsableSubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

