# Terraform::AWS::SesReceiptRule

CloudFormation equivalent of aws_ses_receipt_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SesReceiptRule",
    "Properties" : {
        "<a href="#after" title="After">After</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>,
        "<a href="#rulesetname" title="RuleSetName">RuleSetName</a>" : <i>String</i>,
        "<a href="#scanenabled" title="ScanEnabled">ScanEnabled</a>" : <i>Boolean</i>,
        "<a href="#tlspolicy" title="TlsPolicy">TlsPolicy</a>" : <i>String</i>,
        "<a href="#addheaderaction" title="AddHeaderAction">AddHeaderAction</a>" : <i>[ <a href="addheaderaction.md">AddHeaderAction</a>, ... ]</i>,
        "<a href="#bounceaction" title="BounceAction">BounceAction</a>" : <i>[ <a href="bounceaction.md">BounceAction</a>, ... ]</i>,
        "<a href="#lambdaaction" title="LambdaAction">LambdaAction</a>" : <i>[ <a href="lambdaaction.md">LambdaAction</a>, ... ]</i>,
        "<a href="#s3action" title="S3Action">S3Action</a>" : <i>[ <a href="s3action.md">S3Action</a>, ... ]</i>,
        "<a href="#snsaction" title="SnsAction">SnsAction</a>" : <i>[ <a href="snsaction.md">SnsAction</a>, ... ]</i>,
        "<a href="#stopaction" title="StopAction">StopAction</a>" : <i>[ <a href="stopaction.md">StopAction</a>, ... ]</i>,
        "<a href="#workmailaction" title="WorkmailAction">WorkmailAction</a>" : <i>[ <a href="workmailaction.md">WorkmailAction</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SesReceiptRule
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
      - <a href="addheaderaction.md">AddHeaderAction</a></i>
    <a href="#bounceaction" title="BounceAction">BounceAction</a>: <i>
      - <a href="bounceaction.md">BounceAction</a></i>
    <a href="#lambdaaction" title="LambdaAction">LambdaAction</a>: <i>
      - <a href="lambdaaction.md">LambdaAction</a></i>
    <a href="#s3action" title="S3Action">S3Action</a>: <i>
      - <a href="s3action.md">S3Action</a></i>
    <a href="#snsaction" title="SnsAction">SnsAction</a>: <i>
      - <a href="snsaction.md">SnsAction</a></i>
    <a href="#stopaction" title="StopAction">StopAction</a>: <i>
      - <a href="stopaction.md">StopAction</a></i>
    <a href="#workmailaction" title="WorkmailAction">WorkmailAction</a>: <i>
      - <a href="workmailaction.md">WorkmailAction</a></i>
</pre>

## Properties

#### After

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSetName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddHeaderAction

_Required_: No

_Type_: List of <a href="addheaderaction.md">AddHeaderAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BounceAction

_Required_: No

_Type_: List of <a href="bounceaction.md">BounceAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaAction

_Required_: No

_Type_: List of <a href="lambdaaction.md">LambdaAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Action

_Required_: No

_Type_: List of <a href="s3action.md">S3Action</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsAction

_Required_: No

_Type_: List of <a href="snsaction.md">SnsAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopAction

_Required_: No

_Type_: List of <a href="stopaction.md">StopAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkmailAction

_Required_: No

_Type_: List of <a href="workmailaction.md">WorkmailAction</a>

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

