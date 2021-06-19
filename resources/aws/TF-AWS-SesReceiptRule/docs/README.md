# TF::AWS::SesReceiptRule

Provides an SES receipt rule resource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SesReceiptRule",
    "Properties" : {
        "<a href="#after" title="After">After</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>,
        "<a href="#rulesetname" title="RuleSetName">RuleSetName</a>" : <i>String</i>,
        "<a href="#scanenabled" title="ScanEnabled">ScanEnabled</a>" : <i>Boolean</i>,
        "<a href="#tlspolicy" title="TlsPolicy">TlsPolicy</a>" : <i>String</i>,
        "<a href="#addheaderaction" title="AddHeaderAction">AddHeaderAction</a>" : <i>[ <a href="addheaderactiondefinition.md">AddHeaderActionDefinition</a>, ... ]</i>,
        "<a href="#bounceaction" title="BounceAction">BounceAction</a>" : <i>[ <a href="bounceactiondefinition.md">BounceActionDefinition</a>, ... ]</i>,
        "<a href="#lambdaaction" title="LambdaAction">LambdaAction</a>" : <i>[ <a href="lambdaactiondefinition.md">LambdaActionDefinition</a>, ... ]</i>,
        "<a href="#s3action" title="S3Action">S3Action</a>" : <i>[ <a href="s3actiondefinition.md">S3ActionDefinition</a>, ... ]</i>,
        "<a href="#snsaction" title="SnsAction">SnsAction</a>" : <i>[ <a href="snsactiondefinition.md">SnsActionDefinition</a>, ... ]</i>,
        "<a href="#stopaction" title="StopAction">StopAction</a>" : <i>[ <a href="stopactiondefinition.md">StopActionDefinition</a>, ... ]</i>,
        "<a href="#workmailaction" title="WorkmailAction">WorkmailAction</a>" : <i>[ <a href="workmailactiondefinition.md">WorkmailActionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SesReceiptRule
Properties:
    <a href="#after" title="After">After</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
    <a href="#rulesetname" title="RuleSetName">RuleSetName</a>: <i>String</i>
    <a href="#scanenabled" title="ScanEnabled">ScanEnabled</a>: <i>Boolean</i>
    <a href="#tlspolicy" title="TlsPolicy">TlsPolicy</a>: <i>String</i>
    <a href="#addheaderaction" title="AddHeaderAction">AddHeaderAction</a>: <i>
      - <a href="addheaderactiondefinition.md">AddHeaderActionDefinition</a></i>
    <a href="#bounceaction" title="BounceAction">BounceAction</a>: <i>
      - <a href="bounceactiondefinition.md">BounceActionDefinition</a></i>
    <a href="#lambdaaction" title="LambdaAction">LambdaAction</a>: <i>
      - <a href="lambdaactiondefinition.md">LambdaActionDefinition</a></i>
    <a href="#s3action" title="S3Action">S3Action</a>: <i>
      - <a href="s3actiondefinition.md">S3ActionDefinition</a></i>
    <a href="#snsaction" title="SnsAction">SnsAction</a>: <i>
      - <a href="snsactiondefinition.md">SnsActionDefinition</a></i>
    <a href="#stopaction" title="StopAction">StopAction</a>: <i>
      - <a href="stopactiondefinition.md">StopActionDefinition</a></i>
    <a href="#workmailaction" title="WorkmailAction">WorkmailAction</a>: <i>
      - <a href="workmailactiondefinition.md">WorkmailActionDefinition</a></i>
</pre>

## Properties

#### After

The name of the rule to place this rule after.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

If true, the rule will be enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

A list of email addresses.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSetName

The name of the rule set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanEnabled

If true, incoming emails will be scanned for spam and viruses.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsPolicy

Require or Optional.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddHeaderAction

_Required_: No

_Type_: List of <a href="addheaderactiondefinition.md">AddHeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BounceAction

_Required_: No

_Type_: List of <a href="bounceactiondefinition.md">BounceActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaAction

_Required_: No

_Type_: List of <a href="lambdaactiondefinition.md">LambdaActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Action

_Required_: No

_Type_: List of <a href="s3actiondefinition.md">S3ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsAction

_Required_: No

_Type_: List of <a href="snsactiondefinition.md">SnsActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopAction

_Required_: No

_Type_: List of <a href="stopactiondefinition.md">StopActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkmailAction

_Required_: No

_Type_: List of <a href="workmailactiondefinition.md">WorkmailActionDefinition</a>

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

