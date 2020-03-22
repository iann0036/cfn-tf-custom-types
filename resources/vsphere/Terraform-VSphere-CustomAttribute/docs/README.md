# Terraform::VSphere::CustomAttribute

The `vsphere_custom_attribute` resource can be used to create and manage custom
attributes, which allow users to associate user-specific meta-information with 
vSphere managed objects. Custom attribute values must be strings and are stored 
on the vCenter Server and not the managed object.

For more information about custom attributes, click [here][ext-custom-attributes].

[ext-custom-attributes]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-73606C4C-763C-4E27-A1DA-032E4C46219D.html

~> **NOTE:** Custom attributes are unsupported on direct ESXi connections 
and require vCenter.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::CustomAttribute",
    "Properties" : {
        "<a href="#managedobjecttype" title="ManagedObjectType">ManagedObjectType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::CustomAttribute
Properties:
    <a href="#managedobjecttype" title="ManagedObjectType">ManagedObjectType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ManagedObjectType

The object type that this attribute may be
applied to. If not set, the custom attribute may be applied to any object
type. For a full list, click [here](#managed-object-types). Forces a new
resource if changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the custom attribute.

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

#### Id

Returns the <code>Id</code> value.

