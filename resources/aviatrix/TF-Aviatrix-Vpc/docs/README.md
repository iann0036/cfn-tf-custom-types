# TF::Aviatrix::Vpc

The **aviatrix_vpc** resource allows the creation and management of Aviatrix-created VPCs of various cloud types.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Vpc",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#aviatrixfirenetvpc" title="AviatrixFirenetVpc">AviatrixFirenetVpc</a>" : <i>Boolean</i>,
        "<a href="#aviatrixtransitvpc" title="AviatrixTransitVpc">AviatrixTransitVpc</a>" : <i>Boolean</i>,
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>Double</i>,
        "<a href="#enablenativegwlb" title="EnableNativeGwlb">EnableNativeGwlb</a>" : <i>Boolean</i>,
        "<a href="#enableprivateoobsubnet" title="EnablePrivateOobSubnet">EnablePrivateOobSubnet</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numofsubnetpairs" title="NumOfSubnetPairs">NumOfSubnetPairs</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#subnetsize" title="SubnetSize">SubnetSize</a>" : <i>Double</i>,
        "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ <a href="subnetsdefinition.md">SubnetsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Vpc
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#aviatrixfirenetvpc" title="AviatrixFirenetVpc">AviatrixFirenetVpc</a>: <i>Boolean</i>
    <a href="#aviatrixtransitvpc" title="AviatrixTransitVpc">AviatrixTransitVpc</a>: <i>Boolean</i>
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>Double</i>
    <a href="#enablenativegwlb" title="EnableNativeGwlb">EnableNativeGwlb</a>: <i>Boolean</i>
    <a href="#enableprivateoobsubnet" title="EnablePrivateOobSubnet">EnablePrivateOobSubnet</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numofsubnetpairs" title="NumOfSubnetPairs">NumOfSubnetPairs</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#subnetsize" title="SubnetSize">SubnetSize</a>: <i>Double</i>
    <a href="#subnets" title="Subnets">Subnets</a>: <i>
      - <a href="subnetsdefinition.md">SubnetsDefinition</a></i>
</pre>

## Properties

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AviatrixFirenetVpc

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AviatrixTransitVpc

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNativeGwlb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateOobSubnet

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumOfSubnetPairs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of <a href="subnetsdefinition.md">SubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AzureVnetResourceId

Returns the <code>AzureVnetResourceId</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrivateSubnets

Returns the <code>PrivateSubnets</code> value.

#### PublicSubnets

Returns the <code>PublicSubnets</code> value.

#### RouteTables

Returns the <code>RouteTables</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

