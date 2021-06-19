# TF::AWS::ConfigOrganizationManagedRule

Manages a Config Organization Managed Rule. More information about these rules can be found in the [Enabling AWS Config Rules Across all Accounts in Your Organization](https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html) and [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) documentation. For working with Organization Custom Rules (those invoking a custom Lambda Function), see the [`aws_config_organization_custom_rule` resource](/docs/providers/aws/r/config_organization_custom_rule.html).

~> **NOTE:** This resource must be created in the Organization master account and rules will include the master account unless its ID is added to the `excluded_accounts` argument.

~> **NOTE:** Every Organization account except those configured in the `excluded_accounts` argument must have a Configuration Recorder with proper IAM permissions before the rule will successfully create or update. See also...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ConfigOrganizationManagedRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#excludedaccounts" title="ExcludedAccounts">ExcludedAccounts</a>" : <i>[ String, ... ]</i>,
        "<a href="#inputparameters" title="InputParameters">InputParameters</a>" : <i>String</i>,
        "<a href="#maximumexecutionfrequency" title="MaximumExecutionFrequency">MaximumExecutionFrequency</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourceidscope" title="ResourceIdScope">ResourceIdScope</a>" : <i>String</i>,
        "<a href="#resourcetypesscope" title="ResourceTypesScope">ResourceTypesScope</a>" : <i>[ String, ... ]</i>,
        "<a href="#ruleidentifier" title="RuleIdentifier">RuleIdentifier</a>" : <i>String</i>,
        "<a href="#tagkeyscope" title="TagKeyScope">TagKeyScope</a>" : <i>String</i>,
        "<a href="#tagvaluescope" title="TagValueScope">TagValueScope</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ConfigOrganizationManagedRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#excludedaccounts" title="ExcludedAccounts">ExcludedAccounts</a>: <i>
      - String</i>
    <a href="#inputparameters" title="InputParameters">InputParameters</a>: <i>String</i>
    <a href="#maximumexecutionfrequency" title="MaximumExecutionFrequency">MaximumExecutionFrequency</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourceidscope" title="ResourceIdScope">ResourceIdScope</a>: <i>String</i>
    <a href="#resourcetypesscope" title="ResourceTypesScope">ResourceTypesScope</a>: <i>
      - String</i>
    <a href="#ruleidentifier" title="RuleIdentifier">RuleIdentifier</a>: <i>String</i>
    <a href="#tagkeyscope" title="TagKeyScope">TagKeyScope</a>: <i>String</i>
    <a href="#tagvaluescope" title="TagValueScope">TagValueScope</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

Description of the rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedAccounts

List of AWS account identifiers to exclude from the rule.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputParameters

A string in JSON format that is passed to the AWS Config Rule Lambda Function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumExecutionFrequency

The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceIdScope

Identifier of the AWS resource to evaluate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceTypesScope

List of types of AWS resources to evaluate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleIdentifier

Identifier of an available AWS Config Managed Rule to call. For available values, see the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) documentation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagKeyScope

Tag key of AWS resources to evaluate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagValueScope

Tag value of AWS resources to evaluate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

