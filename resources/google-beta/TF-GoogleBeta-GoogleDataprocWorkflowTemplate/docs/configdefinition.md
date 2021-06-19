# TF::GoogleBeta::GoogleDataprocWorkflowTemplate ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#stagingbucket" title="StagingBucket">StagingBucket</a>" : <i>String</i>,
    "<a href="#tempbucket" title="TempBucket">TempBucket</a>" : <i>String</i>,
    "<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>" : <i>[ <a href="autoscalingconfigdefinition.md">AutoscalingConfigDefinition</a>, ... ]</i>,
    "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ <a href="encryptionconfigdefinition.md">EncryptionConfigDefinition</a>, ... ]</i>,
    "<a href="#endpointconfig" title="EndpointConfig">EndpointConfig</a>" : <i>[ <a href="endpointconfigdefinition.md">EndpointConfigDefinition</a>, ... ]</i>,
    "<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>" : <i>[ <a href="gceclusterconfigdefinition.md">GceClusterConfigDefinition</a>, ... ]</i>,
    "<a href="#gkeclusterconfig" title="GkeClusterConfig">GkeClusterConfig</a>" : <i>[ <a href="gkeclusterconfigdefinition.md">GkeClusterConfigDefinition</a>, ... ]</i>,
    "<a href="#initializationactions" title="InitializationActions">InitializationActions</a>" : <i>[ <a href="initializationactionsdefinition.md">InitializationActionsDefinition</a>, ... ]</i>,
    "<a href="#lifecycleconfig" title="LifecycleConfig">LifecycleConfig</a>" : <i>[ <a href="lifecycleconfigdefinition.md">LifecycleConfigDefinition</a>, ... ]</i>,
    "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ <a href="masterconfigdefinition.md">MasterConfigDefinition</a>, ... ]</i>,
    "<a href="#metastoreconfig" title="MetastoreConfig">MetastoreConfig</a>" : <i>[ <a href="metastoreconfigdefinition.md">MetastoreConfigDefinition</a>, ... ]</i>,
    "<a href="#secondaryworkerconfig" title="SecondaryWorkerConfig">SecondaryWorkerConfig</a>" : <i>[ <a href="secondaryworkerconfigdefinition.md">SecondaryWorkerConfigDefinition</a>, ... ]</i>,
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
<a href="#endpointconfig" title="EndpointConfig">EndpointConfig</a>: <i>
      - <a href="endpointconfigdefinition.md">EndpointConfigDefinition</a></i>
<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>: <i>
      - <a href="gceclusterconfigdefinition.md">GceClusterConfigDefinition</a></i>
<a href="#gkeclusterconfig" title="GkeClusterConfig">GkeClusterConfig</a>: <i>
      - <a href="gkeclusterconfigdefinition.md">GkeClusterConfigDefinition</a></i>
<a href="#initializationactions" title="InitializationActions">InitializationActions</a>: <i>
      - <a href="initializationactionsdefinition.md">InitializationActionsDefinition</a></i>
<a href="#lifecycleconfig" title="LifecycleConfig">LifecycleConfig</a>: <i>
      - <a href="lifecycleconfigdefinition.md">LifecycleConfigDefinition</a></i>
<a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - <a href="masterconfigdefinition.md">MasterConfigDefinition</a></i>
<a href="#metastoreconfig" title="MetastoreConfig">MetastoreConfig</a>: <i>
      - <a href="metastoreconfigdefinition.md">MetastoreConfigDefinition</a></i>
<a href="#secondaryworkerconfig" title="SecondaryWorkerConfig">SecondaryWorkerConfig</a>: <i>
      - <a href="secondaryworkerconfigdefinition.md">SecondaryWorkerConfigDefinition</a></i>
<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>
      - <a href="securityconfigdefinition.md">SecurityConfigDefinition</a></i>
<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a></i>
<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - <a href="workerconfigdefinition.md">WorkerConfigDefinition</a></i>
</pre>

## Properties

#### StagingBucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TempBucket

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

#### EndpointConfig

_Required_: No

_Type_: List of <a href="endpointconfigdefinition.md">EndpointConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GceClusterConfig

_Required_: No

_Type_: List of <a href="gceclusterconfigdefinition.md">GceClusterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GkeClusterConfig

_Required_: No

_Type_: List of <a href="gkeclusterconfigdefinition.md">GkeClusterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializationActions

_Required_: No

_Type_: List of <a href="initializationactionsdefinition.md">InitializationActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleConfig

_Required_: No

_Type_: List of <a href="lifecycleconfigdefinition.md">LifecycleConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No

_Type_: List of <a href="masterconfigdefinition.md">MasterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetastoreConfig

_Required_: No

_Type_: List of <a href="metastoreconfigdefinition.md">MetastoreConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryWorkerConfig

_Required_: No

_Type_: List of <a href="secondaryworkerconfigdefinition.md">SecondaryWorkerConfigDefinition</a>

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

