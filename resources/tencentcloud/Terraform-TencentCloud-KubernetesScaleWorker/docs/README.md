# Terraform::TencentCloud::KubernetesScaleWorker

CloudFormation equivalent of tencentcloud_kubernetes_scale_worker

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::KubernetesScaleWorker",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#workerinstanceslist" title="WorkerInstancesList">WorkerInstancesList</a>" : <i>[ &lt;a href=&#34;workerinstanceslist.md&#34;&gt;WorkerInstancesList&lt;/a&gt;, ... ]</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ &lt;a href=&#34;datadisk.md&#34;&gt;DataDisk&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::KubernetesScaleWorker
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#workerinstanceslist" title="WorkerInstancesList">WorkerInstancesList</a>: <i>
      - &lt;a href=&#34;workerinstanceslist.md&#34;&gt;WorkerInstancesList&lt;/a&gt;</i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;</i>
    <a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - &lt;a href=&#34;datadisk.md&#34;&gt;DataDisk&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerInstancesList

_Required_: No

_Type_: List of &lt;a href=&#34;workerinstanceslist.md&#34;&gt;WorkerInstancesList&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of &lt;a href=&#34;datadisk.md&#34;&gt;DataDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### WorkerInstancesList

Returns the &lt;code&gt;WorkerInstancesList&lt;/code&gt; value.

