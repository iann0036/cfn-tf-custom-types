# TF::Google::NotebooksInstance

A Cloud AI Platform Notebook instance.


~> **Note:** Due to limitations of the Notebooks Instance API, many fields
in this resource do not properly detect drift. These fields will also not
appear in state once imported.


To get more information about Instance, see:

* [API documentation](https://cloud.google.com/ai-platform/notebooks/docs/reference/rest)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/ai-platform-notebooks)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=notebook_instance_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32p...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::NotebooksInstance",
    "Properties" : {
        "<a href="#bootdisksizegb" title="BootDiskSizeGb">BootDiskSizeGb</a>" : <i>Double</i>,
        "<a href="#bootdisktype" title="BootDiskType">BootDiskType</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#customgpudriverpath" title="CustomGpuDriverPath">CustomGpuDriverPath</a>" : <i>String</i>,
        "<a href="#datadisksizegb" title="DataDiskSizeGb">DataDiskSizeGb</a>" : <i>Double</i>,
        "<a href="#datadisktype" title="DataDiskType">DataDiskType</a>" : <i>String</i>,
        "<a href="#diskencryption" title="DiskEncryption">DiskEncryption</a>" : <i>String</i>,
        "<a href="#installgpudriver" title="InstallGpuDriver">InstallGpuDriver</a>" : <i>Boolean</i>,
        "<a href="#instanceowners" title="InstanceOwners">InstanceOwners</a>" : <i>[ String, ... ]</i>,
        "<a href="#kmskey" title="KmsKey">KmsKey</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#noproxyaccess" title="NoProxyAccess">NoProxyAccess</a>" : <i>Boolean</i>,
        "<a href="#nopublicip" title="NoPublicIp">NoPublicIp</a>" : <i>Boolean</i>,
        "<a href="#noremovedatadisk" title="NoRemoveDataDisk">NoRemoveDataDisk</a>" : <i>Boolean</i>,
        "<a href="#poststartupscript" title="PostStartupScript">PostStartupScript</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
        "<a href="#serviceaccountscopes" title="ServiceAccountScopes">ServiceAccountScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#updatetime" title="UpdateTime">UpdateTime</a>" : <i>String</i>,
        "<a href="#acceleratorconfig" title="AcceleratorConfig">AcceleratorConfig</a>" : <i>[ <a href="acceleratorconfigdefinition.md">AcceleratorConfigDefinition</a>, ... ]</i>,
        "<a href="#containerimage" title="ContainerImage">ContainerImage</a>" : <i>[ <a href="containerimagedefinition.md">ContainerImageDefinition</a>, ... ]</i>,
        "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vmimage" title="VmImage">VmImage</a>" : <i>[ <a href="vmimagedefinition.md">VmImageDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::NotebooksInstance
Properties:
    <a href="#bootdisksizegb" title="BootDiskSizeGb">BootDiskSizeGb</a>: <i>Double</i>
    <a href="#bootdisktype" title="BootDiskType">BootDiskType</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#customgpudriverpath" title="CustomGpuDriverPath">CustomGpuDriverPath</a>: <i>String</i>
    <a href="#datadisksizegb" title="DataDiskSizeGb">DataDiskSizeGb</a>: <i>Double</i>
    <a href="#datadisktype" title="DataDiskType">DataDiskType</a>: <i>String</i>
    <a href="#diskencryption" title="DiskEncryption">DiskEncryption</a>: <i>String</i>
    <a href="#installgpudriver" title="InstallGpuDriver">InstallGpuDriver</a>: <i>Boolean</i>
    <a href="#instanceowners" title="InstanceOwners">InstanceOwners</a>: <i>
      - String</i>
    <a href="#kmskey" title="KmsKey">KmsKey</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#noproxyaccess" title="NoProxyAccess">NoProxyAccess</a>: <i>Boolean</i>
    <a href="#nopublicip" title="NoPublicIp">NoPublicIp</a>: <i>Boolean</i>
    <a href="#noremovedatadisk" title="NoRemoveDataDisk">NoRemoveDataDisk</a>: <i>Boolean</i>
    <a href="#poststartupscript" title="PostStartupScript">PostStartupScript</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
    <a href="#serviceaccountscopes" title="ServiceAccountScopes">ServiceAccountScopes</a>: <i>
      - String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#updatetime" title="UpdateTime">UpdateTime</a>: <i>String</i>
    <a href="#acceleratorconfig" title="AcceleratorConfig">AcceleratorConfig</a>: <i>
      - <a href="acceleratorconfigdefinition.md">AcceleratorConfigDefinition</a></i>
    <a href="#containerimage" title="ContainerImage">ContainerImage</a>: <i>
      - <a href="containerimagedefinition.md">ContainerImageDefinition</a></i>
    <a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vmimage" title="VmImage">VmImage</a>: <i>
      - <a href="vmimagedefinition.md">VmImageDefinition</a></i>
</pre>

## Properties

#### BootDiskSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiskType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomGpuDriverPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallGpuDriver

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceOwners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoProxyAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoPublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoRemoveDataDisk

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostStartupScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountScopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcceleratorConfig

_Required_: No

_Type_: List of <a href="acceleratorconfigdefinition.md">AcceleratorConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerImage

_Required_: No

_Type_: List of <a href="containerimagedefinition.md">ContainerImageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmImage

_Required_: No

_Type_: List of <a href="vmimagedefinition.md">VmImageDefinition</a>

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

#### ProxyUri

Returns the <code>ProxyUri</code> value.

#### State

Returns the <code>State</code> value.

