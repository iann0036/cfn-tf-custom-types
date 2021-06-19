# TF::Volterra::K8sPodSecurityPolicy PspSpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>" : <i>Boolean</i>,
    "<a href="#allowedcsidrivers" title="AllowedCsiDrivers">AllowedCsiDrivers</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedflexvolumes" title="AllowedFlexVolumes">AllowedFlexVolumes</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedprocmounts" title="AllowedProcMounts">AllowedProcMounts</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultallowprivilegeescalation" title="DefaultAllowPrivilegeEscalation">DefaultAllowPrivilegeEscalation</a>" : <i>Boolean</i>,
    "<a href="#forbiddensysctls" title="ForbiddenSysctls">ForbiddenSysctls</a>" : <i>[ String, ... ]</i>,
    "<a href="#hostipc" title="HostIpc">HostIpc</a>" : <i>Boolean</i>,
    "<a href="#hostnetwork" title="HostNetwork">HostNetwork</a>" : <i>Boolean</i>,
    "<a href="#hostpid" title="HostPid">HostPid</a>" : <i>Boolean</i>,
    "<a href="#hostportranges" title="HostPortRanges">HostPortRanges</a>" : <i>String</i>,
    "<a href="#noallowedcapabilities" title="NoAllowedCapabilities">NoAllowedCapabilities</a>" : <i>Boolean</i>,
    "<a href="#nodefaultcapabilities" title="NoDefaultCapabilities">NoDefaultCapabilities</a>" : <i>Boolean</i>,
    "<a href="#nodropcapabilities" title="NoDropCapabilities">NoDropCapabilities</a>" : <i>Boolean</i>,
    "<a href="#nofsgroups" title="NoFsGroups">NoFsGroups</a>" : <i>Boolean</i>,
    "<a href="#norunasgroup" title="NoRunAsGroup">NoRunAsGroup</a>" : <i>Boolean</i>,
    "<a href="#norunasuser" title="NoRunAsUser">NoRunAsUser</a>" : <i>Boolean</i>,
    "<a href="#noruntimeclass" title="NoRuntimeClass">NoRuntimeClass</a>" : <i>Boolean</i>,
    "<a href="#noselinuxoptions" title="NoSeLinuxOptions">NoSeLinuxOptions</a>" : <i>Boolean</i>,
    "<a href="#nosupplementalgroups" title="NoSupplementalGroups">NoSupplementalGroups</a>" : <i>Boolean</i>,
    "<a href="#privileged" title="Privileged">Privileged</a>" : <i>Boolean</i>,
    "<a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>" : <i>Boolean</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedcapabilities" title="AllowedCapabilities">AllowedCapabilities</a>" : <i>[ <a href="allowedcapabilitiesdefinition.md">AllowedCapabilitiesDefinition</a>, ... ]</i>,
    "<a href="#allowedhostpaths" title="AllowedHostPaths">AllowedHostPaths</a>" : <i>[ <a href="allowedhostpathsdefinition.md">AllowedHostPathsDefinition</a>, ... ]</i>,
    "<a href="#defaultcapabilities" title="DefaultCapabilities">DefaultCapabilities</a>" : <i>[ <a href="defaultcapabilitiesdefinition.md">DefaultCapabilitiesDefinition</a>, ... ]</i>,
    "<a href="#dropcapabilities" title="DropCapabilities">DropCapabilities</a>" : <i>[ <a href="dropcapabilitiesdefinition.md">DropCapabilitiesDefinition</a>, ... ]</i>,
    "<a href="#fsgroupstrategyoptions" title="FsGroupStrategyOptions">FsGroupStrategyOptions</a>" : <i>[ <a href="fsgroupstrategyoptionsdefinition.md">FsGroupStrategyOptionsDefinition</a>, ... ]</i>,
    "<a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>" : <i>[ <a href="runasgroupdefinition.md">RunAsGroupDefinition</a>, ... ]</i>,
    "<a href="#runasuser" title="RunAsUser">RunAsUser</a>" : <i>[ <a href="runasuserdefinition.md">RunAsUserDefinition</a>, ... ]</i>,
    "<a href="#runtimeclass" title="RuntimeClass">RuntimeClass</a>" : <i>[ <a href="runtimeclassdefinition.md">RuntimeClassDefinition</a>, ... ]</i>,
    "<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>" : <i>[ <a href="selinuxoptionsdefinition.md">SeLinuxOptionsDefinition</a>, ... ]</i>,
    "<a href="#supplementalgroups" title="SupplementalGroups">SupplementalGroups</a>" : <i>[ <a href="supplementalgroupsdefinition.md">SupplementalGroupsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>: <i>Boolean</i>
<a href="#allowedcsidrivers" title="AllowedCsiDrivers">AllowedCsiDrivers</a>: <i>
      - String</i>
<a href="#allowedflexvolumes" title="AllowedFlexVolumes">AllowedFlexVolumes</a>: <i>
      - String</i>
<a href="#allowedprocmounts" title="AllowedProcMounts">AllowedProcMounts</a>: <i>
      - String</i>
<a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>: <i>
      - String</i>
<a href="#defaultallowprivilegeescalation" title="DefaultAllowPrivilegeEscalation">DefaultAllowPrivilegeEscalation</a>: <i>Boolean</i>
<a href="#forbiddensysctls" title="ForbiddenSysctls">ForbiddenSysctls</a>: <i>
      - String</i>
<a href="#hostipc" title="HostIpc">HostIpc</a>: <i>Boolean</i>
<a href="#hostnetwork" title="HostNetwork">HostNetwork</a>: <i>Boolean</i>
<a href="#hostpid" title="HostPid">HostPid</a>: <i>Boolean</i>
<a href="#hostportranges" title="HostPortRanges">HostPortRanges</a>: <i>String</i>
<a href="#noallowedcapabilities" title="NoAllowedCapabilities">NoAllowedCapabilities</a>: <i>Boolean</i>
<a href="#nodefaultcapabilities" title="NoDefaultCapabilities">NoDefaultCapabilities</a>: <i>Boolean</i>
<a href="#nodropcapabilities" title="NoDropCapabilities">NoDropCapabilities</a>: <i>Boolean</i>
<a href="#nofsgroups" title="NoFsGroups">NoFsGroups</a>: <i>Boolean</i>
<a href="#norunasgroup" title="NoRunAsGroup">NoRunAsGroup</a>: <i>Boolean</i>
<a href="#norunasuser" title="NoRunAsUser">NoRunAsUser</a>: <i>Boolean</i>
<a href="#noruntimeclass" title="NoRuntimeClass">NoRuntimeClass</a>: <i>Boolean</i>
<a href="#noselinuxoptions" title="NoSeLinuxOptions">NoSeLinuxOptions</a>: <i>Boolean</i>
<a href="#nosupplementalgroups" title="NoSupplementalGroups">NoSupplementalGroups</a>: <i>Boolean</i>
<a href="#privileged" title="Privileged">Privileged</a>: <i>Boolean</i>
<a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>: <i>Boolean</i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - String</i>
<a href="#allowedcapabilities" title="AllowedCapabilities">AllowedCapabilities</a>: <i>
      - <a href="allowedcapabilitiesdefinition.md">AllowedCapabilitiesDefinition</a></i>
<a href="#allowedhostpaths" title="AllowedHostPaths">AllowedHostPaths</a>: <i>
      - <a href="allowedhostpathsdefinition.md">AllowedHostPathsDefinition</a></i>
<a href="#defaultcapabilities" title="DefaultCapabilities">DefaultCapabilities</a>: <i>
      - <a href="defaultcapabilitiesdefinition.md">DefaultCapabilitiesDefinition</a></i>
<a href="#dropcapabilities" title="DropCapabilities">DropCapabilities</a>: <i>
      - <a href="dropcapabilitiesdefinition.md">DropCapabilitiesDefinition</a></i>
<a href="#fsgroupstrategyoptions" title="FsGroupStrategyOptions">FsGroupStrategyOptions</a>: <i>
      - <a href="fsgroupstrategyoptionsdefinition.md">FsGroupStrategyOptionsDefinition</a></i>
<a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>: <i>
      - <a href="runasgroupdefinition.md">RunAsGroupDefinition</a></i>
<a href="#runasuser" title="RunAsUser">RunAsUser</a>: <i>
      - <a href="runasuserdefinition.md">RunAsUserDefinition</a></i>
<a href="#runtimeclass" title="RuntimeClass">RuntimeClass</a>: <i>
      - <a href="runtimeclassdefinition.md">RuntimeClassDefinition</a></i>
<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>: <i>
      - <a href="selinuxoptionsdefinition.md">SeLinuxOptionsDefinition</a></i>
<a href="#supplementalgroups" title="SupplementalGroups">SupplementalGroups</a>: <i>
      - <a href="supplementalgroupsdefinition.md">SupplementalGroupsDefinition</a></i>
</pre>

## Properties

#### AllowPrivilegeEscalation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedCsiDrivers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedFlexVolumes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedProcMounts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUnsafeSysctls

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

#### HostPortRanges

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAllowedCapabilities

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDefaultCapabilities

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDropCapabilities

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoFsGroups

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoRunAsGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoRunAsUser

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoRuntimeClass

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSeLinuxOptions

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSupplementalGroups

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

#### Volumes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedCapabilities

_Required_: No

_Type_: List of <a href="allowedcapabilitiesdefinition.md">AllowedCapabilitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedHostPaths

_Required_: No

_Type_: List of <a href="allowedhostpathsdefinition.md">AllowedHostPathsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCapabilities

_Required_: No

_Type_: List of <a href="defaultcapabilitiesdefinition.md">DefaultCapabilitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropCapabilities

_Required_: No

_Type_: List of <a href="dropcapabilitiesdefinition.md">DropCapabilitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsGroupStrategyOptions

_Required_: No

_Type_: List of <a href="fsgroupstrategyoptionsdefinition.md">FsGroupStrategyOptionsDefinition</a>

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

#### SeLinuxOptions

_Required_: No

_Type_: List of <a href="selinuxoptionsdefinition.md">SeLinuxOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupplementalGroups

_Required_: No

_Type_: List of <a href="supplementalgroupsdefinition.md">SupplementalGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

