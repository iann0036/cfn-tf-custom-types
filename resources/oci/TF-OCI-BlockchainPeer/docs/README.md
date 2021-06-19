# TF::OCI::BlockchainPeer

This resource provides the Peer resource in Oracle Cloud Infrastructure Blockchain service.

Create Blockchain Platform Peer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::BlockchainPeer",
    "Properties" : {
        "<a href="#ad" title="Ad">Ad</a>" : <i>String</i>,
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
        "<a href="#blockchainplatformid" title="BlockchainPlatformId">BlockchainPlatformId</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#ocpuallocationparam" title="OcpuAllocationParam">OcpuAllocationParam</a>" : <i>[ <a href="ocpuallocationparamdefinition.md">OcpuAllocationParamDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::BlockchainPeer
Properties:
    <a href="#ad" title="Ad">Ad</a>: <i>String</i>
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
    <a href="#blockchainplatformid" title="BlockchainPlatformId">BlockchainPlatformId</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#ocpuallocationparam" title="OcpuAllocationParam">OcpuAllocationParam</a>: <i>
      - <a href="ocpuallocationparamdefinition.md">OcpuAllocationParamDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Ad

Availability Domain to place new peer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alias

peer alias.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockchainPlatformId

Unique service identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

Peer role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcpuAllocationParam

_Required_: No

_Type_: List of <a href="ocpuallocationparamdefinition.md">OcpuAllocationParamDefinition</a>

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

#### Host

Returns the <code>Host</code> value.

#### Id

Returns the <code>Id</code> value.

#### PeerKey

Returns the <code>PeerKey</code> value.

#### State

Returns the <code>State</code> value.

