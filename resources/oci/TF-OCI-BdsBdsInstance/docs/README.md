# TF::OCI::BdsBdsInstance

This resource provides the Bds Instance resource in Oracle Cloud Infrastructure Big Data Service service.

Creates a new BDS instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::BdsBdsInstance",
    "Properties" : {
        "<a href="#clusteradminpassword" title="ClusterAdminPassword">ClusterAdminPassword</a>" : <i>String</i>,
        "<a href="#clusterpublickey" title="ClusterPublicKey">ClusterPublicKey</a>" : <i>String</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#iscloudsqlconfigured" title="IsCloudSqlConfigured">IsCloudSqlConfigured</a>" : <i>Boolean</i>,
        "<a href="#ishighavailability" title="IsHighAvailability">IsHighAvailability</a>" : <i>Boolean</i>,
        "<a href="#issecure" title="IsSecure">IsSecure</a>" : <i>Boolean</i>,
        "<a href="#cloudsqldetails" title="CloudSqlDetails">CloudSqlDetails</a>" : <i>[ <a href="cloudsqldetailsdefinition.md">CloudSqlDetailsDefinition</a>, ... ]</i>,
        "<a href="#masternode" title="MasterNode">MasterNode</a>" : <i>[ <a href="masternodedefinition.md">MasterNodeDefinition</a>, ... ]</i>,
        "<a href="#networkconfig" title="NetworkConfig">NetworkConfig</a>" : <i>[ <a href="networkconfigdefinition.md">NetworkConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#utilnode" title="UtilNode">UtilNode</a>" : <i>[ <a href="utilnodedefinition.md">UtilNodeDefinition</a>, ... ]</i>,
        "<a href="#workernode" title="WorkerNode">WorkerNode</a>" : <i>[ <a href="workernodedefinition.md">WorkerNodeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::BdsBdsInstance
Properties:
    <a href="#clusteradminpassword" title="ClusterAdminPassword">ClusterAdminPassword</a>: <i>String</i>
    <a href="#clusterpublickey" title="ClusterPublicKey">ClusterPublicKey</a>: <i>String</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#iscloudsqlconfigured" title="IsCloudSqlConfigured">IsCloudSqlConfigured</a>: <i>Boolean</i>
    <a href="#ishighavailability" title="IsHighAvailability">IsHighAvailability</a>: <i>Boolean</i>
    <a href="#issecure" title="IsSecure">IsSecure</a>: <i>Boolean</i>
    <a href="#cloudsqldetails" title="CloudSqlDetails">CloudSqlDetails</a>: <i>
      - <a href="cloudsqldetailsdefinition.md">CloudSqlDetailsDefinition</a></i>
    <a href="#masternode" title="MasterNode">MasterNode</a>: <i>
      - <a href="masternodedefinition.md">MasterNodeDefinition</a></i>
    <a href="#networkconfig" title="NetworkConfig">NetworkConfig</a>: <i>
      - <a href="networkconfigdefinition.md">NetworkConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#utilnode" title="UtilNode">UtilNode</a>: <i>
      - <a href="utilnodedefinition.md">UtilNodeDefinition</a></i>
    <a href="#workernode" title="WorkerNode">WorkerNode</a>: <i>
      - <a href="workernodedefinition.md">WorkerNodeDefinition</a></i>
</pre>

## Properties

#### ClusterAdminPassword

Base-64 encoded password for Cloudera Manager admin user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterPublicKey

The SSH public key used to authenticate the cluster connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

Version of the Hadoop distribution.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The OCID of the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) Name of the BDS instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCloudSqlConfigured

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHighAvailability

Boolean flag specifying whether or not the cluster is HA.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSecure

Boolean flag specifying whether or not the cluster should be setup as secure.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudSqlDetails

_Required_: No

_Type_: List of <a href="cloudsqldetailsdefinition.md">CloudSqlDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNode

_Required_: No

_Type_: List of <a href="masternodedefinition.md">MasterNodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfig

_Required_: No

_Type_: List of <a href="networkconfigdefinition.md">NetworkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtilNode

_Required_: No

_Type_: List of <a href="utilnodedefinition.md">UtilNodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNode

_Required_: No

_Type_: List of <a href="workernodedefinition.md">WorkerNodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterDetails

Returns the <code>ClusterDetails</code> value.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### Id

Returns the <code>Id</code> value.

#### Nodes

Returns the <code>Nodes</code> value.

#### NumberOfNodes

The amount of worker nodes should be created, at least be 3.
* `shape` - (Required) Shape of the node
* `subnet_id` - (Required) The OCID of the subnet in which the node should be created.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

