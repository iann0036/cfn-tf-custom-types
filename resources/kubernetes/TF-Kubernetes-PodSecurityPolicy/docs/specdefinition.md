# TF::Kubernetes::PodSecurityPolicy SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>" : <i>Boolean</i>,
    "<a href="#allowedcapabilities" title="AllowedCapabilities">AllowedCapabilities</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedprocmounttypes" title="AllowedProcMountTypes">AllowedProcMountTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultaddcapabilities" title="DefaultAddCapabilities">DefaultAddCapabilities</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultallowprivilegeescalation" title="DefaultAllowPrivilegeEscalation">DefaultAllowPrivilegeEscalation</a>" : <i>Boolean</i>,
    "<a href="#forbiddensysctls" title="ForbiddenSysctls">ForbiddenSysctls</a>" : <i>[ String, ... ]</i>,
    "<a href="#hostipc" title="HostIpc">HostIpc</a>" : <i>Boolean</i>,
    "<a href="#hostnetwork" title="HostNetwork">HostNetwork</a>" : <i>Boolean</i>,
    "<a href="#hostpid" title="HostPid">HostPid</a>" : <i>Boolean</i>,
    "<a href="#privileged" title="Privileged">Privileged</a>" : <i>Boolean</i>,
    "<a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>" : <i>Boolean</i>,
    "<a href="#requireddropcapabilities" title="RequiredDropCapabilities">RequiredDropCapabilities</a>" : <i>[ String, ... ]</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedflexvolumes" title="AllowedFlexVolumes">AllowedFlexVolumes</a>" : <i>[ <a href="allowedflexvolumesdefinition.md">AllowedFlexVolumesDefinition</a>, ... ]</i>,
    "<a href="#allowedhostpaths" title="AllowedHostPaths">AllowedHostPaths</a>" : <i>[ <a href="allowedhostpathsdefinition.md">AllowedHostPathsDefinition</a>, ... ]</i>,
    "<a href="#fsgroup" title="FsGroup">FsGroup</a>" : <i>[ <a href="fsgroupdefinition.md">FsGroupDefinition</a>, ... ]</i>,
    "<a href="#hostports" title="HostPorts">HostPorts</a>" : <i>[ <a href="hostportsdefinition.md">HostPortsDefinition</a>, ... ]</i>,
    "<a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>" : <i>[ <a href="runasgroupdefinition.md">RunAsGroupDefinition</a>, ... ]</i>,
    "<a href="#runasuser" title="RunAsUser">RunAsUser</a>" : <i>[ <a href="runasuserdefinition.md">RunAsUserDefinition</a>, ... ]</i>,
    "<a href="#selinux" title="SeLinux">SeLinux</a>" : <i>[ <a href="selinuxdefinition.md">SeLinuxDefinition</a>, ... ]</i>,
    "<a href="#supplementalgroups" title="SupplementalGroups">SupplementalGroups</a>" : <i>[ <a href="supplementalgroupsdefinition.md">SupplementalGroupsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>: <i>Boolean</i>
<a href="#allowedcapabilities" title="AllowedCapabilities">AllowedCapabilities</a>: <i>
      - String</i>
<a href="#allowedprocmounttypes" title="AllowedProcMountTypes">AllowedProcMountTypes</a>: <i>
      - String</i>
<a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>: <i>
      - String</i>
<a href="#defaultaddcapabilities" title="DefaultAddCapabilities">DefaultAddCapabilities</a>: <i>
      - String</i>
<a href="#defaultallowprivilegeescalation" title="DefaultAllowPrivilegeEscalation">DefaultAllowPrivilegeEscalation</a>: <i>Boolean</i>
<a href="#forbiddensysctls" title="ForbiddenSysctls">ForbiddenSysctls</a>: <i>
      - String</i>
<a href="#hostipc" title="HostIpc">HostIpc</a>: <i>Boolean</i>
<a href="#hostnetwork" title="HostNetwork">HostNetwork</a>: <i>Boolean</i>
<a href="#hostpid" title="HostPid">HostPid</a>: <i>Boolean</i>
<a href="#privileged" title="Privileged">Privileged</a>: <i>Boolean</i>
<a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>: <i>Boolean</i>
<a href="#requireddropcapabilities" title="RequiredDropCapabilities">RequiredDropCapabilities</a>: <i>
      - String</i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - String</i>
<a href="#allowedflexvolumes" title="AllowedFlexVolumes">AllowedFlexVolumes</a>: <i>
      - <a href="allowedflexvolumesdefinition.md">AllowedFlexVolumesDefinition</a></i>
<a href="#allowedhostpaths" title="AllowedHostPaths">AllowedHostPaths</a>: <i>
      - <a href="allowedhostpathsdefinition.md">AllowedHostPathsDefinition</a></i>
<a href="#fsgroup" title="FsGroup">FsGroup</a>: <i>
      - <a href="fsgroupdefinition.md">FsGroupDefinition</a></i>
<a href="#hostports" title="HostPorts">HostPorts</a>: <i>
      - <a href="hostportsdefinition.md">HostPortsDefinition</a></i>
<a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>: <i>
      - <a href="runasgroupdefinition.md">RunAsGroupDefinition</a></i>
<a href="#runasuser" title="RunAsUser">RunAsUser</a>: <i>
      - <a href="runasuserdefinition.md">RunAsUserDefinition</a></i>
<a href="#selinux" title="SeLinux">SeLinux</a>: <i>
      - <a href="selinuxdefinition.md">SeLinuxDefinition</a></i>
<a href="#supplementalgroups" title="SupplementalGroups">SupplementalGroups</a>: <i>
      - <a href="supplementalgroupsdefinition.md">SupplementalGroupsDefinition</a></i>
</pre>

## Properties

#### AllowPrivilegeEscalation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedCapabilities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedProcMountTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUnsafeSysctls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAddCapabilities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAllowPrivilegeEscalation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForbiddenSysctls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostIpc

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPid

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileged

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnlyRootFilesystem

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredDropCapabilities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedFlexVolumes

_Required_: No

_Type_: List of <a href="allowedflexvolumesdefinition.md">AllowedFlexVolumesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedHostPaths

_Required_: No

_Type_: List of <a href="allowedhostpathsdefinition.md">AllowedHostPathsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsGroup

_Required_: No

_Type_: List of <a href="fsgroupdefinition.md">FsGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPorts

_Required_: No

_Type_: List of <a href="hostportsdefinition.md">HostPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunAsGroup

_Required_: No

_Type_: List of <a href="runasgroupdefinition.md">RunAsGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunAsUser

_Required_: No

_Type_: List of <a href="runasuserdefinition.md">RunAsUserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinux

_Required_: No

_Type_: List of <a href="selinuxdefinition.md">SeLinuxDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupplementalGroups

_Required_: No

_Type_: List of <a href="supplementalgroupsdefinition.md">SupplementalGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

