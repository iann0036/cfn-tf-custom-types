# TF::Volterra::HttpLoadbalancer RateLimitDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#noipallowedlist" title="NoIpAllowedList">NoIpAllowedList</a>" : <i>Boolean</i>,
    "<a href="#nopolicies" title="NoPolicies">NoPolicies</a>" : <i>Boolean</i>,
    "<a href="#customipallowedlist" title="CustomIpAllowedList">CustomIpAllowedList</a>" : <i>[ <a href="customipallowedlistdefinition.md">CustomIpAllowedListDefinition</a>, ... ]</i>,
    "<a href="#ipallowedlist" title="IpAllowedList">IpAllowedList</a>" : <i>[ <a href="ipallowedlistdefinition.md">IpAllowedListDefinition</a>, ... ]</i>,
    "<a href="#policies" title="Policies">Policies</a>" : <i>[ <a href="policiesdefinition.md">PoliciesDefinition</a>, ... ]</i>,
    "<a href="#ratelimiter" title="RateLimiter">RateLimiter</a>" : <i>[ <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#noipallowedlist" title="NoIpAllowedList">NoIpAllowedList</a>: <i>Boolean</i>
<a href="#nopolicies" title="NoPolicies">NoPolicies</a>: <i>Boolean</i>
<a href="#customipallowedlist" title="CustomIpAllowedList">CustomIpAllowedList</a>: <i>
      - <a href="customipallowedlistdefinition.md">CustomIpAllowedListDefinition</a></i>
<a href="#ipallowedlist" title="IpAllowedList">IpAllowedList</a>: <i>
      - <a href="ipallowedlistdefinition.md">IpAllowedListDefinition</a></i>
<a href="#policies" title="Policies">Policies</a>: <i>
      - <a href="policiesdefinition.md">PoliciesDefinition</a></i>
<a href="#ratelimiter" title="RateLimiter">RateLimiter</a>: <i>
      - <a href="ratelimiterdefinition.md">RateLimiterDefinition</a></i>
</pre>

## Properties

#### NoIpAllowedList

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoPolicies

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomIpAllowedList

_Required_: No

_Type_: List of <a href="customipallowedlistdefinition.md">CustomIpAllowedListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllowedList

_Required_: No

_Type_: List of <a href="ipallowedlistdefinition.md">IpAllowedListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of <a href="policiesdefinition.md">PoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiter

_Required_: No

_Type_: List of <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

