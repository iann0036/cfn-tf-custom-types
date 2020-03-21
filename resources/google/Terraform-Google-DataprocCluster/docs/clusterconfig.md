# Terraform::Google::DataprocCluster ClusterConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#stagingbucket" title="StagingBucket">StagingBucket</a>" : <i>String</i>,
    "<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-autoscalingconfig.md&#34;&gt;AutoscalingConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-encryptionconfig.md&#34;&gt;EncryptionConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-gceclusterconfig.md&#34;&gt;GceClusterConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#initializationaction" title="InitializationAction">InitializationAction</a>" : <i>[ &lt;a href=&#34;clusterconfig-initializationaction.md&#34;&gt;InitializationAction&lt;/a&gt;, ... ]</i>,
    "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-preemptibleworkerconfig.md&#34;&gt;PreemptibleWorkerConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-securityconfig.md&#34;&gt;SecurityConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig-workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#stagingbucket" title="StagingBucket">StagingBucket</a>: <i>String</i>
<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-autoscalingconfig.md&#34;&gt;AutoscalingConfig&lt;/a&gt;</i>
<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-encryptionconfig.md&#34;&gt;EncryptionConfig&lt;/a&gt;</i>
<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-gceclusterconfig.md&#34;&gt;GceClusterConfig&lt;/a&gt;</i>
<a href="#initializationaction" title="InitializationAction">InitializationAction</a>: <i>
      - &lt;a href=&#34;clusterconfig-initializationaction.md&#34;&gt;InitializationAction&lt;/a&gt;</i>
<a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;</i>
<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-preemptibleworkerconfig.md&#34;&gt;PreemptibleWorkerConfig&lt;/a&gt;</i>
<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-securityconfig.md&#34;&gt;SecurityConfig&lt;/a&gt;</i>
<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;</i>
<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig-workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;</i>
</pre>

## Properties

#### StagingBucket

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-autoscalingconfig.md&#34;&gt;AutoscalingConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-encryptionconfig.md&#34;&gt;EncryptionConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GceClusterConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-gceclusterconfig.md&#34;&gt;GceClusterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializationAction

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-initializationaction.md&#34;&gt;InitializationAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptibleWorkerConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-preemptibleworkerconfig.md&#34;&gt;PreemptibleWorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-securityconfig.md&#34;&gt;SecurityConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No
_Type_: List of &lt;a href=&#34;clusterconfig-workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

