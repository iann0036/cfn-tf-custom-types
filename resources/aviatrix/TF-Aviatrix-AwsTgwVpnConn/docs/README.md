# TF::Aviatrix::AwsTgwVpnConn

The **aviatrix_aws_tgw_vpn_conn** resource allows the creation and management of Aviatrix AWS TGW VPN connections in their selected Security Domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsTgwVpnConn",
    "Properties" : {
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#connectiontype" title="ConnectionType">ConnectionType</a>" : <i>String</i>,
        "<a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>" : <i>Boolean</i>,
        "<a href="#insideipcidrtun1" title="InsideIpCidrTun1">InsideIpCidrTun1</a>" : <i>String</i>,
        "<a href="#insideipcidrtun2" title="InsideIpCidrTun2">InsideIpCidrTun2</a>" : <i>String</i>,
        "<a href="#presharedkeytun1" title="PreSharedKeyTun1">PreSharedKeyTun1</a>" : <i>String</i>,
        "<a href="#presharedkeytun2" title="PreSharedKeyTun2">PreSharedKeyTun2</a>" : <i>String</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>String</i>,
        "<a href="#remoteasnumber" title="RemoteAsNumber">RemoteAsNumber</a>" : <i>String</i>,
        "<a href="#remotecidr" title="RemoteCidr">RemoteCidr</a>" : <i>String</i>,
        "<a href="#routedomainname" title="RouteDomainName">RouteDomainName</a>" : <i>String</i>,
        "<a href="#tgwname" title="TgwName">TgwName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsTgwVpnConn
Properties:
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#connectiontype" title="ConnectionType">ConnectionType</a>: <i>String</i>
    <a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>: <i>Boolean</i>
    <a href="#insideipcidrtun1" title="InsideIpCidrTun1">InsideIpCidrTun1</a>: <i>String</i>
    <a href="#insideipcidrtun2" title="InsideIpCidrTun2">InsideIpCidrTun2</a>: <i>String</i>
    <a href="#presharedkeytun1" title="PreSharedKeyTun1">PreSharedKeyTun1</a>: <i>String</i>
    <a href="#presharedkeytun2" title="PreSharedKeyTun2">PreSharedKeyTun2</a>: <i>String</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>String</i>
    <a href="#remoteasnumber" title="RemoteAsNumber">RemoteAsNumber</a>: <i>String</i>
    <a href="#remotecidr" title="RemoteCidr">RemoteCidr</a>: <i>String</i>
    <a href="#routedomainname" title="RouteDomainName">RouteDomainName</a>: <i>String</i>
    <a href="#tgwname" title="TgwName">TgwName</a>: <i>String</i>
</pre>

## Properties

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLearnedCidrsApproval

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideIpCidrTun1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideIpCidrTun2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSharedKeyTun1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSharedKeyTun2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAsNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteDomainName

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

#### VpnId

Returns the <code>VpnId</code> value.

