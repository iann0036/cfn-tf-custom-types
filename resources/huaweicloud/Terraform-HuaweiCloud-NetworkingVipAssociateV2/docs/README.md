# Terraform::HuaweiCloud::NetworkingVipAssociateV2

Manages a V2 vip associate resource within HuaweiCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::NetworkingVipAssociateV2",
    "Properties" : {
        "<a href="#portids" title="PortIds">PortIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#vipid" title="VipId">VipId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::NetworkingVipAssociateV2
Properties:
    <a href="#portids" title="PortIds">PortIds</a>: <i>
      - String</i>
    <a href="#vipid" title="VipId">VipId</a>: <i>String</i>
</pre>

## Properties

#### PortIds

An array of one or more IDs of the ports to attach the vip to.
Changing this creates a new vip associate.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipId

The ID of vip to attach the port to.
Changing this creates a new vip associate.

_Required_: Yes

_Type_: String

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

#### VipIpAddress

Returns the <code>VipIpAddress</code> value.

#### VipSubnetId

Returns the <code>VipSubnetId</code> value.

