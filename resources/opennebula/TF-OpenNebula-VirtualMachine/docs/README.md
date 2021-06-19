# TF::OpenNebula::VirtualMachine

Provides an OpenNebula virtual machine resource.

This resource allows you to manage virtual machines on your OpenNebula clusters. When applied,
a new virtual machine is created. When destroyed, this virtual machine is removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::VirtualMachine",
    "Properties" : {
        "<a href="#context" title="Context">Context</a>" : <i>[ <a href="contextdefinition.md">ContextDefinition</a>, ... ]</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pending" title="Pending">Pending</a>" : <i>Boolean</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>Double</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#vcpu" title="Vcpu">Vcpu</a>" : <i>Double</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="diskdefinition.md">DiskDefinition</a>, ... ]</i>,
        "<a href="#graphics" title="Graphics">Graphics</a>" : <i>[ <a href="graphicsdefinition.md">GraphicsDefinition</a>, ... ]</i>,
        "<a href="#nic" title="Nic">Nic</a>" : <i>[ <a href="nicdefinition.md">NicDefinition</a>, ... ]</i>,
        "<a href="#os" title="Os">Os</a>" : <i>[ <a href="osdefinition.md">OsDefinition</a>, ... ]</i>,
        "<a href="#vmgroup" title="Vmgroup">Vmgroup</a>" : <i>[ <a href="vmgroupdefinition.md">VmgroupDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::VirtualMachine
Properties:
    <a href="#context" title="Context">Context</a>: <i>
      - <a href="contextdefinition.md">ContextDefinition</a></i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pending" title="Pending">Pending</a>: <i>Boolean</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#templateid" title="TemplateId">TemplateId</a>: <i>Double</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#vcpu" title="Vcpu">Vcpu</a>: <i>Double</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="diskdefinition.md">DiskDefinition</a></i>
    <a href="#graphics" title="Graphics">Graphics</a>: <i>
      - <a href="graphicsdefinition.md">GraphicsDefinition</a></i>
    <a href="#nic" title="Nic">Nic</a>: <i>
      - <a href="nicdefinition.md">NicDefinition</a></i>
    <a href="#os" title="Os">Os</a>: <i>
      - <a href="osdefinition.md">OsDefinition</a></i>
    <a href="#vmgroup" title="Vmgroup">Vmgroup</a>: <i>
      - <a href="vmgroupdefinition.md">VmgroupDefinition</a></i>
</pre>

## Properties

#### Context

Array of free form key=value pairs, rendered and added to the CONTEXT variables for the VM. Recommended to include: `NETWORK = "YES"` and `SET_HOSTNAME = "$NAME"`. If a `template_id` is set, see [Instantiate from a template](#instantiate-from-a-template) for details.

_Required_: No

_Type_: List of <a href="contextdefinition.md">ContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

Amount of CPU shares assigned to the VM. **Mandatory if** `template_id` **is not set**.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Name of the group which owns the virtual machine. Defaults to the caller primary group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

Amount of RAM assigned to the VM in MB. **Mandatory if** `template_id` **is not set**.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the virtual machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pending

Pending state during VM creation. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Permissions applied on virtual machine. Defaults to the UMASK in OpenNebula (in UNIX Format: owner-group-other => Use-Manage-Admin).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Virtual Machine tags (Key = Value).

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

If set, VM are instantiated from the template ID. See [Instantiate from a template](#instantiate-from-a-template) for details. Changing this argument triggers a new resource.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout (in Minutes) for VM availability. Defaults to 3 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="diskdefinition.md">DiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Graphics

_Required_: No

_Type_: List of <a href="graphicsdefinition.md">GraphicsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nic

_Required_: No

_Type_: List of <a href="nicdefinition.md">NicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Os

_Required_: No

_Type_: List of <a href="osdefinition.md">OsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vmgroup

_Required_: No

_Type_: List of <a href="vmgroupdefinition.md">VmgroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Gid

Returns the <code>Gid</code> value.

#### Gname

Returns the <code>Gname</code> value.

#### Id

Returns the <code>Id</code> value.

#### Instance

Returns the <code>Instance</code> value.

#### Ip

Returns the <code>Ip</code> value.

#### Lcmstate

Returns the <code>Lcmstate</code> value.

#### State

Returns the <code>State</code> value.

#### Uid

Returns the <code>Uid</code> value.

#### Uname

Returns the <code>Uname</code> value.

