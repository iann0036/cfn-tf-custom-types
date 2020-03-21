# Terraform::Hedvig::Mount

A Hedvig Mount mounts a vdisk resource with a particular controller. It can then be used to connect ACL access resources to the vdisk as well.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Hedvig::Mount",
    "Properties" : {
        "<a href="#controller" title="Controller">Controller</a>" : <i>String</i>,
        "<a href="#vdisk" title="Vdisk">Vdisk</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Hedvig::Mount
Properties:
    <a href="#controller" title="Controller">Controller</a>: <i>String</i>
    <a href="#vdisk" title="Vdisk">Vdisk</a>: <i>String</i>
</pre>

## Properties

#### Controller

The fully qualified domain name for the controller that the Mount is to attach to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdisk

The name of the vdisk the Mount is on.

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

