# TF::AzureRM::VirtualHubConnection

Manages a Connection for a Virtual Hub.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::VirtualHubConnection",
    "Properties" : {
        "<a href="#hubtovitualnetworktrafficallowed" title="HubToVitualNetworkTrafficAllowed">HubToVitualNetworkTrafficAllowed</a>" : <i>Boolean</i>,
        "<a href="#internetsecurityenabled" title="InternetSecurityEnabled">InternetSecurityEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotevirtualnetworkid" title="RemoteVirtualNetworkId">RemoteVirtualNetworkId</a>" : <i>String</i>,
        "<a href="#virtualhubid" title="VirtualHubId">VirtualHubId</a>" : <i>String</i>,
        "<a href="#vitualnetworktohubgatewaystrafficallowed" title="VitualNetworkToHubGatewaysTrafficAllowed">VitualNetworkToHubGatewaysTrafficAllowed</a>" : <i>Boolean</i>,
        "<a href="#routing" title="Routing">Routing</a>" : <i>[ <a href="routingdefinition.md">RoutingDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::VirtualHubConnection
Properties:
    <a href="#hubtovitualnetworktrafficallowed" title="HubToVitualNetworkTrafficAllowed">HubToVitualNetworkTrafficAllowed</a>: <i>Boolean</i>
    <a href="#internetsecurityenabled" title="InternetSecurityEnabled">InternetSecurityEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotevirtualnetworkid" title="RemoteVirtualNetworkId">RemoteVirtualNetworkId</a>: <i>String</i>
    <a href="#virtualhubid" title="VirtualHubId">VirtualHubId</a>: <i>String</i>
    <a href="#vitualnetworktohubgatewaystrafficallowed" title="VitualNetworkToHubGatewaysTrafficAllowed">VitualNetworkToHubGatewaysTrafficAllowed</a>: <i>Boolean</i>
    <a href="#routing" title="Routing">Routing</a>: <i>
      - <a href="routingdefinition.md">RoutingDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### HubToVitualNetworkTrafficAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetSecurityEnabled

Should Internet Security be enabled to secure internet traffic? Changing this forces a new resource to be created. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name which should be used for this Connection, which must be unique within the Virtual Hub. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteVirtualNetworkId

The ID of the Virtual Network which the Virtual Hub should be connected to. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualHubId

The ID of the Virtual Hub within which this connection should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VitualNetworkToHubGatewaysTrafficAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routing

_Required_: No

_Type_: List of <a href="routingdefinition.md">RoutingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

