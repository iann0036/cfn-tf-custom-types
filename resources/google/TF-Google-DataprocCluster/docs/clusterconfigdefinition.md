# TF::Google::DataprocCluster ClusterConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#stagingbucket" title="StagingBucket">StagingBucket</a>" : <i>String</i>,
    "<a href="#tempbucket" title="TempBucket">TempBucket</a>" : <i>String</i>,
    "<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>" : <i>[ <a href="autoscalingconfigdefinition.md">AutoscalingConfigDefinition</a>, ... ]</i>,
    "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ <a href="encryptionconfigdefinition.md">EncryptionConfigDefinition</a>, ... ]</i>,
    "<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>" : <i>[ <a href="gceclusterconfigdefinition.md">GceClusterConfigDefinition</a>, ... ]</i>,
    "<a href="#initializationaction" title="InitializationAction">InitializationAction</a>" : <i>[ <a href="initializationactiondefinition.md">InitializationActionDefinition</a>, ... ]</i>,
    "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ <a href="masterconfigdefinition.md">MasterConfigDefinition</a>, ... ]</i>,
    "<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>" : <i>[ <a href="preemptibleworkerconfigdefinition.md">PreemptibleWorkerConfigDefinition</a>, ... ]</i>,
    "<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>" : <i>[ <a href="securityconfigdefinition.md">SecurityConfigDefinition</a>, ... ]</i>,
    "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a>, ... ]</i>,
    "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ <a href="workerconfigdefinition.md">WorkerConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#stagingbucket" title="StagingBucket">StagingBucket</a>: <i>String</i>
<a href="#tempbucket" title="TempBucket">TempBucket</a>: <i>String</i>
<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>: <i>
      - <a href="autoscalingconfigdefinition.md">AutoscalingConfigDefinition</a></i>
<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>: <i>
      - <a href="encryptionconfigdefinition.md">EncryptionConfigDefinition</a></i>
<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>: <i>
      - <a href="gceclusterconfigdefinition.md">GceClusterConfigDefinition</a></i>
<a href="#initializationaction" title="InitializationAction">InitializationAction</a>: <i>
      - <a href="initializationactiondefinition.md">InitializationActionDefinition</a></i>
<a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - <a href="masterconfigdefinition.md">MasterConfigDefinition</a></i>
<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>: <i>
      - <a href="preemptibleworkerconfigdefinition.md">PreemptibleWorkerConfigDefinition</a></i>
<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>
      - <a href="securityconfigdefinition.md">SecurityConfigDefinition</a></i>
<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a></i>
<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - <a href="workerconfigdefinition.md">WorkerConfigDefinition</a></i>
</pre>

## Properties

#### StagingBucket

The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don't explicitly specify a `staging_bucket`
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TempBucket

The Cloud Storage temp bucket used to store ephemeral cluster
and jobs data, such as Spark and MapReduce history files.
Note: If you don't explicitly specify a `temp_bucket` then GCP will auto create / assign one for you.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingConfig

_Required_: No

_Type_: List of <a href="autoscalingconfigdefinition.md">AutoscalingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfig

_Required_: No

_Type_: List of <a href="encryptionconfigdefinition.md">EncryptionConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GceClusterConfig

_Required_: No

_Type_: List of <a href="gceclusterconfigdefinition.md">GceClusterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializationAction

_Required_: No

_Type_: List of <a href="initializationactiondefinition.md">InitializationActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No

_Type_: List of <a href="masterconfigdefinition.md">MasterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptibleWorkerConfig

_Required_: No

_Type_: List of <a href="preemptibleworkerconfigdefinition.md">PreemptibleWorkerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfig

_Required_: No

_Type_: List of <a href="securityconfigdefinition.md">SecurityConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No

_Type_: List of <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of <a href="workerconfigdefinition.md">WorkerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

