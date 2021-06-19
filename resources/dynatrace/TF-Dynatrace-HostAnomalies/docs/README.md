# TF::Dynatrace::HostAnomalies

CloudFormation equivalent of dynatrace_host_anomalies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::HostAnomalies",
    "Properties" : {
        "<a href="#connections" title="Connections">Connections</a>" : <i>[ <a href="connectionsdefinition.md">ConnectionsDefinition</a>, ... ]</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>[ <a href="cpudefinition.md">CpuDefinition</a>, ... ]</i>,
        "<a href="#disks" title="Disks">Disks</a>" : <i>[ <a href="disksdefinition.md">DisksDefinition</a>, ... ]</i>,
        "<a href="#gc" title="Gc">Gc</a>" : <i>[ <a href="gcdefinition.md">GcDefinition</a>, ... ]</i>,
        "<a href="#java" title="Java">Java</a>" : <i>[ <a href="javadefinition.md">JavaDefinition</a>, ... ]</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>[ <a href="memorydefinition.md">MemoryDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::HostAnomalies
Properties:
    <a href="#connections" title="Connections">Connections</a>: <i>
      - <a href="connectionsdefinition.md">ConnectionsDefinition</a></i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>
      - <a href="cpudefinition.md">CpuDefinition</a></i>
    <a href="#disks" title="Disks">Disks</a>: <i>
      - <a href="disksdefinition.md">DisksDefinition</a></i>
    <a href="#gc" title="Gc">Gc</a>: <i>
      - <a href="gcdefinition.md">GcDefinition</a></i>
    <a href="#java" title="Java">Java</a>: <i>
      - <a href="javadefinition.md">JavaDefinition</a></i>
    <a href="#memory" title="Memory">Memory</a>: <i>
      - <a href="memorydefinition.md">MemoryDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
</pre>

## Properties

#### Connections

_Required_: No

_Type_: List of <a href="connectionsdefinition.md">ConnectionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: List of <a href="cpudefinition.md">CpuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disks

_Required_: No

_Type_: List of <a href="disksdefinition.md">DisksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gc

_Required_: No

_Type_: List of <a href="gcdefinition.md">GcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Java

_Required_: No

_Type_: List of <a href="javadefinition.md">JavaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: List of <a href="memorydefinition.md">MemoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

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

