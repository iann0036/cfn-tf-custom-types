# TF::Rancher2::PodSecurityPolicyTemplate

Provides a Rancher v2 PodSecurityPolicyTemplate resource. This can be used to create PodSecurityPolicyTemplates for Rancher v2 environments and retrieve their information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::PodSecurityPolicyTemplate",
    "Properties" : {
        "<a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>" : <i>Boolean</i>,
        "<a href="#allowedcapabilities" title="AllowedCapabilities">AllowedCapabilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowedprocmounttypes" title="AllowedProcMountTypes">AllowedProcMountTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>" : <i>[ String, ... ]</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#defaultaddcapabilities" title="DefaultAddCapabilities">DefaultAddCapabilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultallowprivilegeescalation" title="DefaultAllowPrivilegeEscalation">DefaultAllowPrivilegeEscalation</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#forbiddensysctls" title="ForbiddenSysctls">ForbiddenSysctls</a>" : <i>[ String, ... ]</i>,
        "<a href="#hostipc" title="HostIpc">HostIpc</a>" : <i>Boolean</i>,
        "<a href="#hostnetwork" title="HostNetwork">HostNetwork</a>" : <i>Boolean</i>,
        "<a href="#hostpid" title="HostPid">HostPid</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privileged" title="Privileged">Privileged</a>" : <i>Boolean</i>,
        "<a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>" : <i>Boolean</i>,
        "<a href="#requireddropcapabilities" title="RequiredDropCapabilities">RequiredDropCapabilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowedcsidriver" title="AllowedCsiDriver">AllowedCsiDriver</a>" : <i>[ <a href="allowedcsidriverdefinition.md">AllowedCsiDriverDefinition</a>, ... ]</i>,
        "<a href="#allowedflexvolume" title="AllowedFlexVolume">AllowedFlexVolume</a>" : <i>[ <a href="allowedflexvolumedefinition.md">AllowedFlexVolumeDefinition</a>, ... ]</i>,
        "<a href="#allowedhostpath" title="AllowedHostPath">AllowedHostPath</a>" : <i>[ <a href="allowedhostpathdefinition.md">AllowedHostPathDefinition</a>, ... ]</i>,
        "<a href="#fsgroup" title="FsGroup">FsGroup</a>" : <i>[ <a href="fsgroupdefinition.md">FsGroupDefinition</a>, ... ]</i>,
        "<a href="#hostport" title="HostPort">HostPort</a>" : <i>[ <a href="hostportdefinition.md">HostPortDefinition</a>, ... ]</i>,
        "<a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>" : <i>[ <a href="runasgroupdefinition.md">RunAsGroupDefinition</a>, ... ]</i>,
        "<a href="#runasuser" title="RunAsUser">RunAsUser</a>" : <i>[ <a href="runasuserdefinition.md">RunAsUserDefinition</a>, ... ]</i>,
        "<a href="#runtimeclass" title="RuntimeClass">RuntimeClass</a>" : <i>[ <a href="runtimeclassdefinition.md">RuntimeClassDefinition</a>, ... ]</i>,
        "<a href="#selinux" title="SeLinux">SeLinux</a>" : <i>[ <a href="selinuxdefinition.md">SeLinuxDefinition</a>, ... ]</i>,
        "<a href="#supplementalgroup" title="SupplementalGroup">SupplementalGroup</a>" : <i>[ <a href="supplementalgroupdefinition.md">SupplementalGroupDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::PodSecurityPolicyTemplate
Properties:
    <a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>: <i>Boolean</i>
    <a href="#allowedcapabilities" title="AllowedCapabilities">AllowedCapabilities</a>: <i>
      - String</i>
    <a href="#allowedprocmounttypes" title="AllowedProcMountTypes">AllowedProcMountTypes</a>: <i>
      - String</i>
    <a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>: <i>
      - String</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#defaultaddcapabilities" title="DefaultAddCapabilities">DefaultAddCapabilities</a>: <i>
      - String</i>
    <a href="#defaultallowprivilegeescalation" title="DefaultAllowPrivilegeEscalation">DefaultAllowPrivilegeEscalation</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#forbiddensysctls" title="ForbiddenSysctls">ForbiddenSysctls</a>: <i>
      - String</i>
    <a href="#hostipc" title="HostIpc">HostIpc</a>: <i>Boolean</i>
    <a href="#hostnetwork" title="HostNetwork">HostNetwork</a>: <i>Boolean</i>
    <a href="#hostpid" title="HostPid">HostPid</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privileged" title="Privileged">Privileged</a>: <i>Boolean</i>
    <a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>: <i>Boolean</i>
    <a href="#requireddropcapabilities" title="RequiredDropCapabilities">RequiredDropCapabilities</a>: <i>
      - String</i>
    <a href="#volumes" title="Volumes">Volumes</a>: <i>
      - String</i>
    <a href="#allowedcsidriver" title="AllowedCsiDriver">AllowedCsiDriver</a>: <i>
      - <a href="allowedcsidriverdefinition.md">AllowedCsiDriverDefinition</a></i>
    <a href="#allowedflexvolume" title="AllowedFlexVolume">AllowedFlexVolume</a>: <i>
      - <a href="allowedflexvolumedefinition.md">AllowedFlexVolumeDefinition</a></i>
    <a href="#allowedhostpath" title="AllowedHostPath">AllowedHostPath</a>: <i>
      - <a href="allowedhostpathdefinition.md">AllowedHostPathDefinition</a></i>
    <a href="#fsgroup" title="FsGroup">FsGroup</a>: <i>
      - <a href="fsgroupdefinition.md">FsGroupDefinition</a></i>
    <a href="#hostport" title="HostPort">HostPort</a>: <i>
      - <a href="hostportdefinition.md">HostPortDefinition</a></i>
    <a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>: <i>
      - <a href="runasgroupdefinition.md">RunAsGroupDefinition</a></i>
    <a href="#runasuser" title="RunAsUser">RunAsUser</a>: <i>
      - <a href="runasuserdefinition.md">RunAsUserDefinition</a></i>
    <a href="#runtimeclass" title="RuntimeClass">RuntimeClass</a>: <i>
      - <a href="runtimeclassdefinition.md">RuntimeClassDefinition</a></i>
    <a href="#selinux" title="SeLinux">SeLinux</a>: <i>
      - <a href="selinuxdefinition.md">SeLinuxDefinition</a></i>
    <a href="#supplementalgroup" title="SupplementalGroup">SupplementalGroup</a>: <i>
      - <a href="supplementalgroupdefinition.md">SupplementalGroupDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AllowPrivilegeEscalation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedCapabilities

(list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedProcMountTypes

(list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUnsafeSysctls

(list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

Annotations for PodSecurityPolicyTemplate object (map).

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAddCapabilities

(list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAllowPrivilegeEscalation

(list).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The PodSecurityPolicyTemplate description (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForbiddenSysctls

(list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostIpc

(bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPid

(bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Labels for PodSecurityPolicyTemplate object (map).

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the PodSecurityPolicyTemplate (string).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileged

(bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnlyRootFilesystem

(bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredDropCapabilities

(list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

(list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedCsiDriver

_Required_: No

_Type_: List of <a href="allowedcsidriverdefinition.md">AllowedCsiDriverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedFlexVolume

_Required_: No

_Type_: List of <a href="allowedflexvolumedefinition.md">AllowedFlexVolumeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedHostPath

_Required_: No

_Type_: List of <a href="allowedhostpathdefinition.md">AllowedHostPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsGroup

_Required_: No

_Type_: List of <a href="fsgroupdefinition.md">FsGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPort

_Required_: No

_Type_: List of <a href="hostportdefinition.md">HostPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunAsGroup

_Required_: No

_Type_: List of <a href="runasgroupdefinition.md">RunAsGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunAsUser

_Required_: No

_Type_: List of <a href="runasuserdefinition.md">RunAsUserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeClass

_Required_: No

_Type_: List of <a href="runtimeclassdefinition.md">RuntimeClassDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinux

_Required_: No

_Type_: List of <a href="selinuxdefinition.md">SeLinuxDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupplementalGroup

_Required_: No

_Type_: List of <a href="supplementalgroupdefinition.md">SupplementalGroupDefinition</a>

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

