# Terraform::AWS::DlmLifecyclePolicy

Provides a [Data Lifecycle Manager (DLM) lifecycle policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) for managing snapshots.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DlmLifecyclePolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#policydetails" title="PolicyDetails">PolicyDetails</a>" : <i>[ <a href="policydetails.md">PolicyDetails</a>, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="schedule.md">Schedule</a>, ... ]</i>,
        "<a href="#createrule" title="CreateRule">CreateRule</a>" : <i>[ <a href="createrule.md">CreateRule</a>, ... ]</i>,
        "<a href="#retainrule" title="RetainRule">RetainRule</a>" : <i>[ <a href="retainrule.md">RetainRule</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DlmLifecyclePolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#policydetails" title="PolicyDetails">PolicyDetails</a>: <i>
      - <a href="policydetails.md">PolicyDetails</a></i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="schedule.md">Schedule</a></i>
    <a href="#createrule" title="CreateRule">CreateRule</a>: <i>
      - <a href="createrule.md">CreateRule</a></i>
    <a href="#retainrule" title="RetainRule">RetainRule</a>: <i>
      - <a href="retainrule.md">RetainRule</a></i>
</pre>

## Properties

#### Description

A description for the DLM lifecycle policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

The ARN of an IAM role that is able to be assumed by the DLM service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDetails

_Required_: No

_Type_: List of <a href="policydetails.md">PolicyDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="schedule.md">Schedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateRule

_Required_: No

_Type_: List of <a href="createrule.md">CreateRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainRule

_Required_: No

_Type_: List of <a href="retainrule.md">RetainRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

