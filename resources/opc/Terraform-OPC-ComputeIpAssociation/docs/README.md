# Terraform::OPC::ComputeIpAssociation

The ``opc_compute_ip_association`` resource creates and manages an association between an IP address and an instance in
an Oracle Cloud Infrastructure Compute Classic identity domain, for the Shared Network.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeIpAssociation",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentpool" title="ParentPool">ParentPool</a>" : <i>String</i>,
        "<a href="#vcable" title="Vcable">Vcable</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeIpAssociation
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentpool" title="ParentPool">ParentPool</a>: <i>String</i>
    <a href="#vcable" title="Vcable">Vcable</a>: <i>String</i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentPool

The pool from which to take an IP address. To associate a specific reserved IP address, use
the prefix `ipreservation:` followed by the name of the IP reservation. To allocate an IP address from a pool, use the
prefix `ippool:`, e.g. `ippool:/oracle/public/ippool`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcable

The vcable of the instance to associate the IP address with.

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

