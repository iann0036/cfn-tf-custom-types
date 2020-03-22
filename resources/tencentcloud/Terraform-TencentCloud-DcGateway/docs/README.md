# Terraform::TencentCloud::DcGateway

Provides a resource to creating direct connect gateway instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DcGateway",
    "Properties" : {
        "<a href="#gatewaytype" title="GatewayType">GatewayType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkinstanceid" title="NetworkInstanceId">NetworkInstanceId</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DcGateway
Properties:
    <a href="#gatewaytype" title="GatewayType">GatewayType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkinstanceid" title="NetworkInstanceId">NetworkInstanceId</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
</pre>

## Properties

#### GatewayType

Type of the gateway, the available value include 'NORMAL' and 'NAT'. Default is 'NORMAL'. NOTES: CCN only supports 'NORMAL' and a vpc can create two DCGs, the one is NAT type and the other is non-NAT type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the DCG.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInstanceId

If the 'network_type' value is 'VPC', the available value is VPC ID. But when the 'network_type' value is 'CCN', the available value is CCN instance ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Type of associated network, the available value include 'VPC' and 'CCN'.

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

#### CnnRouteType

Returns the <code>CnnRouteType</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### EnableBgp

Returns the <code>EnableBgp</code> value.

#### Id

Returns the <code>Id</code> value.

