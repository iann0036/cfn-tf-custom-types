# Terraform::AWS::CloudformationStack

Provides a CloudFormation Stack resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CloudformationStack",
    "Properties" : {
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#disablerollback" title="DisableRollback">DisableRollback</a>" : <i>Boolean</i>,
        "<a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationarns" title="NotificationArns">NotificationArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#onfailure" title="OnFailure">OnFailure</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#policybody" title="PolicyBody">PolicyBody</a>" : <i>String</i>,
        "<a href="#policyurl" title="PolicyUrl">PolicyUrl</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#templatebody" title="TemplateBody">TemplateBody</a>" : <i>String</i>,
        "<a href="#templateurl" title="TemplateUrl">TemplateUrl</a>" : <i>String</i>,
        "<a href="#timeoutinminutes" title="TimeoutInMinutes">TimeoutInMinutes</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CloudformationStack
Properties:
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - String</i>
    <a href="#disablerollback" title="DisableRollback">DisableRollback</a>: <i>Boolean</i>
    <a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationarns" title="NotificationArns">NotificationArns</a>: <i>
      - String</i>
    <a href="#onfailure" title="OnFailure">OnFailure</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#policybody" title="PolicyBody">PolicyBody</a>: <i>String</i>
    <a href="#policyurl" title="PolicyUrl">PolicyUrl</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#templatebody" title="TemplateBody">TemplateBody</a>: <i>String</i>
    <a href="#templateurl" title="TemplateUrl">TemplateUrl</a>: <i>String</i>
    <a href="#timeoutinminutes" title="TimeoutInMinutes">TimeoutInMinutes</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Capabilities

A list of capabilities.
Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, or `CAPABILITY_AUTO_EXPAND`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRollback

Set to true to disable rollback of the stack if stack creation failed.
Conflicts with `on_failure`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRoleArn

The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Stack name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationArns

A list of SNS topic ARNs to publish stack related events.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnFailure

Action to be taken if stack creation fails. This must be
one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

A map of Parameter structures that specify input parameters for the stack.

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyBody

Structure containing the stack policy body.
Conflicts w/ `policy_url`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyUrl

Location of a file containing the stack policy.
Conflicts w/ `policy_body`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags to associate with this stack.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateBody

Structure containing the template body (max size: 51,200 bytes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUrl

Location of a file containing the template body (max size: 460,800 bytes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutInMinutes

The amount of time that can pass before the stack status becomes `CREATE_FAILED`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

#### Outputs

Returns the <code>Outputs</code> value.

