# Terraform::Cobbler::Profile

CloudFormation equivalent of cobbler_profile

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distro

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGpxe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMenu

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FetchableFiles

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptionsPost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kickstart

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KsMeta

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtClasses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtParameters

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServersSearch

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repos

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFiles

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateRemoteKickstarts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtAutoBoot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtBridge

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtCpus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtDiskDriver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtFileSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtRam

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtType

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

