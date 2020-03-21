# Terraform::Cloudflare::LoadBalancer

Provides a Cloudflare Load Balancer resource. This sits in front of a number of defined pools of origins and provides various options for geographically-aware load balancing. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::LoadBalancer",
    "Properties" : {
        "<a href="#defaultpoolids" title="DefaultPoolIds">DefaultPoolIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#fallbackpoolid" title="FallbackPoolId">FallbackPoolId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#proxied" title="Proxied">Proxied</a>" : <i>Boolean</i>,
        "<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>" : <i>String</i>,
        "<a href="#steeringpolicy" title="SteeringPolicy">SteeringPolicy</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#poppools" title="PopPools">PopPools</a>" : <i>[ <a href="poppools.md">PopPools</a>, ... ]</i>,
        "<a href="#regionpools" title="RegionPools">RegionPools</a>" : <i>[ <a href="regionpools.md">RegionPools</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::LoadBalancer
Properties:
    <a href="#defaultpoolids" title="DefaultPoolIds">DefaultPoolIds</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#fallbackpoolid" title="FallbackPoolId">FallbackPoolId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#proxied" title="Proxied">Proxied</a>: <i>Boolean</i>
    <a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>: <i>String</i>
    <a href="#steeringpolicy" title="SteeringPolicy">SteeringPolicy</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#poppools" title="PopPools">PopPools</a>: <i>
      - <a href="poppools.md">PopPools</a></i>
    <a href="#regionpools" title="RegionPools">RegionPools</a>: <i>
      - <a href="regionpools.md">RegionPools</a></i>
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

The DNS name (FQDN, including the zone) to associate with the load balancer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxied

Whether the hostname gets Cloudflare's origin protection. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinity

Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: `""`, `"none"`, `"cookie"`, and `"ip_cookie"`.  Default is `""`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SteeringPolicy

Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: `"off"`, `"geo"`, `"dynamic_latency"`, `"random"` or `""`. Default is `""`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Time to live (TTL) of this load balancer's DNS `name`. Conflicts with `proxied` - this cannot be set for proxied load balancers. Default is `30`.

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

_Type_: List of <a href="poppools.md">PopPools</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionPools

_Required_: No

_Type_: List of <a href="regionpools.md">RegionPools</a>

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

#### ModifiedOn

Returns the <code>ModifiedOn</code> value.

