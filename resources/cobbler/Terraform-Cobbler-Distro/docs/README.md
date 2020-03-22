# Terraform::Cobbler::Distro

Manages a distribution within Cobbler.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cobbler::Distro",
    "Properties" : {
        "<a href="#arch" title="Arch">Arch</a>" : <i>String</i>,
        "<a href="#bootfiles" title="BootFiles">BootFiles</a>" : <i>String</i>,
        "<a href="#breed" title="Breed">Breed</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#fetchablefiles" title="FetchableFiles">FetchableFiles</a>" : <i>String</i>,
        "<a href="#initrd" title="Initrd">Initrd</a>" : <i>String</i>,
        "<a href="#kernel" title="Kernel">Kernel</a>" : <i>String</i>,
        "<a href="#kerneloptions" title="KernelOptions">KernelOptions</a>" : <i>String</i>,
        "<a href="#kerneloptionspost" title="KernelOptionsPost">KernelOptionsPost</a>" : <i>String</i>,
        "<a href="#mgmtclasses" title="MgmtClasses">MgmtClasses</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#osversion" title="OsVersion">OsVersion</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#redhatmanagementkey" title="RedhatManagementKey">RedhatManagementKey</a>" : <i>String</i>,
        "<a href="#redhatmanagementserver" title="RedhatManagementServer">RedhatManagementServer</a>" : <i>String</i>,
        "<a href="#templatefiles" title="TemplateFiles">TemplateFiles</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cobbler::Distro
Properties:
    <a href="#arch" title="Arch">Arch</a>: <i>String</i>
    <a href="#bootfiles" title="BootFiles">BootFiles</a>: <i>String</i>
    <a href="#breed" title="Breed">Breed</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#fetchablefiles" title="FetchableFiles">FetchableFiles</a>: <i>String</i>
    <a href="#initrd" title="Initrd">Initrd</a>: <i>String</i>
    <a href="#kernel" title="Kernel">Kernel</a>: <i>String</i>
    <a href="#kerneloptions" title="KernelOptions">KernelOptions</a>: <i>String</i>
    <a href="#kerneloptionspost" title="KernelOptionsPost">KernelOptionsPost</a>: <i>String</i>
    <a href="#mgmtclasses" title="MgmtClasses">MgmtClasses</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#osversion" title="OsVersion">OsVersion</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#redhatmanagementkey" title="RedhatManagementKey">RedhatManagementKey</a>: <i>String</i>
    <a href="#redhatmanagementserver" title="RedhatManagementServer">RedhatManagementServer</a>: <i>String</i>
    <a href="#templatefiles" title="TemplateFiles">TemplateFiles</a>: <i>String</i>
</pre>

## Properties

#### Arch

The architecture of the distro. Valid options
are: i386, x86_64, ia64, ppc, ppc64, s390, arm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootFiles

Files copied into tftpboot beyond the
kernel/initrd.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Breed

The "breed" of distribution. Valid options
are: redhat, fedora, centos, scientific linux, suse, debian, and
ubuntu. These choices may vary depending on the version of Cobbler
in use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Free form text description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FetchableFiles

Templates for tftp or wget.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initrd

Absolute path to initrd on filesystem. This
must already exist prior to creating the distro.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kernel

Absolute path to kernel on filesystem. This
must already exist prior to creating the distro.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptions

Kernel options to use with the
kernel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelOptionsPost

Post install Kernel options to
use with the kernel after installation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtClasses

Management classes for external config
management.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the distro.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsVersion

The version of the distro you are
creating. This varies with the version of Cobbler you are using.
An updated signature list may need to be obtained in order to
support a newer version. Example: `trusty`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

Owners list for authz_ownership.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementKey

Red Hat Management key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedhatManagementServer

Red Hat Management server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateFiles

File mappings for built-in config
management.

_Required_: No

_Type_: String

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

