# Terraform::TencentCloud::KubernetesAsScalingGroup AutoScalingConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>" : <i>String</i>,
    "<a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>" : <i>Boolean</i>,
    "<a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>" : <i>Boolean</i>,
    "<a href="#instancetags" title="InstanceTags">InstanceTags</a>" : <i>[ &lt;a href=&#34;autoscalingconfig-instancetags.md&#34;&gt;InstanceTags&lt;/a&gt;, ... ]</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
    "<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>" : <i>Double</i>,
    "<a href="#keyids" title="KeyIds">KeyIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
    "<a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>" : <i>Boolean</i>,
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>" : <i>Double</i>,
    "<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>" : <i>String</i>,
    "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ &lt;a href=&#34;autoscalingconfig-datadisk.md&#34;&gt;DataDisk&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>: <i>String</i>
<a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>: <i>Boolean</i>
<a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>: <i>Boolean</i>
<a href="#instancetags" title="InstanceTags">InstanceTags</a>: <i>
      - &lt;a href=&#34;autoscalingconfig-instancetags.md&#34;&gt;InstanceTags&lt;/a&gt;</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>: <i>Double</i>
<a href="#keyids" title="KeyIds">KeyIds</a>: <i>
      - String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
<a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>: <i>Boolean</i>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>: <i>Double</i>
<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>: <i>String</i>
<a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - &lt;a href=&#34;autoscalingconfig-datadisk.md&#34;&gt;DataDisk&lt;/a&gt;</i>
</pre>

## Properties

#### ConfigurationName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedMonitorService

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedSecurityService

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTags

_Required_: No
_Type_: List of &lt;a href=&#34;autoscalingconfig-instancetags.md&#34;&gt;InstanceTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthOut

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAssigned

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskSize

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No
_Type_: List of &lt;a href=&#34;autoscalingconfig-datadisk.md&#34;&gt;DataDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

