# TF::Spotinst::OceanAksVirtualNodeGroup

Manages a Spotinst Ocean AKS Virtual Node Group resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::OceanAksVirtualNodeGroup",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oceanid" title="OceanId">OceanId</a>" : <i>String</i>,
        "<a href="#autoscale" title="Autoscale">Autoscale</a>" : <i>[ <a href="autoscaledefinition.md">AutoscaleDefinition</a>, ... ]</i>,
        "<a href="#label" title="Label">Label</a>" : <i>[ <a href="labeldefinition.md">LabelDefinition</a>, ... ]</i>,
        "<a href="#launchspecification" title="LaunchSpecification">LaunchSpecification</a>" : <i>[ <a href="launchspecificationdefinition.md">LaunchSpecificationDefinition</a>, ... ]</i>,
        "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>, ... ]</i>,
        "<a href="#taint" title="Taint">Taint</a>" : <i>[ <a href="taintdefinition.md">TaintDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::OceanAksVirtualNodeGroup
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oceanid" title="OceanId">OceanId</a>: <i>String</i>
    <a href="#autoscale" title="Autoscale">Autoscale</a>: <i>
      - <a href="autoscaledefinition.md">AutoscaleDefinition</a></i>
    <a href="#label" title="Label">Label</a>: <i>
      - <a href="labeldefinition.md">LabelDefinition</a></i>
    <a href="#launchspecification" title="LaunchSpecification">LaunchSpecification</a>: <i>
      - <a href="launchspecificationdefinition.md">LaunchSpecificationDefinition</a></i>
    <a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a></i>
    <a href="#taint" title="Taint">Taint</a>: <i>
      - <a href="taintdefinition.md">TaintDefinition</a></i>
</pre>

## Properties

#### Name

Set name for the virtual node group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OceanId

The Ocean cluster ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscale

_Required_: No

_Type_: List of <a href="autoscaledefinition.md">AutoscaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: List of <a href="labeldefinition.md">LabelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchSpecification

_Required_: No

_Type_: List of <a href="launchspecificationdefinition.md">LaunchSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taint

_Required_: No

_Type_: List of <a href="taintdefinition.md">TaintDefinition</a>

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

