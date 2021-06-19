# TF::Aviatrix::TransPeer

The **aviatrix_trans_peer** resource allows the creation and management of Aviatrix [Encrypted Transitive Peering](https://docs.aviatrix.com/HowTos/TransPeering.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::TransPeer",
    "Properties" : {
        "<a href="#nexthop" title="Nexthop">Nexthop</a>" : <i>String</i>,
        "<a href="#reachablecidr" title="ReachableCidr">ReachableCidr</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::TransPeer
Properties:
    <a href="#nexthop" title="Nexthop">Nexthop</a>: <i>String</i>
    <a href="#reachablecidr" title="ReachableCidr">ReachableCidr</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### Nexthop

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReachableCidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: Yes

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

