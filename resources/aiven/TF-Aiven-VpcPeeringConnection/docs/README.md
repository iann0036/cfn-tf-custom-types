# TF::Aiven::VpcPeeringConnection

CloudFormation equivalent of aiven_vpc_peering_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aiven::VpcPeeringConnection",
    "Properties" : {
        "<a href="#peerazureappid" title="PeerAzureAppId">PeerAzureAppId</a>" : <i>String</i>,
        "<a href="#peerazuretenantid" title="PeerAzureTenantId">PeerAzureTenantId</a>" : <i>String</i>,
        "<a href="#peercloudaccount" title="PeerCloudAccount">PeerCloudAccount</a>" : <i>String</i>,
        "<a href="#peerregion" title="PeerRegion">PeerRegion</a>" : <i>String</i>,
        "<a href="#peerresourcegroup" title="PeerResourceGroup">PeerResourceGroup</a>" : <i>String</i>,
        "<a href="#peervpc" title="PeerVpc">PeerVpc</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aiven::VpcPeeringConnection
Properties:
    <a href="#peerazureappid" title="PeerAzureAppId">PeerAzureAppId</a>: <i>String</i>
    <a href="#peerazuretenantid" title="PeerAzureTenantId">PeerAzureTenantId</a>: <i>String</i>
    <a href="#peercloudaccount" title="PeerCloudAccount">PeerCloudAccount</a>: <i>String</i>
    <a href="#peerregion" title="PeerRegion">PeerRegion</a>: <i>String</i>
    <a href="#peerresourcegroup" title="PeerResourceGroup">PeerResourceGroup</a>: <i>String</i>
    <a href="#peervpc" title="PeerVpc">PeerVpc</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### PeerAzureAppId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAzureTenantId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerCloudAccount

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerVpc

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

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

#### Id

Returns the <code>Id</code> value.

#### PeeringConnectionId

Returns the <code>PeeringConnectionId</code> value.

#### State

Returns the <code>State</code> value.

#### StateInfo

Returns the <code>StateInfo</code> value.

