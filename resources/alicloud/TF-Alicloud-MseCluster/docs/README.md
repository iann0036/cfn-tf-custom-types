# TF::Alicloud::MseCluster

Provides a MSE Cluster resource. It is a one-stop microservice platform for the industry's mainstream open source microservice frameworks Spring Cloud and Dubbo, providing governance center, managed registry and managed configuration center.

-> **NOTE:** Available in 1.94.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::MseCluster",
    "Properties" : {
        "<a href="#aclentrylist" title="AclEntryList">AclEntryList</a>" : <i>[ String, ... ]</i>,
        "<a href="#clusteraliasname" title="ClusterAliasName">ClusterAliasName</a>" : <i>String</i>,
        "<a href="#clusterspecification" title="ClusterSpecification">ClusterSpecification</a>" : <i>String</i>,
        "<a href="#clustertype" title="ClusterType">ClusterType</a>" : <i>String</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
        "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
        "<a href="#nettype" title="NetType">NetType</a>" : <i>String</i>,
        "<a href="#privateslbspecification" title="PrivateSlbSpecification">PrivateSlbSpecification</a>" : <i>String</i>,
        "<a href="#pubnetworkflow" title="PubNetworkFlow">PubNetworkFlow</a>" : <i>String</i>,
        "<a href="#pubslbspecification" title="PubSlbSpecification">PubSlbSpecification</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::MseCluster
Properties:
    <a href="#aclentrylist" title="AclEntryList">AclEntryList</a>: <i>
      - String</i>
    <a href="#clusteraliasname" title="ClusterAliasName">ClusterAliasName</a>: <i>String</i>
    <a href="#clusterspecification" title="ClusterSpecification">ClusterSpecification</a>: <i>String</i>
    <a href="#clustertype" title="ClusterType">ClusterType</a>: <i>String</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
    <a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
    <a href="#nettype" title="NetType">NetType</a>: <i>String</i>
    <a href="#privateslbspecification" title="PrivateSlbSpecification">PrivateSlbSpecification</a>: <i>String</i>
    <a href="#pubnetworkflow" title="PubNetworkFlow">PubNetworkFlow</a>: <i>String</i>
    <a href="#pubslbspecification" title="PubSlbSpecification">PubSlbSpecification</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AclEntryList

The whitelist.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAliasName

The alias of MSE Cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterSpecification

The engine specification of MSE Cluster. Valid values: `MSE_SC_1_2_200_c`, `MSE_SC_2`, `MSE_SC_4_8_200_c_4_200_c`, `MSE_SC_8_16_200_c`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterType

The type of MSE Cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

The version of MSE Cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

The type of Disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

The count of instance.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetType

The type of network. Range limit: 1~5.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateSlbSpecification

The specification of private network SLB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PubNetworkFlow

The public network bandwidth. `0` means no access to the public network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PubSlbSpecification

The specification of public network SLB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The id of VSwitch.

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

#### Status

Returns the <code>Status</code> value.

