# Terraform::Google::DataprocCluster

CloudFormation equivalent of google_dataproc_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::DataprocCluster",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig.md&#34;&gt;ClusterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>" : <i>[ &lt;a href=&#34;autoscalingconfig.md&#34;&gt;AutoscalingConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ &lt;a href=&#34;encryptionconfig.md&#34;&gt;EncryptionConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>" : <i>[ &lt;a href=&#34;gceclusterconfig.md&#34;&gt;GceClusterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#initializationaction" title="InitializationAction">InitializationAction</a>" : <i>[ &lt;a href=&#34;initializationaction.md&#34;&gt;InitializationAction&lt;/a&gt;, ... ]</i>,
        "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ &lt;a href=&#34;masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>" : <i>[ &lt;a href=&#34;preemptibleworkerconfig.md&#34;&gt;PreemptibleWorkerConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>" : <i>[ &lt;a href=&#34;securityconfig.md&#34;&gt;SecurityConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ &lt;a href=&#34;softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#accelerators" title="Accelerators">Accelerators</a>" : <i>[ &lt;a href=&#34;accelerators.md&#34;&gt;Accelerators&lt;/a&gt;, ... ]</i>,
        "<a href="#diskconfig" title="DiskConfig">DiskConfig</a>" : <i>[ &lt;a href=&#34;diskconfig.md&#34;&gt;DiskConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#kerberosconfig" title="KerberosConfig">KerberosConfig</a>" : <i>[ &lt;a href=&#34;kerberosconfig.md&#34;&gt;KerberosConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::DataprocCluster
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig.md&#34;&gt;ClusterConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>: <i>
      - &lt;a href=&#34;autoscalingconfig.md&#34;&gt;AutoscalingConfig&lt;/a&gt;</i>
    <a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>: <i>
      - &lt;a href=&#34;encryptionconfig.md&#34;&gt;EncryptionConfig&lt;/a&gt;</i>
    <a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>: <i>
      - &lt;a href=&#34;gceclusterconfig.md&#34;&gt;GceClusterConfig&lt;/a&gt;</i>
    <a href="#initializationaction" title="InitializationAction">InitializationAction</a>: <i>
      - &lt;a href=&#34;initializationaction.md&#34;&gt;InitializationAction&lt;/a&gt;</i>
    <a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - &lt;a href=&#34;masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;</i>
    <a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>: <i>
      - &lt;a href=&#34;preemptibleworkerconfig.md&#34;&gt;PreemptibleWorkerConfig&lt;/a&gt;</i>
    <a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>
      - &lt;a href=&#34;securityconfig.md&#34;&gt;SecurityConfig&lt;/a&gt;</i>
    <a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - &lt;a href=&#34;softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;</i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;</i>
    <a href="#accelerators" title="Accelerators">Accelerators</a>: <i>
      - &lt;a href=&#34;accelerators.md&#34;&gt;Accelerators&lt;/a&gt;</i>
    <a href="#diskconfig" title="DiskConfig">DiskConfig</a>: <i>
      - &lt;a href=&#34;diskconfig.md&#34;&gt;DiskConfig&lt;/a&gt;</i>
    <a href="#kerberosconfig" title="KerberosConfig">KerberosConfig</a>: <i>
      - &lt;a href=&#34;kerberosconfig.md&#34;&gt;KerberosConfig&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;clusterconfig.md&#34;&gt;ClusterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingConfig

_Required_: No

_Type_: List of &lt;a href=&#34;autoscalingconfig.md&#34;&gt;AutoscalingConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfig

_Required_: No

_Type_: List of &lt;a href=&#34;encryptionconfig.md&#34;&gt;EncryptionConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GceClusterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;gceclusterconfig.md&#34;&gt;GceClusterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializationAction

_Required_: No

_Type_: List of &lt;a href=&#34;initializationaction.md&#34;&gt;InitializationAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptibleWorkerConfig

_Required_: No

_Type_: List of &lt;a href=&#34;preemptibleworkerconfig.md&#34;&gt;PreemptibleWorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfig

_Required_: No

_Type_: List of &lt;a href=&#34;securityconfig.md&#34;&gt;SecurityConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No

_Type_: List of &lt;a href=&#34;softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Accelerators

_Required_: No

_Type_: List of &lt;a href=&#34;accelerators.md&#34;&gt;Accelerators&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskConfig

_Required_: No

_Type_: List of &lt;a href=&#34;diskconfig.md&#34;&gt;DiskConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KerberosConfig

_Required_: No

_Type_: List of &lt;a href=&#34;kerberosconfig.md&#34;&gt;KerberosConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

