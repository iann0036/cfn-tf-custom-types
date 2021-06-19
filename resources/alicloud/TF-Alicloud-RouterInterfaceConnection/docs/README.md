# TF::Alicloud::RouterInterfaceConnection

Provides a VPC router interface connection resource to connect two router interfaces which are in two different VPCs.
After that, all of the two router interfaces will be active.

-> **NOTE:** At present, Router interface does not support changing opposite router interface, the connection delete action is only deactivating it to inactive, not modifying the connection to empty.

-> **NOTE:** If you want to changing opposite router interface, you can delete router interface and re-build them.

-> **NOTE:** A integrated router interface connection tunnel requires both InitiatingSide and AcceptingSide configuring opposite router interface.

-> **NOTE:** Please remember to add a `depends_on` clause in the router interface connection from the InitiatingSide to the AcceptingSide, because the connection from the AcceptingSide to the InitiatingSide must be done first.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::RouterInterfaceConnection",
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
Type: TF::Alicloud::RouterInterfaceConnection
Properties:
    <a href="#interfaceid" title="InterfaceId">InterfaceId</a>: <i>String</i>
    <a href="#oppositeinterfaceid" title="OppositeInterfaceId">OppositeInterfaceId</a>: <i>String</i>
    <a href="#oppositeinterfaceownerid" title="OppositeInterfaceOwnerId">OppositeInterfaceOwnerId</a>: <i>String</i>
    <a href="#oppositerouterid" title="OppositeRouterId">OppositeRouterId</a>: <i>String</i>
    <a href="#oppositeroutertype" title="OppositeRouterType">OppositeRouterType</a>: <i>String</i>
</pre>

## Properties

#### InterfaceId

One side router interface ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeInterfaceId

Another side router interface ID. It must belong the specified "opposite_interface_owner_id" account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeInterfaceOwnerId

Another side router interface account ID. Log on to the Alibaba Cloud console, select User Info > Account Management to check the account ID. Default to [Provider account_id](https://www.terraform.io/docs/providers/alicloud/index.html#account_id).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeRouterId

Another side router ID. It must belong the specified "opposite_interface_owner_id" account. It is valid when field "opposite_interface_owner_id" is specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OppositeRouterType

Another side router Type. Optional value: VRouter, VBR. It is valid when field "opposite_interface_owner_id" is specified.

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

#### Id

Returns the <code>Id</code> value.

