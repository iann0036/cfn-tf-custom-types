# TF::Equinix::NetworkBgp

Resource `equinix_network_bgp` allows creation and management of Equinix Network
Edge BGP peering configurations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Equinix::NetworkBgp",
    "Properties" : {
        "<a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>" : <i>String</i>,
        "<a href="#connectionid" title="ConnectionId">ConnectionId</a>" : <i>String</i>,
        "<a href="#localasn" title="LocalAsn">LocalAsn</a>" : <i>Double</i>,
        "<a href="#localipaddress" title="LocalIpAddress">LocalIpAddress</a>" : <i>String</i>,
        "<a href="#remoteasn" title="RemoteAsn">RemoteAsn</a>" : <i>Double</i>,
        "<a href="#remoteipaddress" title="RemoteIpAddress">RemoteIpAddress</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Equinix::NetworkBgp
Properties:
    <a href="#authenticationkey" title="AuthenticationKey">AuthenticationKey</a>: <i>String</i>
    <a href="#connectionid" title="ConnectionId">ConnectionId</a>: <i>String</i>
    <a href="#localasn" title="LocalAsn">LocalAsn</a>: <i>Double</i>
    <a href="#localipaddress" title="LocalIpAddress">LocalIpAddress</a>: <i>String</i>
    <a href="#remoteasn" title="RemoteAsn">RemoteAsn</a>: <i>Double</i>
    <a href="#remoteipaddress" title="RemoteIpAddress">RemoteIpAddress</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AuthenticationKey

shared key used for BGP peer authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionId

identifier of a connection established between
network device and remote service provider that will be used for peering.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAsn

Local ASN number.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpAddress

IP address in CIDR format of a local device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAsn

Remote ASN number.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIpAddress

IP address of remote peer.

_Required_: Yes

_Type_: String

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

#### DeviceId

Returns the <code>DeviceId</code> value.

#### Id

Returns the <code>Id</code> value.

#### ProvisioningStatus

Returns the <code>ProvisioningStatus</code> value.

#### State

Returns the <code>State</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

