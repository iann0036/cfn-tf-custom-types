# TF::Rancher2::ClusterSync

CloudFormation equivalent of rancher2_cluster_sync

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::ClusterSync",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#nodepoolids" title="NodePoolIds">NodePoolIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#stateconfirm" title="StateConfirm">StateConfirm</a>" : <i>Double</i>,
        "<a href="#synced" title="Synced">Synced</a>" : <i>Boolean</i>,
        "<a href="#waitalerting" title="WaitAlerting">WaitAlerting</a>" : <i>Boolean</i>,
        "<a href="#waitcatalogs" title="WaitCatalogs">WaitCatalogs</a>" : <i>Boolean</i>,
        "<a href="#waitmonitoring" title="WaitMonitoring">WaitMonitoring</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::ClusterSync
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#nodepoolids" title="NodePoolIds">NodePoolIds</a>: <i>
      - String</i>
    <a href="#stateconfirm" title="StateConfirm">StateConfirm</a>: <i>Double</i>
    <a href="#synced" title="Synced">Synced</a>: <i>Boolean</i>
    <a href="#waitalerting" title="WaitAlerting">WaitAlerting</a>: <i>Boolean</i>
    <a href="#waitcatalogs" title="WaitCatalogs">WaitCatalogs</a>: <i>Boolean</i>
    <a href="#waitmonitoring" title="WaitMonitoring">WaitMonitoring</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ClusterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePoolIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateConfirm

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Synced

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitAlerting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitCatalogs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitMonitoring

_Required_: No

_Type_: Boolean

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

#### DefaultProjectId

Returns the <code>DefaultProjectId</code> value.

#### Id

Returns the <code>Id</code> value.

#### KubeConfig

Returns the <code>KubeConfig</code> value.

#### Nodes

Returns the <code>Nodes</code> value.

#### SystemProjectId

Returns the <code>SystemProjectId</code> value.

