# Terraform::Cobbler::Profile

Manages a Profile within Cobbler.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cobbler::Profile",
    "Properties" : {
        "<a href="#bootfiles" title="BootFiles">BootFiles</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#distro" title="Distro">Distro</a>" : <i>String</i>,
        "<a href="#enablegpxe" title="EnableGpxe">EnableGpxe</a>" : <i>Boolean</i>,
        "<a href="#enablemenu" title="EnableMenu">EnableMenu</a>" : <i>Boolean</i>,
        "<a href="#fetchablefiles" title="FetchableFiles">FetchableFiles</a>" : <i>String</i>,
        "<a href="#kerneloptions" title="KernelOptions">KernelOptions</a>" : <i>String</i>,
        "<a href="#kerneloptionspost" title="KernelOptionsPost">KernelOptionsPost</a>" : <i>String</i>,
        "<a href="#kickstart" title="Kickstart">Kickstart</a>" : <i>String</i>,
        "<a href="#ksmeta" title="KsMeta">KsMeta</a>" : <i>String</i>,
        "<a href="#mgmtclasses" title="MgmtClasses">MgmtClasses</a>" : <i>[ String, ... ]</i>,
        "<a href="#mgmtparameters" title="MgmtParameters">MgmtParameters</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameservers" title="NameServers">NameServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#nameserverssearch" title="NameServersSearch">NameServersSearch</a>" : <i>[ String, ... ]</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#redhatmanagementkey" title="RedhatManagementKey">RedhatManagementKey</a>" : <i>String</i>,
        "<a href="#redhatmanagementserver" title="RedhatManagementServer">RedhatManagementServer</a>" : <i>String</i>,
        "<a href="#repos" title="Repos">Repos</a>" : <i>[ String, ... ]</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#templatefiles" title="TemplateFiles">TemplateFiles</a>" : <i>String</i>,
        "<a href="#templateremotekickstarts" title="TemplateRemoteKickstarts">TemplateRemoteKickstarts</a>" : <i>Double</i>,
        "<a href="#virtautoboot" title="VirtAutoBoot">VirtAutoBoot</a>" : <i>String</i>,
        "<a href="#virtbridge" title="VirtBridge">VirtBridge</a>" : <i>String</i>,
        "<a href="#virtcpus" title="VirtCpus">VirtCpus</a>" : <i>String</i>,
        "<a href="#virtdiskdriver" title="VirtDiskDriver">VirtDiskDriver</a>" : <i>String</i>,
        "<a href="#virtfilesize" title="VirtFileSize">VirtFileSize</a>" : <i>String</i>,
        "<a href="#virtpath" title="VirtPath">VirtPath</a>" : <i>String</i>,
        "<a href="#virtram" title="VirtRam">VirtRam</a>" : <i>String</i>,
        "<a href="#virttype" title="VirtType">VirtType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cobbler::Profile
Properties:
    <a href="#bootfiles" title="BootFiles">BootFiles</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#distro" title="Distro">Distro</a>: <i>String</i>
    <a href="#enablegpxe" title="EnableGpxe">EnableGpxe</a>: <i>Boolean</i>
    <a href="#enablemenu" title="EnableMenu">EnableMenu</a>: <i>Boolean</i>
    <a href="#fetchablefiles" title="FetchableFiles">FetchableFiles</a>: <i>String</i>
    <a href="#kerneloptions" title="KernelOptions">KernelOptions</a>: <i>String</i>
    <a href="#kerneloptionspost" title="KernelOptionsPost">KernelOptionsPost</a>: <i>String</i>
    <a href="#kickstart" title="Kickstart">Kickstart</a>: <i>String</i>
    <a href="#ksmeta" title="KsMeta">KsMeta</a>: <i>String</i>
    <a href="#mgmtclasses" title="MgmtClasses">MgmtClasses</a>: <i>
      - String</i>
    <a href="#mgmtparameters" title="MgmtParameters">MgmtParameters</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameservers" title="NameServers">NameServers</a>: <i>
      - String</i>
    <a href="#nameserverssearch" title="NameServersSearch">NameServersSearch</a>: <i>
      - String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#redhatmanagementkey" title="RedhatManagementKey">RedhatManagementKey</a>: <i>String</i>
    <a href="#redhatmanagementserver" title="RedhatManagementServer">RedhatManagementServer</a>: <i>String</i>
    <a href="#repos" title="Repos">Repos</a>: <i>
      - String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#templatefiles" title="TemplateFiles">TemplateFiles</a>: <i>String</i>
    <a href="#templateremotekickstarts" title="TemplateRemoteKickstarts">TemplateRemoteKickstarts</a>: <i>Double</i>
    <a href="#virtautoboot" title="VirtAutoBoot">VirtAutoBoot</a>: <i>String</i>
    <a href="#virtbridge" title="VirtBridge">VirtBridge</a>: <i>String</i>
    <a href="#virtcpus" title="VirtCpus">VirtCpus</a>: <i>String</i>
    <a href="#virtdiskdriver" title="VirtDiskDriver">VirtDiskDriver</a>: <i>String</i>
    <a href="#virtfilesize" title="VirtFileSize">VirtFileSize</a>: <i>String</i>
    <a href="#virtpath" title="VirtPath">VirtPath</a>: <i>String</i>
    <a href="#virtram" title="VirtRam">VirtRam</a>: <i>String</i>
    <a href="#virttype" title="VirtType">VirtType</a>: <i>String</i>
</pre>

## Properties

#### BootFiles

Files copied into tftpboot beyond the
kernel/initrd.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Free form text description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distro

Parent distribution.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGpxe

Use gPXE instead of PXELINUX for
advanced booting options.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMenu

Enable a boot menu.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FetchableFiles

Templates for tftp or wget.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptions

Kernel options for the profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptionsPost

Post install kernel options.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kickstart

The kickstart file to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KsMeta

Kickstart metadata.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtClasses

For external configuration management.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtParameters

Parameters which will be handed to
your management application (Must be a valid YAML dictionary).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServers

Name servers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServersSearch

Name server search settings.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

Owners list for authz_ownership.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

The parent this profile inherits settings from.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

Proxy URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementKey

Red Hat Management Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementServer

RedHat Management Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repos

Repos to auto-assign to this profile.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

The server-override for the profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFiles

File mappings for built-in config
management.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateRemoteKickstarts

remote kickstart
templates.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtAutoBoot

Auto boot virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtBridge

The bridge for virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtCpus

The number of virtual CPUs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtDiskDriver

The virtual machine disk driver.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtFileSize

The virtual machine file size.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtPath

The virtual machine path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtRam

The amount of RAM for the virtual machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtType

The type of virtual machine. Valid options
are: xenpv, xenfv, qemu, kvm, vmware, openvz.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

