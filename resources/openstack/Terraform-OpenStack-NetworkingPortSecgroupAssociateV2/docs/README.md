# Terraform::OpenStack::NetworkingPortSecgroupAssociateV2

Manages a V2 port's security groups within OpenStack. Useful, when the port was
created not by Terraform (e.g. Manila or LBaaS). It should not be used, when the
port was created directly within Terraform.

When the resource is deleted, Terraform doesn't delete the port, but unsets the
list of user defined security group IDs.  However, if `enforce` is set to `true`
and the resource is deleted, Terraform will remove all assigned security group
IDs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingPortSecgroupAssociateV2",
    "Properties" : {
        "<a href="#enforce" title="Enforce">Enforce</a>" : <i>Boolean</i>,
        "<a href="#portid" title="PortId">PortId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingPortSecgroupAssociateV2
Properties:
    <a href="#enforce" title="Enforce">Enforce</a>: <i>Boolean</i>
    <a href="#portid" title="PortId">PortId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Enforce

Whether to replace or append the list of security
groups, specified in the `security_group_ids`. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortId

An UUID of the port to apply security groups to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 networking client.
A networking client is needed to manage a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

A list of security group IDs to apply to
the port. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllSecurityGroupIds

Returns the <code>AllSecurityGroupIds</code> value.

#### Id

Returns the <code>Id</code> value.

