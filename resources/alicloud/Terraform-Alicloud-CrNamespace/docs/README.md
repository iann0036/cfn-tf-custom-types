# Terraform::Alicloud::CrNamespace

This resource will help you to manager Container Registry namespaces.

-> **NOTE:** Available in v1.34.0+.

-> **NOTE:** You need to set your registry password in Container Registry console before use this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CrNamespace",
    "Properties" : {
        "<a href="#autocreate" title="AutoCreate">AutoCreate</a>" : <i>Boolean</i>,
        "<a href="#defaultvisibility" title="DefaultVisibility">DefaultVisibility</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CrNamespace
Properties:
    <a href="#autocreate" title="AutoCreate">AutoCreate</a>: <i>Boolean</i>
    <a href="#defaultvisibility" title="DefaultVisibility">DefaultVisibility</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### AutoCreate

Boolean, when it set to true, repositories are automatically created when pushing new images. If it set to false, you create repository for images before pushing.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultVisibility

`PUBLIC` or `PRIVATE`, default repository visibility in this namespace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Container Registry namespace.

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

