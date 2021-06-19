# TF::Cloudflare::LoadBalancer OverridesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultpools" title="DefaultPools">DefaultPools</a>" : <i>[ String, ... ]</i>,
    "<a href="#fallbackpool" title="FallbackPool">FallbackPool</a>" : <i>String</i>,
    "<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>" : <i>String</i>,
    "<a href="#sessionaffinityattributes" title="SessionAffinityAttributes">SessionAffinityAttributes</a>" : <i>[ <a href="sessionaffinityattributesdefinition.md">SessionAffinityAttributesDefinition</a>, ... ]</i>,
    "<a href="#sessionaffinityttl" title="SessionAffinityTtl">SessionAffinityTtl</a>" : <i>Double</i>,
    "<a href="#steeringpolicy" title="SteeringPolicy">SteeringPolicy</a>" : <i>String</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
    "<a href="#poppools" title="PopPools">PopPools</a>" : <i>[ <a href="poppoolsdefinition.md">PopPoolsDefinition</a>, ... ]</i>,
    "<a href="#regionpools" title="RegionPools">RegionPools</a>" : <i>[ <a href="regionpoolsdefinition.md">RegionPoolsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultpools" title="DefaultPools">DefaultPools</a>: <i>
      - String</i>
<a href="#fallbackpool" title="FallbackPool">FallbackPool</a>: <i>String</i>
<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>: <i>String</i>
<a href="#sessionaffinityattributes" title="SessionAffinityAttributes">SessionAffinityAttributes</a>: <i>
      - <a href="sessionaffinityattributesdefinition.md">SessionAffinityAttributesDefinition</a></i>
<a href="#sessionaffinityttl" title="SessionAffinityTtl">SessionAffinityTtl</a>: <i>Double</i>
<a href="#steeringpolicy" title="SteeringPolicy">SteeringPolicy</a>: <i>String</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
<a href="#poppools" title="PopPools">PopPools</a>: <i>
      - <a href="poppoolsdefinition.md">PopPoolsDefinition</a></i>
<a href="#regionpools" title="RegionPools">RegionPools</a>: <i>
      - <a href="regionpoolsdefinition.md">RegionPoolsDefinition</a></i>
</pre>

## Properties

#### DefaultPools

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackPool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityAttributes

_Required_: No

_Type_: List of <a href="sessionaffinityattributesdefinition.md">SessionAffinityAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SteeringPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PopPools

_Required_: No

_Type_: List of <a href="poppoolsdefinition.md">PopPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionPools

_Required_: No

_Type_: List of <a href="regionpoolsdefinition.md">RegionPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

