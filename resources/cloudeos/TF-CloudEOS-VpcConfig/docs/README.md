# TF::CloudEOS::VpcConfig

The `cloudeos_vpc_config` resource sends the deployment information about the AWS VPC and Azure VNET to CVaaS.
CVaaS returns the peering information required by the Leaf VPC/VNETs to create a VPC/VNET Peering connection with its
corresponding Edge.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudEOS::VpcConfig",
    "Properties" : {
        "<a href="#closid" title="ClosId">ClosId</a>" : <i>String</i>,
        "<a href="#closname" title="ClosName">ClosName</a>" : <i>String</i>,
        "<a href="#cloudprovider" title="CloudProvider">CloudProvider</a>" : <i>String</i>,
        "<a href="#cnps" title="Cnps">Cnps</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rgname" title="RgName">RgName</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#topologyid" title="TopologyId">TopologyId</a>" : <i>String</i>,
        "<a href="#topologyname" title="TopologyName">TopologyName</a>" : <i>String</i>,
        "<a href="#vnetname" title="VnetName">VnetName</a>" : <i>String</i>,
        "<a href="#wanid" title="WanId">WanId</a>" : <i>String</i>,
        "<a href="#wanname" title="WanName">WanName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudEOS::VpcConfig
Properties:
    <a href="#closid" title="ClosId">ClosId</a>: <i>String</i>
    <a href="#closname" title="ClosName">ClosName</a>: <i>String</i>
    <a href="#cloudprovider" title="CloudProvider">CloudProvider</a>: <i>String</i>
    <a href="#cnps" title="Cnps">Cnps</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rgname" title="RgName">RgName</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#topologyid" title="TopologyId">TopologyId</a>: <i>String</i>
    <a href="#topologyname" title="TopologyName">TopologyName</a>: <i>String</i>
    <a href="#vnetname" title="VnetName">VnetName</a>: <i>String</i>
    <a href="#wanid" title="WanId">WanId</a>: <i>String</i>
    <a href="#wanname" title="WanName">WanName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ClosId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClosName

CLOS Name this VPC refers to for attributes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProvider

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cnps

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RgName

Resource group name, only valid for Azure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

CloudEdge or CloudLeaf.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyName

Name of topology resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetName

VNET name, only valid for Azure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanName

WAN Name this VPC refers to for attributes.

_Required_: No

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

#### PeerRgName

Returns the <code>PeerRgName</code> value.

#### PeerVnetId

Returns the <code>PeerVnetId</code> value.

#### PeerVnetName

Returns the <code>PeerVnetName</code> value.

#### PeerVpcCidr

Returns the <code>PeerVpcCidr</code> value.

#### PeerVpcId

Returns the <code>PeerVpcId</code> value.

#### Peervpcidr

Returns the <code>Peervpcidr</code> value.

#### TfId

Returns the <code>TfId</code> value.

