# Terraform::OCI::LoadBalancerPathRouteSet

This resource provides the Path Route Set resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a path route set to a load balancer. For more information, see
[Managing Request Routing](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::LoadBalancerPathRouteSet",
    "Properties" : {
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pathroutes" title="PathRoutes">PathRoutes</a>" : <i>[ <a href="pathroutes.md">PathRoutes</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#pathmatchtype" title="PathMatchType">PathMatchType</a>" : <i>[ <a href="pathmatchtype.md">PathMatchType</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::LoadBalancerPathRouteSet
Properties:
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pathroutes" title="PathRoutes">PathRoutes</a>: <i>
      - <a href="pathroutes.md">PathRoutes</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#pathmatchtype" title="PathMatchType">PathMatchType</a>: <i>
      - <a href="pathmatchtype.md">PathMatchType</a></i>
</pre>

## Properties

#### LoadBalancerId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer to add the path route set to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_path_route_set`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRoutes

_Required_: No

_Type_: List of <a href="pathroutes.md">PathRoutes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathMatchType

_Required_: No

_Type_: List of <a href="pathmatchtype.md">PathMatchType</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### State

Returns the <code>State</code> value.

