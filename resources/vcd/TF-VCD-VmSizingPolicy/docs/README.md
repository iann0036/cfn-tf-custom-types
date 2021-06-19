# TF::VCD::VmSizingPolicy

Provides a vCloud Director VM sizing policy resource. This can be
used to create, modify, and delete VM sizing policy.

Supported in provider *v3.0+* and requires VCD 10.0+

~> **Note:** 
CPU and memory properties of a VM sizing policy can't be updated in-place, so updating them will force a re-create. For such re-creation to succeed, the policy can't be used by VDC and VM. Hence, the policy usage has to be removed from VDC and VM beforehand. For the cases when that is not trivial, a two-step approach may be easier: to create a new policy with the new values, assign it to VDC and VM, and afterwards remove the old policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::VmSizingPolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>[ <a href="cpudefinition.md">CpuDefinition</a>, ... ]</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>[ <a href="memorydefinition.md">MemoryDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::VmSizingPolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>
      - <a href="cpudefinition.md">CpuDefinition</a></i>
    <a href="#memory" title="Memory">Memory</a>: <i>
      - <a href="memorydefinition.md">MemoryDefinition</a></i>
</pre>

## Properties

#### Description

description of VM sizing policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of VM sizing policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organizations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: List of <a href="cpudefinition.md">CpuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: List of <a href="memorydefinition.md">MemoryDefinition</a>

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

