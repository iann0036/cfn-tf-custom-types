# TF::Alicloud::BrainIndustrialPidLoop

CloudFormation equivalent of alicloud_brain_industrial_pid_loop

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::BrainIndustrialPidLoop",
    "Properties" : {
        "<a href="#pidloopconfiguration" title="PidLoopConfiguration">PidLoopConfiguration</a>" : <i>String</i>,
        "<a href="#pidloopdcstype" title="PidLoopDcsType">PidLoopDcsType</a>" : <i>String</i>,
        "<a href="#pidloopdesc" title="PidLoopDesc">PidLoopDesc</a>" : <i>String</i>,
        "<a href="#pidloopiscrucial" title="PidLoopIsCrucial">PidLoopIsCrucial</a>" : <i>Boolean</i>,
        "<a href="#pidloopname" title="PidLoopName">PidLoopName</a>" : <i>String</i>,
        "<a href="#pidlooptype" title="PidLoopType">PidLoopType</a>" : <i>String</i>,
        "<a href="#pidprojectid" title="PidProjectId">PidProjectId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::BrainIndustrialPidLoop
Properties:
    <a href="#pidloopconfiguration" title="PidLoopConfiguration">PidLoopConfiguration</a>: <i>String</i>
    <a href="#pidloopdcstype" title="PidLoopDcsType">PidLoopDcsType</a>: <i>String</i>
    <a href="#pidloopdesc" title="PidLoopDesc">PidLoopDesc</a>: <i>String</i>
    <a href="#pidloopiscrucial" title="PidLoopIsCrucial">PidLoopIsCrucial</a>: <i>Boolean</i>
    <a href="#pidloopname" title="PidLoopName">PidLoopName</a>: <i>String</i>
    <a href="#pidlooptype" title="PidLoopType">PidLoopType</a>: <i>String</i>
    <a href="#pidprojectid" title="PidProjectId">PidProjectId</a>: <i>String</i>
</pre>

## Properties

#### PidLoopConfiguration

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidLoopDcsType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidLoopDesc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidLoopIsCrucial

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidLoopName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidLoopType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidProjectId

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

