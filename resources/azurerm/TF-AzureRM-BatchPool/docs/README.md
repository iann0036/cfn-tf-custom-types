# TF::AzureRM::BatchPool

Manages an Azure Batch pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::BatchPool",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#maxtaskspernode" title="MaxTasksPerNode">MaxTasksPerNode</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodeagentskuid" title="NodeAgentSkuId">NodeAgentSkuId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#stoppendingresizeoperation" title="StopPendingResizeOperation">StopPendingResizeOperation</a>" : <i>Boolean</i>,
        "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
        "<a href="#autoscale" title="AutoScale">AutoScale</a>" : <i>[ <a href="autoscaledefinition.md">AutoScaleDefinition</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificatedefinition.md">CertificateDefinition</a>, ... ]</i>,
        "<a href="#containerconfiguration" title="ContainerConfiguration">ContainerConfiguration</a>" : <i>[ <a href="containerconfigurationdefinition.md">ContainerConfigurationDefinition</a>, ... ]</i>,
        "<a href="#fixedscale" title="FixedScale">FixedScale</a>" : <i>[ <a href="fixedscaledefinition.md">FixedScaleDefinition</a>, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>, ... ]</i>,
        "<a href="#starttask" title="StartTask">StartTask</a>" : <i>[ <a href="starttaskdefinition.md">StartTaskDefinition</a>, ... ]</i>,
        "<a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>" : <i>[ <a href="storageimagereferencedefinition.md">StorageImageReferenceDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::BatchPool
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#maxtaskspernode" title="MaxTasksPerNode">MaxTasksPerNode</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodeagentskuid" title="NodeAgentSkuId">NodeAgentSkuId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#stoppendingresizeoperation" title="StopPendingResizeOperation">StopPendingResizeOperation</a>: <i>Boolean</i>
    <a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
    <a href="#autoscale" title="AutoScale">AutoScale</a>: <i>
      - <a href="autoscaledefinition.md">AutoScaleDefinition</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificatedefinition.md">CertificateDefinition</a></i>
    <a href="#containerconfiguration" title="ContainerConfiguration">ContainerConfiguration</a>: <i>
      - <a href="containerconfigurationdefinition.md">ContainerConfigurationDefinition</a></i>
    <a href="#fixedscale" title="FixedScale">FixedScale</a>: <i>
      - <a href="fixedscaledefinition.md">FixedScaleDefinition</a></i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a></i>
    <a href="#starttask" title="StartTask">StartTask</a>: <i>
      - <a href="starttaskdefinition.md">StartTaskDefinition</a></i>
    <a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>: <i>
      - <a href="storageimagereferencedefinition.md">StorageImageReferenceDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccountName

Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Specifies the display name of the Batch pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTasksPerNode

Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to `1`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

A map of custom batch pool metadata.

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Batch pool. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAgentSkuId

Specifies the Sku of the node agents that will be created in the Batch pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopPendingResizeOperation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

Specifies the size of the VM created in the Batch pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScale

_Required_: No

_Type_: List of <a href="autoscaledefinition.md">AutoScaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificatedefinition.md">CertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerConfiguration

_Required_: No

_Type_: List of <a href="containerconfigurationdefinition.md">ContainerConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedScale

_Required_: No

_Type_: List of <a href="fixedscaledefinition.md">FixedScaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTask

_Required_: No

_Type_: List of <a href="starttaskdefinition.md">StartTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageImageReference

_Required_: No

_Type_: List of <a href="storageimagereferencedefinition.md">StorageImageReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

