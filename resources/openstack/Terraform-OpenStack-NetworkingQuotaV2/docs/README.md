# Terraform::OpenStack::NetworkingQuotaV2

Manages a V2 networking quota resource within OpenStack.

~> **Note:** This usually requires admin privileges.

~> **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
    in case of delete call.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingQuotaV2",
    "Properties" : {
        "<a href="#floatingip" title="Floatingip">Floatingip</a>" : <i>Double</i>,
        "<a href="#network" title="Network">Network</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#rbacpolicy" title="RbacPolicy">RbacPolicy</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#router" title="Router">Router</a>" : <i>Double</i>,
        "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>Double</i>,
        "<a href="#securitygrouprule" title="SecurityGroupRule">SecurityGroupRule</a>" : <i>Double</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>Double</i>,
        "<a href="#subnetpool" title="Subnetpool">Subnetpool</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingQuotaV2
Properties:
    <a href="#floatingip" title="Floatingip">Floatingip</a>: <i>Double</i>
    <a href="#network" title="Network">Network</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#rbacpolicy" title="RbacPolicy">RbacPolicy</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#router" title="Router">Router</a>: <i>Double</i>
    <a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>Double</i>
    <a href="#securitygrouprule" title="SecurityGroupRule">SecurityGroupRule</a>: <i>Double</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>Double</i>
    <a href="#subnetpool" title="Subnetpool">Subnetpool</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Floatingip

Quota value for floating IPs. Changing this updates the
existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

Quota value for networks. Changing this updates the
existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Quota value for ports. Changing this updates the
existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

ID of the project to manage quota. Changing this
creates new quota.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RbacPolicy

Quota value for RBAC policies.
Changing this updates the existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to create the quota. If
omitted, the `region` argument of the provider is used. Changing this
creates new quota.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

Quota value for routers. Changing this updates the
existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

Quota value for security groups. Changing
this updates the existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupRule

Quota value for security group rules.
Changing this updates the existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Quota value for subnets. Changing
this updates the existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetpool

Quota value for subnetpools.
Changing this updates the existing quota.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

