# Terraform::Panos::VirtualRouter

CloudFormation equivalent of panos_virtual_router

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::VirtualRouter",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#ebgpdist" title="EbgpDist">EbgpDist</a>" : <i>Double</i>,
        "<a href="#ibgpdist" title="IbgpDist">IbgpDist</a>" : <i>Double</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ospfextdist" title="OspfExtDist">OspfExtDist</a>" : <i>Double</i>,
        "<a href="#ospfintdist" title="OspfIntDist">OspfIntDist</a>" : <i>Double</i>,
        "<a href="#ospfv3extdist" title="Ospfv3ExtDist">Ospfv3ExtDist</a>" : <i>Double</i>,
        "<a href="#ospfv3intdist" title="Ospfv3IntDist">Ospfv3IntDist</a>" : <i>Double</i>,
        "<a href="#ripdist" title="RipDist">RipDist</a>" : <i>Double</i>,
        "<a href="#staticdist" title="StaticDist">StaticDist</a>" : <i>Double</i>,
        "<a href="#staticipv6dist" title="StaticIpv6Dist">StaticIpv6Dist</a>" : <i>Double</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::VirtualRouter
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#ebgpdist" title="EbgpDist">EbgpDist</a>: <i>Double</i>
    <a href="#ibgpdist" title="IbgpDist">IbgpDist</a>: <i>Double</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ospfextdist" title="OspfExtDist">OspfExtDist</a>: <i>Double</i>
    <a href="#ospfintdist" title="OspfIntDist">OspfIntDist</a>: <i>Double</i>
    <a href="#ospfv3extdist" title="Ospfv3ExtDist">Ospfv3ExtDist</a>: <i>Double</i>
    <a href="#ospfv3intdist" title="Ospfv3IntDist">Ospfv3IntDist</a>: <i>Double</i>
    <a href="#ripdist" title="RipDist">RipDist</a>: <i>Double</i>
    <a href="#staticdist" title="StaticDist">StaticDist</a>: <i>Double</i>
    <a href="#staticipv6dist" title="StaticIpv6Dist">StaticIpv6Dist</a>: <i>Double</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbgpDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IbgpDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfExtDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfIntDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospfv3ExtDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospfv3IntDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RipDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticDist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpv6Dist

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

_Required_: No

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

