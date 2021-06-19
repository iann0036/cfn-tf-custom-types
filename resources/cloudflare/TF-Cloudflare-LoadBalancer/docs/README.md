# TF::Cloudflare::LoadBalancer

Provides a Cloudflare Load Balancer resource. This sits in front of a number of defined pools of origins and provides various options for geographically-aware load balancing. Note that the load balancing feature must be enabled in your Cloudflare account before you can use this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::LoadBalancer",
    "Properties" : {
        "<a href="#defaultpoolids" title="DefaultPoolIds">DefaultPoolIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#fallbackpoolid" title="FallbackPoolId">FallbackPoolId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#proxied" title="Proxied">Proxied</a>" : <i>Boolean</i>,
        "<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>" : <i>String</i>,
        "<a href="#sessionaffinityattributes" title="SessionAffinityAttributes">SessionAffinityAttributes</a>" : <i>[ <a href="sessionaffinityattributesdefinition.md">SessionAffinityAttributesDefinition</a>, ... ]</i>,
        "<a href="#sessionaffinityttl" title="SessionAffinityTtl">SessionAffinityTtl</a>" : <i>Double</i>,
        "<a href="#steeringpolicy" title="SteeringPolicy">SteeringPolicy</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#poppools" title="PopPools">PopPools</a>" : <i>[ <a href="poppoolsdefinition.md">PopPoolsDefinition</a>, ... ]</i>,
        "<a href="#regionpools" title="RegionPools">RegionPools</a>" : <i>[ <a href="regionpoolsdefinition.md">RegionPoolsDefinition</a>, ... ]</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rulesdefinition.md">RulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::LoadBalancer
Properties:
    <a href="#defaultpoolids" title="DefaultPoolIds">DefaultPoolIds</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#fallbackpoolid" title="FallbackPoolId">FallbackPoolId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#proxied" title="Proxied">Proxied</a>: <i>Boolean</i>
    <a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>: <i>String</i>
    <a href="#sessionaffinityattributes" title="SessionAffinityAttributes">SessionAffinityAttributes</a>: <i>
      - <a href="sessionaffinityattributesdefinition.md">SessionAffinityAttributesDefinition</a></i>
    <a href="#sessionaffinityttl" title="SessionAffinityTtl">SessionAffinityTtl</a>: <i>Double</i>
    <a href="#steeringpolicy" title="SteeringPolicy">SteeringPolicy</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#poppools" title="PopPools">PopPools</a>: <i>
      - <a href="poppoolsdefinition.md">PopPoolsDefinition</a></i>
    <a href="#regionpools" title="RegionPools">RegionPools</a>: <i>
      - <a href="regionpoolsdefinition.md">RegionPoolsDefinition</a></i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rulesdefinition.md">RulesDefinition</a></i>
</pre>

## Properties

#### DefaultPoolIds

A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Free text description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable or disable the load balancer. Defaults to `true` (enabled).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackPoolId

The pool ID to use when all other pools are detected as unhealthy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Human readable name for this rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxied

Whether the hostname gets Cloudflare's origin protection. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinity

See field above.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityAttributes

See field above.

_Required_: No

_Type_: List of <a href="sessionaffinityattributesdefinition.md">SessionAffinityAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinityTtl

See field above.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SteeringPolicy

See field above.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

See field above.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The zone ID to add the load balancer to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PopPools

_Required_: No

_Type_: List of <a href="poppoolsdefinition.md">PopPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionPools

_Required_: No

_Type_: List of <a href="regionpoolsdefinition.md">RegionPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rulesdefinition.md">RulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedOn

Returns the <code>CreatedOn</code> value.

#### Id

Returns the <code>Id</code> value.

#### ModifiedOn

Returns the <code>ModifiedOn</code> value.

