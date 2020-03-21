# Terraform::VSphere::VappContainer

CloudFormation equivalent of vsphere_vapp_container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::VappContainer",
    "Properties" : {
        "<a href="#cpuexpandable" title="CpuExpandable">CpuExpandable</a>" : <i>Boolean</i>,
        "<a href="#cpulimit" title="CpuLimit">CpuLimit</a>" : <i>Double</i>,
        "<a href="#cpureservation" title="CpuReservation">CpuReservation</a>" : <i>Double</i>,
        "<a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>" : <i>String</i>,
        "<a href="#cpushares" title="CpuShares">CpuShares</a>" : <i>Double</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#memoryexpandable" title="MemoryExpandable">MemoryExpandable</a>" : <i>Boolean</i>,
        "<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>" : <i>Double</i>,
        "<a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>" : <i>Double</i>,
        "<a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>" : <i>String</i>,
        "<a href="#memoryshares" title="MemoryShares">MemoryShares</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentfolderid" title="ParentFolderId">ParentFolderId</a>" : <i>String</i>,
        "<a href="#parentresourcepoolid" title="ParentResourcePoolId">ParentResourcePoolId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::VappContainer
Properties:
    <a href="#cpuexpandable" title="CpuExpandable">CpuExpandable</a>: <i>Boolean</i>
    <a href="#cpulimit" title="CpuLimit">CpuLimit</a>: <i>Double</i>
    <a href="#cpureservation" title="CpuReservation">CpuReservation</a>: <i>Double</i>
    <a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>: <i>String</i>
    <a href="#cpushares" title="CpuShares">CpuShares</a>: <i>Double</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#memoryexpandable" title="MemoryExpandable">MemoryExpandable</a>: <i>Boolean</i>
    <a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>: <i>Double</i>
    <a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>: <i>Double</i>
    <a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>: <i>String</i>
    <a href="#memoryshares" title="MemoryShares">MemoryShares</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentfolderid" title="ParentFolderId">ParentFolderId</a>: <i>String</i>
    <a href="#parentresourcepoolid" title="ParentResourcePoolId">ParentResourcePoolId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### CpuExpandable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuReservation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShares

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributes.md">CustomAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryExpandable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryReservation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShares

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentFolderId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentResourcePoolId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

