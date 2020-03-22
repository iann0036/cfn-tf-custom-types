# Terraform::Google::DataprocCluster

Manages a Cloud Dataproc cluster resource within GCP. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).


!> **Warning:** Due to limitations of the API, all arguments except
`labels`,`cluster_config.worker_config.num_instances` and `cluster_config.preemptible_worker_config.num_instances` are non-updatable. Changing others will cause recreation of the
whole cluster!

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::DataprocCluster",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>" : <i>[ <a href="clusterconfig.md">ClusterConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>" : <i>[ <a href="autoscalingconfig.md">AutoscalingConfig</a>, ... ]</i>,
        "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ <a href="encryptionconfig.md">EncryptionConfig</a>, ... ]</i>,
        "<a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>" : <i>[ <a href="gceclusterconfig.md">GceClusterConfig</a>, ... ]</i>,
        "<a href="#initializationaction" title="InitializationAction">InitializationAction</a>" : <i>[ <a href="initializationaction.md">InitializationAction</a>, ... ]</i>,
        "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ <a href="masterconfig.md">MasterConfig</a>, ... ]</i>,
        "<a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>" : <i>[ <a href="preemptibleworkerconfig.md">PreemptibleWorkerConfig</a>, ... ]</i>,
        "<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>" : <i>[ <a href="securityconfig.md">SecurityConfig</a>, ... ]</i>,
        "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ <a href="softwareconfig.md">SoftwareConfig</a>, ... ]</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ <a href="workerconfig.md">WorkerConfig</a>, ... ]</i>,
        "<a href="#accelerators" title="Accelerators">Accelerators</a>" : <i>[ <a href="accelerators.md">Accelerators</a>, ... ]</i>,
        "<a href="#diskconfig" title="DiskConfig">DiskConfig</a>" : <i>[ <a href="diskconfig.md">DiskConfig</a>, ... ]</i>,
        "<a href="#kerberosconfig" title="KerberosConfig">KerberosConfig</a>" : <i>[ <a href="kerberosconfig.md">KerberosConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::DataprocCluster
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>: <i>
      - <a href="clusterconfig.md">ClusterConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#autoscalingconfig" title="AutoscalingConfig">AutoscalingConfig</a>: <i>
      - <a href="autoscalingconfig.md">AutoscalingConfig</a></i>
    <a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>: <i>
      - <a href="encryptionconfig.md">EncryptionConfig</a></i>
    <a href="#gceclusterconfig" title="GceClusterConfig">GceClusterConfig</a>: <i>
      - <a href="gceclusterconfig.md">GceClusterConfig</a></i>
    <a href="#initializationaction" title="InitializationAction">InitializationAction</a>: <i>
      - <a href="initializationaction.md">InitializationAction</a></i>
    <a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - <a href="masterconfig.md">MasterConfig</a></i>
    <a href="#preemptibleworkerconfig" title="PreemptibleWorkerConfig">PreemptibleWorkerConfig</a>: <i>
      - <a href="preemptibleworkerconfig.md">PreemptibleWorkerConfig</a></i>
    <a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>
      - <a href="securityconfig.md">SecurityConfig</a></i>
    <a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - <a href="softwareconfig.md">SoftwareConfig</a></i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - <a href="workerconfig.md">WorkerConfig</a></i>
    <a href="#accelerators" title="Accelerators">Accelerators</a>: <i>
      - <a href="accelerators.md">Accelerators</a></i>
    <a href="#diskconfig" title="DiskConfig">DiskConfig</a>: <i>
      - <a href="diskconfig.md">DiskConfig</a></i>
    <a href="#kerberosconfig" title="KerberosConfig">KerberosConfig</a>: <i>
      - <a href="kerberosconfig.md">KerberosConfig</a></i>
</pre>

## Properties

#### Labels

The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the cluster, unique within the project and
zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which the cluster and associated nodes will be created in.
Defaults to `global`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterConfig

_Required_: No

_Type_: List of <a href="clusterconfig.md">ClusterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingConfig

_Required_: No

_Type_: List of <a href="autoscalingconfig.md">AutoscalingConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfig

_Required_: No

_Type_: List of <a href="encryptionconfig.md">EncryptionConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GceClusterConfig

_Required_: No

_Type_: List of <a href="gceclusterconfig.md">GceClusterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializationAction

_Required_: No

_Type_: List of <a href="initializationaction.md">InitializationAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No

_Type_: List of <a href="masterconfig.md">MasterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptibleWorkerConfig

_Required_: No

_Type_: List of <a href="preemptibleworkerconfig.md">PreemptibleWorkerConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfig

_Required_: No

_Type_: List of <a href="securityconfig.md">SecurityConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No

_Type_: List of <a href="softwareconfig.md">SoftwareConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of <a href="workerconfig.md">WorkerConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Accelerators

_Required_: No

_Type_: List of <a href="accelerators.md">Accelerators</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskConfig

_Required_: No

_Type_: List of <a href="diskconfig.md">DiskConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KerberosConfig

_Required_: No

_Type_: List of <a href="kerberosconfig.md">KerberosConfig</a>

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

