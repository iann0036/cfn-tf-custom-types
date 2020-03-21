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
        "<a href="#batchtarget" title="BatchTarget">BatchTarget</a>" : <i>[ &lt;a href=&#34;batchtarget.md&#34;&gt;BatchTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#ecstarget" title="EcsTarget">EcsTarget</a>" : <i>[ &lt;a href=&#34;ecstarget.md&#34;&gt;EcsTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#inputtransformer" title="InputTransformer">InputTransformer</a>" : <i>[ &lt;a href=&#34;inputtransformer.md&#34;&gt;InputTransformer&lt;/a&gt;, ... ]</i>,
        "<a href="#kinesistarget" title="KinesisTarget">KinesisTarget</a>" : <i>[ &lt;a href=&#34;kinesistarget.md&#34;&gt;KinesisTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#runcommandtargets" title="RunCommandTargets">RunCommandTargets</a>" : <i>[ &lt;a href=&#34;runcommandtargets.md&#34;&gt;RunCommandTargets&lt;/a&gt;, ... ]</i>,
        "<a href="#sqstarget" title="SqsTarget">SqsTarget</a>" : <i>[ &lt;a href=&#34;sqstarget.md&#34;&gt;SqsTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;batchtarget.md&#34;&gt;BatchTarget&lt;/a&gt;</i>
    <a href="#ecstarget" title="EcsTarget">EcsTarget</a>: <i>
      - &lt;a href=&#34;ecstarget.md&#34;&gt;EcsTarget&lt;/a&gt;</i>
    <a href="#inputtransformer" title="InputTransformer">InputTransformer</a>: <i>
      - &lt;a href=&#34;inputtransformer.md&#34;&gt;InputTransformer&lt;/a&gt;</i>
    <a href="#kinesistarget" title="KinesisTarget">KinesisTarget</a>: <i>
      - &lt;a href=&#34;kinesistarget.md&#34;&gt;KinesisTarget&lt;/a&gt;</i>
    <a href="#runcommandtargets" title="RunCommandTargets">RunCommandTargets</a>: <i>
      - &lt;a href=&#34;runcommandtargets.md&#34;&gt;RunCommandTargets&lt;/a&gt;</i>
    <a href="#sqstarget" title="SqsTarget">SqsTarget</a>: <i>
      - &lt;a href=&#34;sqstarget.md&#34;&gt;SqsTarget&lt;/a&gt;</i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;</i>
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

_Type_: List of &lt;a href=&#34;batchtarget.md&#34;&gt;BatchTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsTarget

_Required_: No

_Type_: List of &lt;a href=&#34;ecstarget.md&#34;&gt;EcsTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputTransformer

_Required_: No

_Type_: List of &lt;a href=&#34;inputtransformer.md&#34;&gt;InputTransformer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisTarget

_Required_: No

_Type_: List of &lt;a href=&#34;kinesistarget.md&#34;&gt;KinesisTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunCommandTargets

_Required_: No

_Type_: List of &lt;a href=&#34;runcommandtargets.md&#34;&gt;RunCommandTargets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsTarget

_Required_: No

_Type_: List of &lt;a href=&#34;sqstarget.md&#34;&gt;SqsTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

