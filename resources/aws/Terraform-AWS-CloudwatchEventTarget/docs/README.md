# Terraform::AWS::CloudwatchEventTarget

CloudFormation equivalent of aws_cloudwatch_event_target

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CloudwatchEventTarget",
    "Properties" : {
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#input" title="Input">Input</a>" : <i>String</i>,
        "<a href="#inputpath" title="InputPath">InputPath</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>String</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>,
        "<a href="#batchtarget" title="BatchTarget">BatchTarget</a>" : <i>[ <a href="batchtarget.md">BatchTarget</a>, ... ]</i>,
        "<a href="#ecstarget" title="EcsTarget">EcsTarget</a>" : <i>[ <a href="ecstarget.md">EcsTarget</a>, ... ]</i>,
        "<a href="#inputtransformer" title="InputTransformer">InputTransformer</a>" : <i>[ <a href="inputtransformer.md">InputTransformer</a>, ... ]</i>,
        "<a href="#kinesistarget" title="KinesisTarget">KinesisTarget</a>" : <i>[ <a href="kinesistarget.md">KinesisTarget</a>, ... ]</i>,
        "<a href="#runcommandtargets" title="RunCommandTargets">RunCommandTargets</a>" : <i>[ <a href="runcommandtargets.md">RunCommandTargets</a>, ... ]</i>,
        "<a href="#sqstarget" title="SqsTarget">SqsTarget</a>" : <i>[ <a href="sqstarget.md">SqsTarget</a>, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ <a href="networkconfiguration.md">NetworkConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CloudwatchEventTarget
Properties:
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#input" title="Input">Input</a>: <i>String</i>
    <a href="#inputpath" title="InputPath">InputPath</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>String</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
    <a href="#batchtarget" title="BatchTarget">BatchTarget</a>: <i>
      - <a href="batchtarget.md">BatchTarget</a></i>
    <a href="#ecstarget" title="EcsTarget">EcsTarget</a>: <i>
      - <a href="ecstarget.md">EcsTarget</a></i>
    <a href="#inputtransformer" title="InputTransformer">InputTransformer</a>: <i>
      - <a href="inputtransformer.md">InputTransformer</a></i>
    <a href="#kinesistarget" title="KinesisTarget">KinesisTarget</a>: <i>
      - <a href="kinesistarget.md">KinesisTarget</a></i>
    <a href="#runcommandtargets" title="RunCommandTargets">RunCommandTargets</a>: <i>
      - <a href="runcommandtargets.md">RunCommandTargets</a></i>
    <a href="#sqstarget" title="SqsTarget">SqsTarget</a>: <i>
      - <a href="sqstarget.md">SqsTarget</a></i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - <a href="networkconfiguration.md">NetworkConfiguration</a></i>
</pre>

## Properties

#### Arn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Input

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchTarget

_Required_: No

_Type_: List of <a href="batchtarget.md">BatchTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsTarget

_Required_: No

_Type_: List of <a href="ecstarget.md">EcsTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputTransformer

_Required_: No

_Type_: List of <a href="inputtransformer.md">InputTransformer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisTarget

_Required_: No

_Type_: List of <a href="kinesistarget.md">KinesisTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunCommandTargets

_Required_: No

_Type_: List of <a href="runcommandtargets.md">RunCommandTargets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsTarget

_Required_: No

_Type_: List of <a href="sqstarget.md">SqsTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of <a href="networkconfiguration.md">NetworkConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

