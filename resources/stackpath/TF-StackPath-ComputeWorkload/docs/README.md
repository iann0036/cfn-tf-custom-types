# TF::StackPath::ComputeWorkload

A computing application deployed to StackPath's edge network.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::StackPath::ComputeWorkload",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#slug" title="Slug">Slug</a>" : <i>String</i>,
        "<a href="#container" title="Container">Container</a>" : <i>[ <a href="containerdefinition.md">ContainerDefinition</a>, ... ]</i>,
        "<a href="#imagepullcredentials" title="ImagePullCredentials">ImagePullCredentials</a>" : <i>[ <a href="imagepullcredentialsdefinition.md">ImagePullCredentialsDefinition</a>, ... ]</i>,
        "<a href="#instances" title="Instances">Instances</a>" : <i>[ <a href="instancesdefinition.md">InstancesDefinition</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>[ <a href="targetdefinition.md">TargetDefinition</a>, ... ]</i>,
        "<a href="#virtualmachine" title="VirtualMachine">VirtualMachine</a>" : <i>[ <a href="virtualmachinedefinition.md">VirtualMachineDefinition</a>, ... ]</i>,
        "<a href="#volumeclaim" title="VolumeClaim">VolumeClaim</a>" : <i>[ <a href="volumeclaimdefinition.md">VolumeClaimDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::StackPath::ComputeWorkload
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#slug" title="Slug">Slug</a>: <i>String</i>
    <a href="#container" title="Container">Container</a>: <i>
      - <a href="containerdefinition.md">ContainerDefinition</a></i>
    <a href="#imagepullcredentials" title="ImagePullCredentials">ImagePullCredentials</a>: <i>
      - <a href="imagepullcredentialsdefinition.md">ImagePullCredentialsDefinition</a></i>
    <a href="#instances" title="Instances">Instances</a>: <i>
      - <a href="instancesdefinition.md">InstancesDefinition</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a></i>
    <a href="#target" title="Target">Target</a>: <i>
      - <a href="targetdefinition.md">TargetDefinition</a></i>
    <a href="#virtualmachine" title="VirtualMachine">VirtualMachine</a>: <i>
      - <a href="virtualmachinedefinition.md">VirtualMachineDefinition</a></i>
    <a href="#volumeclaim" title="VolumeClaim">VolumeClaim</a>: <i>
      - <a href="volumeclaimdefinition.md">VolumeClaimDefinition</a></i>
</pre>

## Properties

#### Annotations

Key/value pairs that define StackPath-specific workload configuration.

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Key/value pairs of arbitrary label names and values that can be referenced as [selectors](#selectors) by [network policies](/docs/providers/stackpath/r/compute_network_policy.html).

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human readable name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slug

A programmatic name for the workload. Workload slugs are used to build the workload's instance names and cannot be changed after creation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="containerdefinition.md">ContainerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullCredentials

_Required_: No

_Type_: List of <a href="imagepullcredentialsdefinition.md">ImagePullCredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of <a href="instancesdefinition.md">InstancesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="targetdefinition.md">TargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachine

_Required_: No

_Type_: List of <a href="virtualmachinedefinition.md">VirtualMachineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeClaim

_Required_: No

_Type_: List of <a href="volumeclaimdefinition.md">VolumeClaimDefinition</a>

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

