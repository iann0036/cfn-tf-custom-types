# Terraform::Google::DataprocCluster ClusterConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#stagingbucket" title="StagingBucket">StagingBucket</a>" : <i>String</i>,
    "<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>" : <i>[ <a href="clusterconfig-autoscalingconfig.md">AutoscalingConfig</a>, ... ]</i>,
    "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ <a href="clusterconfig-encryptionconfig.md">EncryptionConfig</a>, ... ]</i>,
    "<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>" : <i>[ <a href="clusterconfig-gceclusterconfig.md">GceClusterConfig</a>, ... ]</i>,
    "<a href="#initializationaction" title="InitializationAction">InitializationAction</a>" : <i>[ <a href="clusterconfig-initializationaction.md">InitializationAction</a>, ... ]</i>,
    "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ <a href="clusterconfig-masterconfig.md">MasterConfig</a>, ... ]</i>,
    "<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>" : <i>[ <a href="clusterconfig-preemptibleworkerconfig.md">PreemptibleWorkerConfig</a>, ... ]</i>,
    "<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>" : <i>[ <a href="clusterconfig-securityconfig.md">SecurityConfig</a>, ... ]</i>,
    "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ <a href="clusterconfig-softwareconfig.md">SoftwareConfig</a>, ... ]</i>,
    "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ <a href="clusterconfig-workerconfig.md">WorkerConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#stagingbucket" title="StagingBucket">StagingBucket</a>: <i>String</i>
<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>: <i>
      - <a href="clusterconfig-autoscalingconfig.md">AutoscalingConfig</a></i>
<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>: <i>
      - <a href="clusterconfig-encryptionconfig.md">EncryptionConfig</a></i>
<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>: <i>
      - <a href="clusterconfig-gceclusterconfig.md">GceClusterConfig</a></i>
<a href="#initializationaction" title="InitializationAction">InitializationAction</a>: <i>
      - <a href="clusterconfig-initializationaction.md">InitializationAction</a></i>
<a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - <a href="clusterconfig-masterconfig.md">MasterConfig</a></i>
<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>: <i>
      - <a href="clusterconfig-preemptibleworkerconfig.md">PreemptibleWorkerConfig</a></i>
<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>
      - <a href="clusterconfig-securityconfig.md">SecurityConfig</a></i>
<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - <a href="clusterconfig-softwareconfig.md">SoftwareConfig</a></i>
<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - <a href="clusterconfig-workerconfig.md">WorkerConfig</a></i>
</pre>

## Properties

#### StagingBucket

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingConfig

_Required_: No
_Type_: List of <a href="clusterconfig-autoscalingconfig.md">AutoscalingConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfig

_Required_: No
_Type_: List of <a href="clusterconfig-encryptionconfig.md">EncryptionConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GceClusterConfig

_Required_: No
_Type_: List of <a href="clusterconfig-gceclusterconfig.md">GceClusterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializationAction

_Required_: No
_Type_: List of <a href="clusterconfig-initializationaction.md">InitializationAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No
_Type_: List of <a href="clusterconfig-masterconfig.md">MasterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptibleWorkerConfig

_Required_: No
_Type_: List of <a href="clusterconfig-preemptibleworkerconfig.md">PreemptibleWorkerConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfig

_Required_: No
_Type_: List of <a href="clusterconfig-securityconfig.md">SecurityConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No
_Type_: List of <a href="clusterconfig-softwareconfig.md">SoftwareConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No
_Type_: List of <a href="clusterconfig-workerconfig.md">WorkerConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

