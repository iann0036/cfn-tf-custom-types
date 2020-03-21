# Terraform::OpenStack::ComputeFlavorV2

CloudFormation equivalent of openstack_compute_flavor_v2

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

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ephemeral

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraSpecs

_Required_: No

_Type_: List of <a href="extraspecs.md">ExtraSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPublic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ram

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RxTxFactor

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Swap

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcpus

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

