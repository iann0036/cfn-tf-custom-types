# TF::Nutanix::RecoveryPlan AvailabilityZoneNetworkMappingListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityzoneurl" title="AvailabilityZoneUrl">AvailabilityZoneUrl</a>" : <i>String</i>,
    "<a href="#clusterreferencelist" title="ClusterReferenceList">ClusterReferenceList</a>" : <i>[ <a href="clusterreferencelistdefinition.md">ClusterReferenceListDefinition</a>, ... ]</i>,
    "<a href="#recoveryipassignmentlist" title="RecoveryIpAssignmentList">RecoveryIpAssignmentList</a>" : <i>[ <a href="recoveryipassignmentlistdefinition.md">RecoveryIpAssignmentListDefinition</a>, ... ]</i>,
    "<a href="#recoverynetwork" title="RecoveryNetwork">RecoveryNetwork</a>" : <i>[ <a href="recoverynetworkdefinition.md">RecoveryNetworkDefinition</a>, ... ]</i>,
    "<a href="#testipassignmentlist" title="TestIpAssignmentList">TestIpAssignmentList</a>" : <i>[ <a href="testipassignmentlistdefinition.md">TestIpAssignmentListDefinition</a>, ... ]</i>,
    "<a href="#testnetwork" title="TestNetwork">TestNetwork</a>" : <i>[ <a href="testnetworkdefinition.md">TestNetworkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityzoneurl" title="AvailabilityZoneUrl">AvailabilityZoneUrl</a>: <i>String</i>
<a href="#clusterreferencelist" title="ClusterReferenceList">ClusterReferenceList</a>: <i>
      - <a href="clusterreferencelistdefinition.md">ClusterReferenceListDefinition</a></i>
<a href="#recoveryipassignmentlist" title="RecoveryIpAssignmentList">RecoveryIpAssignmentList</a>: <i>
      - <a href="recoveryipassignmentlistdefinition.md">RecoveryIpAssignmentListDefinition</a></i>
<a href="#recoverynetwork" title="RecoveryNetwork">RecoveryNetwork</a>: <i>
      - <a href="recoverynetworkdefinition.md">RecoveryNetworkDefinition</a></i>
<a href="#testipassignmentlist" title="TestIpAssignmentList">TestIpAssignmentList</a>: <i>
      - <a href="testipassignmentlistdefinition.md">TestIpAssignmentListDefinition</a></i>
<a href="#testnetwork" title="TestNetwork">TestNetwork</a>: <i>
      - <a href="testnetworkdefinition.md">TestNetworkDefinition</a></i>
</pre>

## Properties

#### AvailabilityZoneUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterReferenceList

_Required_: No

_Type_: List of <a href="clusterreferencelistdefinition.md">ClusterReferenceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryIpAssignmentList

_Required_: No

_Type_: List of <a href="recoveryipassignmentlistdefinition.md">RecoveryIpAssignmentListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryNetwork

_Required_: No

_Type_: List of <a href="recoverynetworkdefinition.md">RecoveryNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestIpAssignmentList

_Required_: No

_Type_: List of <a href="testipassignmentlistdefinition.md">TestIpAssignmentListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestNetwork

_Required_: No

_Type_: List of <a href="testnetworkdefinition.md">TestNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

