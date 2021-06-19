# TF::AWS::CloudwatchEventTarget

Provides an EventBridge Target resource.

~> **Note:** EventBridge was formerly known as CloudWatch Events. The functionality is identical.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchEventTarget",
    "Properties" : {
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#eventbusname" title="EventBusName">EventBusName</a>" : <i>String</i>,
        "<a href="#input" title="Input">Input</a>" : <i>String</i>,
        "<a href="#inputpath" title="InputPath">InputPath</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>String</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>,
        "<a href="#batchtarget" title="BatchTarget">BatchTarget</a>" : <i>[ <a href="batchtargetdefinition.md">BatchTargetDefinition</a>, ... ]</i>,
        "<a href="#deadletterconfig" title="DeadLetterConfig">DeadLetterConfig</a>" : <i>[ <a href="deadletterconfigdefinition.md">DeadLetterConfigDefinition</a>, ... ]</i>,
        "<a href="#ecstarget" title="EcsTarget">EcsTarget</a>" : <i>[ <a href="ecstargetdefinition.md">EcsTargetDefinition</a>, ... ]</i>,
        "<a href="#httptarget" title="HttpTarget">HttpTarget</a>" : <i>[ <a href="httptargetdefinition.md">HttpTargetDefinition</a>, ... ]</i>,
        "<a href="#inputtransformer" title="InputTransformer">InputTransformer</a>" : <i>[ <a href="inputtransformerdefinition.md">InputTransformerDefinition</a>, ... ]</i>,
        "<a href="#kinesistarget" title="KinesisTarget">KinesisTarget</a>" : <i>[ <a href="kinesistargetdefinition.md">KinesisTargetDefinition</a>, ... ]</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>, ... ]</i>,
        "<a href="#runcommandtargets" title="RunCommandTargets">RunCommandTargets</a>" : <i>[ <a href="runcommandtargetsdefinition.md">RunCommandTargetsDefinition</a>, ... ]</i>,
        "<a href="#sqstarget" title="SqsTarget">SqsTarget</a>" : <i>[ <a href="sqstargetdefinition.md">SqsTargetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchEventTarget
Properties:
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#eventbusname" title="EventBusName">EventBusName</a>: <i>String</i>
    <a href="#input" title="Input">Input</a>: <i>String</i>
    <a href="#inputpath" title="InputPath">InputPath</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>String</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
    <a href="#batchtarget" title="BatchTarget">BatchTarget</a>: <i>
      - <a href="batchtargetdefinition.md">BatchTargetDefinition</a></i>
    <a href="#deadletterconfig" title="DeadLetterConfig">DeadLetterConfig</a>: <i>
      - <a href="deadletterconfigdefinition.md">DeadLetterConfigDefinition</a></i>
    <a href="#ecstarget" title="EcsTarget">EcsTarget</a>: <i>
      - <a href="ecstargetdefinition.md">EcsTargetDefinition</a></i>
    <a href="#httptarget" title="HttpTarget">HttpTarget</a>: <i>
      - <a href="httptargetdefinition.md">HttpTargetDefinition</a></i>
    <a href="#inputtransformer" title="InputTransformer">InputTransformer</a>: <i>
      - <a href="inputtransformerdefinition.md">InputTransformerDefinition</a></i>
    <a href="#kinesistarget" title="KinesisTarget">KinesisTarget</a>: <i>
      - <a href="kinesistargetdefinition.md">KinesisTargetDefinition</a></i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicydefinition.md">RetryPolicyDefinition</a></i>
    <a href="#runcommandtargets" title="RunCommandTargets">RunCommandTargets</a>: <i>
      - <a href="runcommandtargetsdefinition.md">RunCommandTargetsDefinition</a></i>
    <a href="#sqstarget" title="SqsTarget">SqsTarget</a>: <i>
      - <a href="sqstargetdefinition.md">SqsTargetDefinition</a></i>
</pre>

## Properties

#### Arn

The Amazon Resource Name (ARN) of the target.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventBusName

The event bus to associate with the rule. If you omit this, the `default` event bus is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Input

Valid JSON text passed to the target. Conflicts with `input_path` and `input_transformer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputPath

The value of the [JSONPath](http://goessner.net/articles/JsonPath/) that is used for extracting part of the matched event when passing it to the target. Conflicts with `input` and `input_transformer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

The name of the rule you want to add targets to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

The unique target assignment ID.  If missing, will generate a random, unique id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchTarget

_Required_: No

_Type_: List of <a href="batchtargetdefinition.md">BatchTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadLetterConfig

_Required_: No

_Type_: List of <a href="deadletterconfigdefinition.md">DeadLetterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsTarget

_Required_: No

_Type_: List of <a href="ecstargetdefinition.md">EcsTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpTarget

_Required_: No

_Type_: List of <a href="httptargetdefinition.md">HttpTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputTransformer

_Required_: No

_Type_: List of <a href="inputtransformerdefinition.md">InputTransformerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisTarget

_Required_: No

_Type_: List of <a href="kinesistargetdefinition.md">KinesisTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunCommandTargets

_Required_: No

_Type_: List of <a href="runcommandtargetsdefinition.md">RunCommandTargetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsTarget

_Required_: No

_Type_: List of <a href="sqstargetdefinition.md">SqsTargetDefinition</a>

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

