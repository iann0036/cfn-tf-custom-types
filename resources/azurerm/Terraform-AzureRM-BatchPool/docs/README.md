# Terraform::AzureRM::BatchPool

CloudFormation equivalent of azurerm_batch_pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::BatchPool",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#maxtaskspernode" title="MaxTasksPerNode">MaxTasksPerNode</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodeagentskuid" title="NodeAgentSkuId">NodeAgentSkuId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#stoppendingresizeoperation" title="StopPendingResizeOperation">StopPendingResizeOperation</a>" : <i>Boolean</i>,
        "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
        "<a href="#autoscale" title="AutoScale">AutoScale</a>" : <i>[ &lt;a href=&#34;autoscale.md&#34;&gt;AutoScale&lt;/a&gt;, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;, ... ]</i>,
        "<a href="#containerconfiguration" title="ContainerConfiguration">ContainerConfiguration</a>" : <i>[ &lt;a href=&#34;containerconfiguration.md&#34;&gt;ContainerConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#fixedscale" title="FixedScale">FixedScale</a>" : <i>[ &lt;a href=&#34;fixedscale.md&#34;&gt;FixedScale&lt;/a&gt;, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#starttask" title="StartTask">StartTask</a>" : <i>[ &lt;a href=&#34;starttask.md&#34;&gt;StartTask&lt;/a&gt;, ... ]</i>,
        "<a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>" : <i>[ &lt;a href=&#34;storageimagereference.md&#34;&gt;StorageImageReference&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>" : <i>[ &lt;a href=&#34;endpointconfiguration.md&#34;&gt;EndpointConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#resourcefile" title="ResourceFile">ResourceFile</a>" : <i>[ &lt;a href=&#34;resourcefile.md&#34;&gt;ResourceFile&lt;/a&gt;, ... ]</i>,
        "<a href="#useridentity" title="UserIdentity">UserIdentity</a>" : <i>[ &lt;a href=&#34;useridentity.md&#34;&gt;UserIdentity&lt;/a&gt;, ... ]</i>,
        "<a href="#networksecuritygrouprules" title="NetworkSecurityGroupRules">NetworkSecurityGroupRules</a>" : <i>[ &lt;a href=&#34;networksecuritygrouprules.md&#34;&gt;NetworkSecurityGroupRules&lt;/a&gt;, ... ]</i>,
        "<a href="#autouser" title="AutoUser">AutoUser</a>" : <i>[ &lt;a href=&#34;autouser.md&#34;&gt;AutoUser&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::BatchPool
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#maxtaskspernode" title="MaxTasksPerNode">MaxTasksPerNode</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodeagentskuid" title="NodeAgentSkuId">NodeAgentSkuId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#stoppendingresizeoperation" title="StopPendingResizeOperation">StopPendingResizeOperation</a>: <i>Boolean</i>
    <a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
    <a href="#autoscale" title="AutoScale">AutoScale</a>: <i>
      - &lt;a href=&#34;autoscale.md&#34;&gt;AutoScale&lt;/a&gt;</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;</i>
    <a href="#containerconfiguration" title="ContainerConfiguration">ContainerConfiguration</a>: <i>
      - &lt;a href=&#34;containerconfiguration.md&#34;&gt;ContainerConfiguration&lt;/a&gt;</i>
    <a href="#fixedscale" title="FixedScale">FixedScale</a>: <i>
      - &lt;a href=&#34;fixedscale.md&#34;&gt;FixedScale&lt;/a&gt;</i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;</i>
    <a href="#starttask" title="StartTask">StartTask</a>: <i>
      - &lt;a href=&#34;starttask.md&#34;&gt;StartTask&lt;/a&gt;</i>
    <a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>: <i>
      - &lt;a href=&#34;storageimagereference.md&#34;&gt;StorageImageReference&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>: <i>
      - &lt;a href=&#34;endpointconfiguration.md&#34;&gt;EndpointConfiguration&lt;/a&gt;</i>
    <a href="#resourcefile" title="ResourceFile">ResourceFile</a>: <i>
      - &lt;a href=&#34;resourcefile.md&#34;&gt;ResourceFile&lt;/a&gt;</i>
    <a href="#useridentity" title="UserIdentity">UserIdentity</a>: <i>
      - &lt;a href=&#34;useridentity.md&#34;&gt;UserIdentity&lt;/a&gt;</i>
    <a href="#networksecuritygrouprules" title="NetworkSecurityGroupRules">NetworkSecurityGroupRules</a>: <i>
      - &lt;a href=&#34;networksecuritygrouprules.md&#34;&gt;NetworkSecurityGroupRules&lt;/a&gt;</i>
    <a href="#autouser" title="AutoUser">AutoUser</a>: <i>
      - &lt;a href=&#34;autouser.md&#34;&gt;AutoUser&lt;/a&gt;</i>
</pre>

## Properties

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTasksPerNode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAgentSkuId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopPendingResizeOperation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScale

_Required_: No

_Type_: List of &lt;a href=&#34;autoscale.md&#34;&gt;AutoScale&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;containerconfiguration.md&#34;&gt;ContainerConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedScale

_Required_: No

_Type_: List of &lt;a href=&#34;fixedscale.md&#34;&gt;FixedScale&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTask

_Required_: No

_Type_: List of &lt;a href=&#34;starttask.md&#34;&gt;StartTask&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageImageReference

_Required_: No

_Type_: List of &lt;a href=&#34;storageimagereference.md&#34;&gt;StorageImageReference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;endpointconfiguration.md&#34;&gt;EndpointConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFile

_Required_: No

_Type_: List of &lt;a href=&#34;resourcefile.md&#34;&gt;ResourceFile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentity

_Required_: No

_Type_: List of &lt;a href=&#34;useridentity.md&#34;&gt;UserIdentity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupRules

_Required_: No

_Type_: List of &lt;a href=&#34;networksecuritygrouprules.md&#34;&gt;NetworkSecurityGroupRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoUser

_Required_: No

_Type_: List of &lt;a href=&#34;autouser.md&#34;&gt;AutoUser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

