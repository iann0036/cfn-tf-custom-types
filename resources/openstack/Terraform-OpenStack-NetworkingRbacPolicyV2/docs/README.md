# Terraform::OpenStack::NetworkingRbacPolicyV2

The RBAC policy resource contains functionality for working with Neutron RBAC
Policies. Role-Based Access Control (RBAC) policy framework enables both
operators and users to grant access to resources for specific projects.

Sharing an object with a specific project is accomplished by creating a
policy entry that permits the target project the `access_as_shared` action
on that object.

To make a network available as an external network for specific projects
rather than all projects, use the `access_as_external` action.
If a network is marked as external during creation, it now implicitly creates
a wildcard RBAC policy granting everyone access to preserve previous behavior
before this feature was added.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingRbacPolicyV2",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#objectid" title="ObjectId">ObjectId</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#targettenant" title="TargetTenant">TargetTenant</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingRbacPolicyV2
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#objectid" title="ObjectId">ObjectId</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#targettenant" title="TargetTenant">TargetTenant</a>: <i>String</i>
</pre>

## Properties

#### Action

Action for the RBAC policy. Can either be
`access_as_external` or `access_as_shared`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectId

The ID of the `object_type` resource. An
`object_type` of `network` returns a network ID and an `object_type` of
`qos_policy` returns a QoS ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

The type of the object that the RBAC policy
affects. Can either be `qos-policy` or `network`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTenant

The ID of the tenant to which the RBAC policy
will be enforced.

_Required_: Yes

_Type_: String

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

#### ProjectId

Returns the <code>ProjectId</code> value.

