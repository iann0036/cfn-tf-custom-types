# TF::GoogleBeta::GoogleContainerCluster KubeletConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cpucfsquota" title="CpuCfsQuota">CpuCfsQuota</a>" : <i>Boolean</i>,
    "<a href="#cpucfsquotaperiod" title="CpuCfsQuotaPeriod">CpuCfsQuotaPeriod</a>" : <i>String</i>,
    "<a href="#cpumanagerpolicy" title="CpuManagerPolicy">CpuManagerPolicy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cpucfsquota" title="CpuCfsQuota">CpuCfsQuota</a>: <i>Boolean</i>
<a href="#cpucfsquotaperiod" title="CpuCfsQuotaPeriod">CpuCfsQuotaPeriod</a>: <i>String</i>
<a href="#cpumanagerpolicy" title="CpuManagerPolicy">CpuManagerPolicy</a>: <i>String</i>
</pre>

## Properties

#### CpuCfsQuota

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCfsQuotaPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuManagerPolicy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

