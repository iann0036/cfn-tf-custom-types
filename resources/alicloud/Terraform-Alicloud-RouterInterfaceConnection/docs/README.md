# Terraform::Alicloud::RouterInterfaceConnection

CloudFormation equivalent of alicloud_router_interface_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::RouterInterfaceConnection",
    "Properties" : {
        "<a href="#interfaceid" title="InterfaceId">InterfaceId</a>" : <i>String</i>,
        "<a href="#oppositeinterfaceid" title="OppositeInterfaceId">OppositeInterfaceId</a>" : <i>String</i>,
        "<a href="#oppositeinterfaceownerid" title="OppositeInterfaceOwnerId">OppositeInterfaceOwnerId</a>" : <i>String</i>,
        "<a href="#oppositerouterid" title="OppositeRouterId">OppositeRouterId</a>" : <i>String</i>,
        "<a href="#oppositeroutertype" title="OppositeRouterType">OppositeRouterType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::RouterInterfaceConnection
Properties:
    <a href="#interfaceid" title="InterfaceId">InterfaceId</a>: <i>String</i>
    <a href="#oppositeinterfaceid" title="OppositeInterfaceId">OppositeInterfaceId</a>: <i>String</i>
    <a href="#oppositeinterfaceownerid" title="OppositeInterfaceOwnerId">OppositeInterfaceOwnerId</a>: <i>String</i>
    <a href="#oppositerouterid" title="OppositeRouterId">OppositeRouterId</a>: <i>String</i>
    <a href="#oppositeroutertype" title="OppositeRouterType">OppositeRouterType</a>: <i>String</i>
</pre>

## Properties

#### InterfaceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeInterfaceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeInterfaceOwnerId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeRouterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeRouterType

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

