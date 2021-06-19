# TF::Aviatrix::TransitVpc

The aviatrix_transit_vpc resource creates and manages the Aviatrix Transit Network Gateways.

!> **WARNING:** The `aviatrix_transit_vpc` resource is deprecated as of **Release 2.0**. It is currently kept for backward-compatibility and will be removed in the future. Please use the transit gateway resource instead. If this is already in the state, please remove it from state file and import as `aviatrix_transit_gateway`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::TransitVpc",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>Double</i>,
        "<a href="#connectedtransit" title="ConnectedTransit">ConnectedTransit</a>" : <i>String</i>,
        "<a href="#enablefirenetinterfaces" title="EnableFirenetInterfaces">EnableFirenetInterfaces</a>" : <i>Boolean</i>,
        "<a href="#enablehybridconnection" title="EnableHybridConnection">EnableHybridConnection</a>" : <i>Boolean</i>,
        "<a href="#enablenat" title="EnableNat">EnableNat</a>" : <i>String</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#hagwsize" title="HaGwSize">HaGwSize</a>" : <i>String</i>,
        "<a href="#hainsanemodeaz" title="HaInsaneModeAz">HaInsaneModeAz</a>" : <i>String</i>,
        "<a href="#hasubnet" title="HaSubnet">HaSubnet</a>" : <i>String</i>,
        "<a href="#insanemode" title="InsaneMode">InsaneMode</a>" : <i>Boolean</i>,
        "<a href="#insanemodeaz" title="InsaneModeAz">InsaneModeAz</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#taglist" title="TagList">TagList</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcreg" title="VpcReg">VpcReg</a>" : <i>String</i>,
        "<a href="#vpcsize" title="VpcSize">VpcSize</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::TransitVpc
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>Double</i>
    <a href="#connectedtransit" title="ConnectedTransit">ConnectedTransit</a>: <i>String</i>
    <a href="#enablefirenetinterfaces" title="EnableFirenetInterfaces">EnableFirenetInterfaces</a>: <i>Boolean</i>
    <a href="#enablehybridconnection" title="EnableHybridConnection">EnableHybridConnection</a>: <i>Boolean</i>
    <a href="#enablenat" title="EnableNat">EnableNat</a>: <i>String</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#hagwsize" title="HaGwSize">HaGwSize</a>: <i>String</i>
    <a href="#hainsanemodeaz" title="HaInsaneModeAz">HaInsaneModeAz</a>: <i>String</i>
    <a href="#hasubnet" title="HaSubnet">HaSubnet</a>: <i>String</i>
    <a href="#insanemode" title="InsaneMode">InsaneMode</a>: <i>Boolean</i>
    <a href="#insanemodeaz" title="InsaneModeAz">InsaneModeAz</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#taglist" title="TagList">TagList</a>: <i>
      - String</i>
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

Type of cloud service provider, requires an integer value. Use 1 for AWS.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectedTransit

Specify Connected Transit status. Supported values: true, false.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFirenetInterfaces

Sign of readiness for FireNet connection. Valid values: true and false. Default: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHybridConnection

Sign of readiness for TGW connection. Only supported for aws. Example: false.

_Required_: No

_Type_: Boolean

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

#### HaInsaneModeAz

AZ of subnet being created for Insane Mode Transit HA Gateway. Required if insane_mode is enabled and ha_subnet is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaSubnet

HA Subnet CIDR. Example: "10.12.0.0/24".Setting to empty/unset will disable HA. Setting to a valid subnet CIDR will create an HA gateway on the subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsaneMode

Specify Insane Mode high performance gateway. Insane Mode gateway size must be at least c5 size. If enabled, will look for spare /26 segment to create a new subnet. Only available for AWS. Supported values: true, false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsaneModeAz

AZ of subnet being created for Insane Mode Transit Gateway. Required if insane_mode is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Public Subnet CIDR. Example: AWS: "10.0.0.0/24". Copy/paste from AWS Console to get the right subnet CIDR.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagList

Instance tag of cloud provider. Only supported for aws. Example: ["key1:value1","key002:value002"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC-ID/VNet-Name of cloud provider. Required if for aws. Example: AWS: "vpc-abcd1234", GCP: "mygooglecloudvpcname", etc...

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcReg

Region of cloud provider. Example: AWS: "us-east-1", ARM: "East US 2", etc...

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSize

Size of the gateway instance. Example: AWS: "t2.large", etc...

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

