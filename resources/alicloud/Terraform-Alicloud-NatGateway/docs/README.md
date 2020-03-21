# Terraform::Alicloud::NatGateway

Provides a resource to create a VPC NAT Gateway.


-> **NOTE:** Resource bandwidth packages will not be supported since 00:00 on November 4, 2017, and public IP can be replaced be elastic IPs.
If a Nat Gateway has already bought some bandwidth packages, it can not bind elastic IP and you have to submit the [work order](https://selfservice.console.aliyun.com/ticket/createIndex) to solve.
If you want to add public IP, you can use resource 'alicloud_eip_association' to bind several elastic IPs for one Nat Gateway.

-> **NOTE:** From version 1.7.1, this resource has deprecated bandwidth packages.
But, in order to manage stock bandwidth packages, version 1.13.0 re-support configuring 'bandwidth_packages'.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::NatGateway",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>String</i>,
        "<a href="#specification" title="Specification">Specification</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#bandwidthpackages" title="BandwidthPackages">BandwidthPackages</a>" : <i>[ <a href="bandwidthpackages.md">BandwidthPackages</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::NatGateway
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#spec" title="Spec">Spec</a>: <i>String</i>
    <a href="#specification" title="Specification">Specification</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#bandwidthpackages" title="BandwidthPackages">BandwidthPackages</a>: <i>
      - <a href="bandwidthpackages.md">BandwidthPackages</a></i>
</pre>

## Properties

#### Description

Description of the nat gateway, This description can have a string of 2 to 256 characters, It cannot begin with http:// or https://. Defaults to null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

The billing method of the nat gateway. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the nat gateway. The value can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin or end with a hyphen, and must not begin with http:// or https://. Defaults to null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

It has been deprecated from provider version 1.7.1, and new field 'specification' can replace it.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Specification

The specification of the nat gateway. Valid values are `Small`, `Middle` and `Large`. Default to `Small`. Details refer to [Nat Gateway Specification](https://www.alibabacloud.com/help/doc-detail/42757.htm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPC ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthPackages

_Required_: No

_Type_: List of <a href="bandwidthpackages.md">BandwidthPackages</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BandwidthPackageIds

Returns the <code>BandwidthPackageIds</code> value.

#### ForwardTableIds

Returns the <code>ForwardTableIds</code> value.

#### SnatTableIds

Returns the <code>SnatTableIds</code> value.

