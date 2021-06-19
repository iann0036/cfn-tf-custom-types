# TF::Aviatrix::SpokeVpc

The aviatrix_spoke_vpc resource allows to create and manage Aviatrix Spoke Gateways.

!> **WARNING:** The `aviatrix_spoke_vpc` resource is deprecated as of **Release 2.0**. It is currently kept for backward-compatibility and will be removed in the future. Please use the spoke gateway resource instead. If this is already in the state, please remove it from the state file and import as `aviatrix_spoke_gateway`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SpokeVpc",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>Double</i>,
        "<a href="#enablenat" title="EnableNat">EnableNat</a>" : <i>String</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#hagwsize" title="HaGwSize">HaGwSize</a>" : <i>String</i>,
        "<a href="#hasubnet" title="HaSubnet">HaSubnet</a>" : <i>String</i>,
        "<a href="#hazone" title="HaZone">HaZone</a>" : <i>String</i>,
        "<a href="#singleazha" title="SingleAzHa">SingleAzHa</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#taglist" title="TagList">TagList</a>" : <i>[ String, ... ]</i>,
        "<a href="#transitgw" title="TransitGw">TransitGw</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcreg" title="VpcReg">VpcReg</a>" : <i>String</i>,
        "<a href="#vpcsize" title="VpcSize">VpcSize</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SpokeVpc
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>Double</i>
    <a href="#enablenat" title="EnableNat">EnableNat</a>: <i>String</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#hagwsize" title="HaGwSize">HaGwSize</a>: <i>String</i>
    <a href="#hasubnet" title="HaSubnet">HaSubnet</a>: <i>String</i>
    <a href="#hazone" title="HaZone">HaZone</a>: <i>String</i>
    <a href="#singleazha" title="SingleAzHa">SingleAzHa</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#taglist" title="TagList">TagList</a>: <i>
      - String</i>
    <a href="#transitgw" title="TransitGw">TransitGw</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcreg" title="VpcReg">VpcReg</a>: <i>String</i>
    <a href="#vpcsize" title="VpcSize">VpcSize</a>: <i>String</i>
</pre>

## Properties

#### AccountName

This parameter represents the name of a Cloud-Account in Aviatrix controller.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

Type of cloud service provider. AWS=1, GCP=4, ARM=8.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName

Name of the gateway which is going to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaGwSize

HA Gateway Size. Mandatory if HA is enabled (ha_subnet is set). Example: "t2.micro".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaSubnet

HA Subnet. Required for enabling HA for AWS/ARM gateways. Setting to empty/unset will disable HA. Setting to a valid subnet (Example: 10.12.0.0/24) will create an HA gateway on the subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaZone

HA Zone. Required for enabling HA for GCP gateway. Setting to empty/unset will disable HA. Setting to a valid zone will create an HA gateway in the zone. Example: "us-west1-c".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleAzHa

Set to "enabled" if this feature is desired.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Public Subnet Info. Example: AWS: "CIDRZONESubnetName", etc...

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagList

Instance tag of cloud provider. Example: key1:value1,key002:value002, etc... Only AWS (cloud_type is "1") is supported.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGw

Specify the transit Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC-ID/VNet-Name of cloud provider. Required if cloud_type is "1" or "4". Example: AWS: "vpc-abcd1234", etc...

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcReg

Region of cloud provider. Example: AWS: "us-east-1", GCP: "us-west1-b", ARM: "East US 2", etc...

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSize

Size of the gateway instance. Example: AWS: "t2.large", GCP: "f1.micro", ARM: "StandardD2", etc...

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

#### CloudInstanceId

Returns the <code>CloudInstanceId</code> value.

#### Id

Returns the <code>Id</code> value.

