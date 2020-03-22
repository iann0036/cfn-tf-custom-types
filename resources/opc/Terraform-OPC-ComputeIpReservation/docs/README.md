# Terraform::OPC::ComputeIpReservation

The ``opc_compute_ip_reservation`` resource creates and manages an IP reservation in an Oracle Cloud Infrastructure Compute Classic identity domain for the Shared Network.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeIpReservation",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentpool" title="ParentPool">ParentPool</a>" : <i>String</i>,
        "<a href="#permanent" title="Permanent">Permanent</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeIpReservation
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentpool" title="ParentPool">ParentPool</a>: <i>String</i>
    <a href="#permanent" title="Permanent">Permanent</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### Name

Name of the IP Reservation. Will be generated if unspecified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentPool

The pool from which to allocate the IP address. Defaults to `/oracle/public/ippool`, and is currently the only acceptable input.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permanent

Whether the IP address remains reserved even when it is no longer associated with an instance
(if true), or may be returned to the pool and replaced with a different IP address when an instance is restarted, or
deleted and recreated (if false).

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of tags that may be applied to the IP reservation.

_Required_: No

_Type_: List of String

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

#### Ip

Returns the <code>Ip</code> value.

#### Used

Returns the <code>Used</code> value.

