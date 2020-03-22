# Terraform::Cobbler::System

Manages a System within Cobbler.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cobbler::System",
    "Properties" : {
        "<a href="#bootfiles" title="BootFiles">BootFiles</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#enablegpxe" title="EnableGpxe">EnableGpxe</a>" : <i>Boolean</i>,
        "<a href="#fetchablefiles" title="FetchableFiles">FetchableFiles</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#ipv6defaultdevice" title="Ipv6DefaultDevice">Ipv6DefaultDevice</a>" : <i>String</i>,
        "<a href="#kerneloptions" title="KernelOptions">KernelOptions</a>" : <i>String</i>,
        "<a href="#kerneloptionspost" title="KernelOptionsPost">KernelOptionsPost</a>" : <i>String</i>,
        "<a href="#kickstart" title="Kickstart">Kickstart</a>" : <i>String</i>,
        "<a href="#ksmeta" title="KsMeta">KsMeta</a>" : <i>String</i>,
        "<a href="#ldapenabled" title="LdapEnabled">LdapEnabled</a>" : <i>Boolean</i>,
        "<a href="#ldaptype" title="LdapType">LdapType</a>" : <i>String</i>,
        "<a href="#mgmtclasses" title="MgmtClasses">MgmtClasses</a>" : <i>[ String, ... ]</i>,
        "<a href="#mgmtparameters" title="MgmtParameters">MgmtParameters</a>" : <i>String</i>,
        "<a href="#monitenabled" title="MonitEnabled">MonitEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameservers" title="NameServers">NameServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#nameserverssearch" title="NameServersSearch">NameServersSearch</a>" : <i>[ String, ... ]</i>,
        "<a href="#netbootenabled" title="NetbootEnabled">NetbootEnabled</a>" : <i>Boolean</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#poweraddress" title="PowerAddress">PowerAddress</a>" : <i>String</i>,
        "<a href="#powerid" title="PowerId">PowerId</a>" : <i>String</i>,
        "<a href="#powerpass" title="PowerPass">PowerPass</a>" : <i>String</i>,
        "<a href="#powertype" title="PowerType">PowerType</a>" : <i>String</i>,
        "<a href="#poweruser" title="PowerUser">PowerUser</a>" : <i>String</i>,
        "<a href="#profile" title="Profile">Profile</a>" : <i>String</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#redhatmanagementkey" title="RedhatManagementKey">RedhatManagementKey</a>" : <i>String</i>,
        "<a href="#redhatmanagementserver" title="RedhatManagementServer">RedhatManagementServer</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#templatefiles" title="TemplateFiles">TemplateFiles</a>" : <i>String</i>,
        "<a href="#templateremotekickstarts" title="TemplateRemoteKickstarts">TemplateRemoteKickstarts</a>" : <i>Double</i>,
        "<a href="#virtautoboot" title="VirtAutoBoot">VirtAutoBoot</a>" : <i>String</i>,
        "<a href="#virtcpus" title="VirtCpus">VirtCpus</a>" : <i>String</i>,
        "<a href="#virtdiskdriver" title="VirtDiskDriver">VirtDiskDriver</a>" : <i>String</i>,
        "<a href="#virtfilesize" title="VirtFileSize">VirtFileSize</a>" : <i>String</i>,
        "<a href="#virtpath" title="VirtPath">VirtPath</a>" : <i>String</i>,
        "<a href="#virtpxeboot" title="VirtPxeBoot">VirtPxeBoot</a>" : <i>Double</i>,
        "<a href="#virtram" title="VirtRam">VirtRam</a>" : <i>String</i>,
        "<a href="#virttype" title="VirtType">VirtType</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interface.md">Interface</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cobbler::System
Properties:
    <a href="#bootfiles" title="BootFiles">BootFiles</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#enablegpxe" title="EnableGpxe">EnableGpxe</a>: <i>Boolean</i>
    <a href="#fetchablefiles" title="FetchableFiles">FetchableFiles</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#ipv6defaultdevice" title="Ipv6DefaultDevice">Ipv6DefaultDevice</a>: <i>String</i>
    <a href="#kerneloptions" title="KernelOptions">KernelOptions</a>: <i>String</i>
    <a href="#kerneloptionspost" title="KernelOptionsPost">KernelOptionsPost</a>: <i>String</i>
    <a href="#kickstart" title="Kickstart">Kickstart</a>: <i>String</i>
    <a href="#ksmeta" title="KsMeta">KsMeta</a>: <i>String</i>
    <a href="#ldapenabled" title="LdapEnabled">LdapEnabled</a>: <i>Boolean</i>
    <a href="#ldaptype" title="LdapType">LdapType</a>: <i>String</i>
    <a href="#mgmtclasses" title="MgmtClasses">MgmtClasses</a>: <i>
      - String</i>
    <a href="#mgmtparameters" title="MgmtParameters">MgmtParameters</a>: <i>String</i>
    <a href="#monitenabled" title="MonitEnabled">MonitEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameservers" title="NameServers">NameServers</a>: <i>
      - String</i>
    <a href="#nameserverssearch" title="NameServersSearch">NameServersSearch</a>: <i>
      - String</i>
    <a href="#netbootenabled" title="NetbootEnabled">NetbootEnabled</a>: <i>Boolean</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#poweraddress" title="PowerAddress">PowerAddress</a>: <i>String</i>
    <a href="#powerid" title="PowerId">PowerId</a>: <i>String</i>
    <a href="#powerpass" title="PowerPass">PowerPass</a>: <i>String</i>
    <a href="#powertype" title="PowerType">PowerType</a>: <i>String</i>
    <a href="#poweruser" title="PowerUser">PowerUser</a>: <i>String</i>
    <a href="#profile" title="Profile">Profile</a>: <i>String</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#redhatmanagementkey" title="RedhatManagementKey">RedhatManagementKey</a>: <i>String</i>
    <a href="#redhatmanagementserver" title="RedhatManagementServer">RedhatManagementServer</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#templatefiles" title="TemplateFiles">TemplateFiles</a>: <i>String</i>
    <a href="#templateremotekickstarts" title="TemplateRemoteKickstarts">TemplateRemoteKickstarts</a>: <i>Double</i>
    <a href="#virtautoboot" title="VirtAutoBoot">VirtAutoBoot</a>: <i>String</i>
    <a href="#virtcpus" title="VirtCpus">VirtCpus</a>: <i>String</i>
    <a href="#virtdiskdriver" title="VirtDiskDriver">VirtDiskDriver</a>: <i>String</i>
    <a href="#virtfilesize" title="VirtFileSize">VirtFileSize</a>: <i>String</i>
    <a href="#virtpath" title="VirtPath">VirtPath</a>: <i>String</i>
    <a href="#virtpxeboot" title="VirtPxeBoot">VirtPxeBoot</a>: <i>Double</i>
    <a href="#virtram" title="VirtRam">VirtRam</a>: <i>String</i>
    <a href="#virttype" title="VirtType">VirtType</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interface.md">Interface</a></i>
</pre>

## Properties

#### BootFiles

TFTP boot files copied into tftpboot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Free form text description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGpxe

Use gPXE instead of PXELINUX.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FetchableFiles

Templates for tftp or wget.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Network gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Hostname of the system.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

Parent image (if no profile is used).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DefaultDevice

IPv6 default device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptions

Kernel options.
ex: selinux=permissive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptionsPost

Kernel options (post install).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kickstart

Path to kickstart template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KsMeta

Kickstart metadata.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapEnabled

Configure LDAP at next config update.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapType

LDAP management type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtClasses

Management classes for external config
management.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtParameters

Parameters which will be handed to
your management application. Must be a valid YAML dictionary.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitEnabled

Configure monit on this machine at
next config update.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the system.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServers

Name servers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServersSearch

Name servers search path.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetbootEnabled

(re)Install this machine at next
boot.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

Owners list for authz_ownership.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerAddress

Power management address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerId

Usually a plug number or blade name if
power type requires it.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerPass

Power management password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerType

Power management type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerUser

Power management user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

Parent profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

Proxy URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementKey

Red Hat management key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementServer

Red Hat management server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

System status (development, testing,
acceptance, production).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFiles

File mappings for built-in
configuration management.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateRemoteKickstarts

template remote
kickstarts.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtAutoBoot

Auto boot the VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtCpus

Number of virtual CPUs in the VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtDiskDriver

The on-disk format for the
virtualization disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtFileSize

Virt file size.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtPath

Path to the VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtPxeBoot

Use PXE to build this VM?.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtRam

The amount of RAM for the VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtType

Virtualization technology to use: xenpv,
xenfv, qemu, kvm, vmware, openvz.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interface.md">Interface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

