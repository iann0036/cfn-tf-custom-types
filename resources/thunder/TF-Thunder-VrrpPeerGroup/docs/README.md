# TF::Thunder::VrrpPeerGroup

`thunder_vrrp_peer_group` Provides details about thunder vrrp peer group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::VrrpPeerGroup",
    "Properties" : {
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#peer" title="Peer">Peer</a>" : <i>[ <a href="peerdefinition.md">PeerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::VrrpPeerGroup
Properties:
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#peer" title="Peer">Peer</a>: <i>
      - <a href="peerdefinition.md">PeerDefinition</a></i>
</pre>

## Properties

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peer

_Required_: No

_Type_: List of <a href="peerdefinition.md">PeerDefinition</a>

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

