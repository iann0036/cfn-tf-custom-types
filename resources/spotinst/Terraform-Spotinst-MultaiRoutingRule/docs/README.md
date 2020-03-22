# Terraform::Spotinst::MultaiRoutingRule

Provides a Spotinst Multai Routing Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::MultaiRoutingRule",
    "Properties" : {
        "<a href="#balancerid" title="BalancerId">BalancerId</a>" : <i>String</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#middlewareids" title="MiddlewareIds">MiddlewareIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#route" title="Route">Route</a>" : <i>String</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>String</i>,
        "<a href="#targetsetids" title="TargetSetIds">TargetSetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::MultaiRoutingRule
Properties:
    <a href="#balancerid" title="BalancerId">BalancerId</a>: <i>String</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#middlewareids" title="MiddlewareIds">MiddlewareIds</a>: <i>
      - String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#route" title="Route">Route</a>: <i>String</i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>String</i>
    <a href="#targetsetids" title="TargetSetIds">TargetSetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### BalancerId

The ID of the balancer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

The ID of the listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiddlewareIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

Route defines a simple language for matching HTTP requests and route the traffic accordingly. Route provides series of matchers that follow the syntax: Path matcher: — Path("/foo/bar") // trie-based PathRegexp(“/foo/.*”) // regexp-based Method matcher: — Method(“GET”) // trie-based MethodRegexp(“POST|PUT”) // regexp based Header matcher: — Header(“Content-Type”, “application/json”) // trie-based HeaderRegexp(“Content-Type”, “application/.*”) // regexp based Matchers can be combined using && operator: — Method(“POST”) && Path("/v1").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

Balancing strategy. Valid values: `ROUNDROBIN`, `RANDOM`, `LEASTCONN`, `IPHASH`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSetIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

