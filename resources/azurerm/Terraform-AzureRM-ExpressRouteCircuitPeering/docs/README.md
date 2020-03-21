# Terraform::AzureRM::ExpressRouteCircuitPeering

CloudFormation equivalent of azurerm_express_route_circuit_peering

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ExpressRouteCircuitPeering",
    "Properties" : {
        "<a href="#expressroutecircuitname" title="ExpressRouteCircuitName">ExpressRouteCircuitName</a>" : <i>String</i>,
        "<a href="#peerasn" title="PeerAsn">PeerAsn</a>" : <i>Double</i>,
        "<a href="#peeringtype" title="PeeringType">PeeringType</a>" : <i>String</i>,
        "<a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>" : <i>String</i>,
        "<a href="#sharedkey" title="SharedKey">SharedKey</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#microsoftpeeringconfig" title="MicrosoftPeeringConfig">MicrosoftPeeringConfig</a>" : <i>[ <a href="microsoftpeeringconfig.md">MicrosoftPeeringConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ExpressRouteCircuitPeering
Properties:
    <a href="#expressroutecircuitname" title="ExpressRouteCircuitName">ExpressRouteCircuitName</a>: <i>String</i>
    <a href="#peerasn" title="PeerAsn">PeerAsn</a>: <i>Double</i>
    <a href="#peeringtype" title="PeeringType">PeeringType</a>: <i>String</i>
    <a href="#primarypeeraddressprefix" title="PrimaryPeerAddressPrefix">PrimaryPeerAddressPrefix</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#secondarypeeraddressprefix" title="SecondaryPeerAddressPrefix">SecondaryPeerAddressPrefix</a>: <i>String</i>
    <a href="#sharedkey" title="SharedKey">SharedKey</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#microsoftpeeringconfig" title="MicrosoftPeeringConfig">MicrosoftPeeringConfig</a>: <i>
      - <a href="microsoftpeeringconfig.md">MicrosoftPeeringConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ExpressRouteCircuitName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAsn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryPeerAddressPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryPeerAddressPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicrosoftPeeringConfig

_Required_: No

_Type_: List of <a href="microsoftpeeringconfig.md">MicrosoftPeeringConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AzureAsn

Returns the <code>AzureAsn</code> value.

#### PrimaryAzurePort

Returns the <code>PrimaryAzurePort</code> value.

#### SecondaryAzurePort

Returns the <code>SecondaryAzurePort</code> value.

