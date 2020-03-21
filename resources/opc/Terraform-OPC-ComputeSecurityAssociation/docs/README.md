# Terraform::OPC::ComputeSecurityAssociation

The ``opc_compute_security_association`` resource creates and manages an association between an instance and a security
list in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeSecurityAssociation",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#seclist" title="Seclist">Seclist</a>" : <i>String</i>,
        "<a href="#vcable" title="Vcable">Vcable</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeSecurityAssociation
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#seclist" title="Seclist">Seclist</a>: <i>String</i>
    <a href="#vcable" title="Vcable">Vcable</a>: <i>String</i>
</pre>

## Properties

#### Name

The Name for the Security Association. If not specified, one is created automatically. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Seclist

The name of the security list to associate the instance to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcable

The `vcable` of the instance to associate to the security list.

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

