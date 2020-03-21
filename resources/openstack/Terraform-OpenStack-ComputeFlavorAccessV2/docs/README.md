# Terraform::OpenStack::ComputeFlavorAccessV2

Manages a project access for flavor V2 resource within OpenStack.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

---

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::ComputeFlavorAccessV2",
    "Properties" : {
        "<a href="#flavorid" title="FlavorId">FlavorId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::ComputeFlavorAccessV2
Properties:
    <a href="#flavorid" title="FlavorId">FlavorId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
</pre>

## Properties

#### FlavorId

The UUID of flavor to use. Changing this creates a new flavor access.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Compute client.
If omitted, the `region` argument of the provider is used.
Changing this creates a new flavor access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The UUID of tenant which is allowed to use the flavor.
Changing this creates a new flavor access.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

