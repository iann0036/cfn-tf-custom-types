# TF::Quorum::BootstrapNodeKey

Use this resource to create a node key for a new Quorum node.

Node key encodes a private key that defines an identity of a Quorum node in the network. It is primarily used in P2P networking.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Quorum::BootstrapNodeKey",
    "Properties" : {
    }
}
</pre>

### YAML

<pre>
Type: TF::Quorum::BootstrapNodeKey
Properties:
</pre>

## Properties

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HexNodeId

Returns the <code>HexNodeId</code> value.

#### Id

Returns the <code>Id</code> value.

#### IstanbulAddress

Returns the <code>IstanbulAddress</code> value.

#### NodeId

Returns the <code>NodeId</code> value.

#### NodeKeyHex

Returns the <code>NodeKeyHex</code> value.

