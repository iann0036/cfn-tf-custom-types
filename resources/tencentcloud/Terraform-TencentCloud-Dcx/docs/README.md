# Terraform::TencentCloud::Dcx

Provides a resource to creating dedicated tunnels instances.

~> **NOTE:** 1. ID of the DC is queried, can only apply for this resource offline.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::Dcx",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#bgpasn" title="BgpAsn">BgpAsn</a>" : <i>Double</i>,
        "<a href="#bgpauthkey" title="BgpAuthKey">BgpAuthKey</a>" : <i>String</i>,
        "<a href="#customeraddress" title="CustomerAddress">CustomerAddress</a>" : <i>String</i>,
        "<a href="#dcid" title="DcId">DcId</a>" : <i>String</i>,
        "<a href="#dcgid" title="DcgId">DcgId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
        "<a href="#routefilterprefixes" title="RouteFilterPrefixes">RouteFilterPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#routetype" title="RouteType">RouteType</a>" : <i>String</i>,
        "<a href="#tencentaddress" title="TencentAddress">TencentAddress</a>" : <i>String</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::Dcx
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#bgpasn" title="BgpAsn">BgpAsn</a>: <i>Double</i>
    <a href="#bgpauthkey" title="BgpAuthKey">BgpAuthKey</a>: <i>String</i>
    <a href="#customeraddress" title="CustomerAddress">CustomerAddress</a>: <i>String</i>
    <a href="#dcid" title="DcId">DcId</a>: <i>String</i>
    <a href="#dcgid" title="DcgId">DcgId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
    <a href="#routefilterprefixes" title="RouteFilterPrefixes">RouteFilterPrefixes</a>: <i>
      - String</i>
    <a href="#routetype" title="RouteType">RouteType</a>: <i>String</i>
    <a href="#tencentaddress" title="TencentAddress">TencentAddress</a>: <i>String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

Bandwidth of the DC.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpAsn

BGP ASN of the user. A required field within BGP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpAuthKey

BGP key of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerAddress

Interconnect IP of the DC within client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DcId

ID of the DC to be queried, application deployment offline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DcgId

ID of the DC Gateway. Currently only new in the console.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the dedicated tunnel.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Type of the network, and available values include VPC, BMVPC and CCN. The default value is VPC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteFilterPrefixes

Static route, the network address of the user IDC. It can be modified after setting but cannot be deleted. AN unable field within BGP.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteType

Type of the route, and available values include BGP and STATIC. The default value is BGP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TencentAddress

Interconnect IP of the DC within Tencent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

Vlan of the dedicated tunnels, and the range of values is [0-3000]. '0' means that only one tunnel can be created for the physical connect.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

ID of the VPC or BMVPC.

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

