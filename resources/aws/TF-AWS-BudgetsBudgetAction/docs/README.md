# TF::AWS::BudgetsBudgetAction

Provides a budget action resource. Budget actions are cost savings controls that run either automatically on your behalf or by using a workflow approval process.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::BudgetsBudgetAction",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#actiontype" title="ActionType">ActionType</a>" : <i>String</i>,
        "<a href="#approvalmodel" title="ApprovalModel">ApprovalModel</a>" : <i>String</i>,
        "<a href="#budgetname" title="BudgetName">BudgetName</a>" : <i>String</i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#notificationtype" title="NotificationType">NotificationType</a>" : <i>String</i>,
        "<a href="#actionthreshold" title="ActionThreshold">ActionThreshold</a>" : <i>[ <a href="actionthresholddefinition.md">ActionThresholdDefinition</a>, ... ]</i>,
        "<a href="#definition" title="Definition">Definition</a>" : <i>[ <a href="definitiondefinition.md">DefinitionDefinition</a>, ... ]</i>,
        "<a href="#subscriber" title="Subscriber">Subscriber</a>" : <i>[ <a href="subscriberdefinition.md">SubscriberDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::BudgetsBudgetAction
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#actiontype" title="ActionType">ActionType</a>: <i>String</i>
    <a href="#approvalmodel" title="ApprovalModel">ApprovalModel</a>: <i>String</i>
    <a href="#budgetname" title="BudgetName">BudgetName</a>: <i>String</i>
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
    <a href="#notificationtype" title="NotificationType">NotificationType</a>: <i>String</i>
    <a href="#actionthreshold" title="ActionThreshold">ActionThreshold</a>: <i>
      - <a href="actionthresholddefinition.md">ActionThresholdDefinition</a></i>
    <a href="#definition" title="Definition">Definition</a>: <i>
      - <a href="definitiondefinition.md">DefinitionDefinition</a></i>
    <a href="#subscriber" title="Subscriber">Subscriber</a>: <i>
      - <a href="subscriberdefinition.md">SubscriberDefinition</a></i>
</pre>

## Properties

#### AccountId

The ID of the target account for budget. Will use current user's account_id by default if omitted.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionType

The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition. Valid values are `APPLY_IAM_POLICY`, `APPLY_SCP_POLICY`, and `RUN_SSM_DOCUMENTS`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApprovalModel

This specifies if the action needs manual or automatic approval. Valid values are `AUTOMATIC` and `MANUAL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BudgetName

The name of a budget.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

The role passed for action execution and reversion. Roles and actions must be in the same account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationType

The type of a notification. Valid values are `ACTUAL` or `FORECASTED`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionThreshold

_Required_: No

_Type_: List of <a href="actionthresholddefinition.md">ActionThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Definition

_Required_: No

_Type_: List of <a href="definitiondefinition.md">DefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subscriber

_Required_: No

_Type_: List of <a href="subscriberdefinition.md">SubscriberDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActionId

Returns the <code>ActionId</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

