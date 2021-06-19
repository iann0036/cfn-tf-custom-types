# TF::FortiOS::RouterMulticast6 PimSmGlobalDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#registerratelimit" title="RegisterRateLimit">RegisterRateLimit</a>" : <i>Double</i>,
    "<a href="#rpaddress" title="RpAddress">RpAddress</a>" : <i>[ <a href="rpaddressdefinition.md">RpAddressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#registerratelimit" title="RegisterRateLimit">RegisterRateLimit</a>: <i>Double</i>
<a href="#rpaddress" title="RpAddress">RpAddress</a>: <i>
      - <a href="rpaddressdefinition.md">RpAddressDefinition</a></i>
</pre>

## Properties

#### RegisterRateLimit

Limit of packets/sec per source registered through this RP (0 means unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpAddress

_Required_: No

_Type_: List of <a href="rpaddressdefinition.md">RpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

