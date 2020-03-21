# Terraform::OpenStack::ComputeFlavorV2

Manages a V2 flavor resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::ComputeFlavorV2",
    "Properties" : {
        "<a href="#disk" title="Disk">Disk</a>" : <i>Double</i>,
        "<a href="#ephemeral" title="Ephemeral">Ephemeral</a>" : <i>Double</i>,
        "<a href="#extraspecs" title="ExtraSpecs">ExtraSpecs</a>" : <i>[ <a href="extraspecs.md">ExtraSpecs</a>, ... ]</i>,
        "<a href="#ispublic" title="IsPublic">IsPublic</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ram" title="Ram">Ram</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rxtxfactor" title="RxTxFactor">RxTxFactor</a>" : <i>Double</i>,
        "<a href="#swap" title="Swap">Swap</a>" : <i>Double</i>,
        "<a href="#vcpus" title="Vcpus">Vcpus</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::ComputeFlavorV2
Properties:
    <a href="#disk" title="Disk">Disk</a>: <i>Double</i>
    <a href="#ephemeral" title="Ephemeral">Ephemeral</a>: <i>Double</i>
    <a href="#extraspecs" title="ExtraSpecs">ExtraSpecs</a>: <i>
      - <a href="extraspecs.md">ExtraSpecs</a></i>
    <a href="#ispublic" title="IsPublic">IsPublic</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ram" title="Ram">Ram</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rxtxfactor" title="RxTxFactor">RxTxFactor</a>: <i>Double</i>
    <a href="#swap" title="Swap">Swap</a>: <i>Double</i>
    <a href="#vcpus" title="Vcpus">Vcpus</a>: <i>Double</i>
</pre>

## Properties

#### Disk

The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ephemeral

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraSpecs

Key/Value pairs of metadata for the flavor.

_Required_: No

_Type_: List of <a href="extraspecs.md">ExtraSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPublic

Whether the flavor is public. Changing this creates
a new flavor.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the flavor. Changing this creates a new
flavor.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ram

The amount of RAM to use, in megabytes. Changing this
creates a new flavor.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new flavor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RxTxFactor

RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Swap

The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcpus

The number of virtual CPUs to use. Changing this creates
a new flavor.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

