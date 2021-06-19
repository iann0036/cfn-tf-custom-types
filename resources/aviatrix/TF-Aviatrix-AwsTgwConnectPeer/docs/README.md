# TF::Aviatrix::AwsTgwConnectPeer

The **aviatrix_aws_tgw_connect_peer** resource allows the creation and management of AWS TGW Connect peers. This
resource is available as of provider version R2.18.1+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsTgwConnectPeer",
    "Properties" : {
        "<a href="#bgpinsidecidrs" title="BgpInsideCidrs">BgpInsideCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#connectattachmentid" title="ConnectAttachmentId">ConnectAttachmentId</a>" : <i>String</i>,
        "<a href="#connectpeername" title="ConnectPeerName">ConnectPeerName</a>" : <i>String</i>,
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#peerasnumber" title="PeerAsNumber">PeerAsNumber</a>" : <i>String</i>,
        "<a href="#peergreaddress" title="PeerGreAddress">PeerGreAddress</a>" : <i>String</i>,
        "<a href="#tgwgreaddress" title="TgwGreAddress">TgwGreAddress</a>" : <i>String</i>,
        "<a href="#tgwname" title="TgwName">TgwName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsTgwConnectPeer
Properties:
    <a href="#bgpinsidecidrs" title="BgpInsideCidrs">BgpInsideCidrs</a>: <i>
      - String</i>
    <a href="#connectattachmentid" title="ConnectAttachmentId">ConnectAttachmentId</a>: <i>String</i>
    <a href="#connectpeername" title="ConnectPeerName">ConnectPeerName</a>: <i>String</i>
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#peerasnumber" title="PeerAsNumber">PeerAsNumber</a>: <i>String</i>
    <a href="#peergreaddress" title="PeerGreAddress">PeerGreAddress</a>: <i>String</i>
    <a href="#tgwgreaddress" title="TgwGreAddress">TgwGreAddress</a>: <i>String</i>
    <a href="#tgwname" title="TgwName">TgwName</a>: <i>String</i>
</pre>

## Properties

#### BgpInsideCidrs

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectAttachmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectPeerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAsNumber

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGreAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwGreAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwName

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

#### ConnectPeerId

Returns the <code>ConnectPeerId</code> value.

#### Id

Returns the <code>Id</code> value.

