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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>,
        "<a href="#rulesetname" title="RuleSetName">RuleSetName</a>" : <i>String</i>,
        "<a href="#scanenabled" title="ScanEnabled">ScanEnabled</a>" : <i>Boolean</i>,
        "<a href="#tlspolicy" title="TlsPolicy">TlsPolicy</a>" : <i>String</i>,
        "<a href="#addheaderaction" title="AddHeaderAction">AddHeaderAction</a>" : <i>[ &lt;a href=&#34;addheaderaction.md&#34;&gt;AddHeaderAction&lt;/a&gt;, ... ]</i>,
        "<a href="#bounceaction" title="BounceAction">BounceAction</a>" : <i>[ &lt;a href=&#34;bounceaction.md&#34;&gt;BounceAction&lt;/a&gt;, ... ]</i>,
        "<a href="#lambdaaction" title="LambdaAction">LambdaAction</a>" : <i>[ &lt;a href=&#34;lambdaaction.md&#34;&gt;LambdaAction&lt;/a&gt;, ... ]</i>,
        "<a href="#s3action" title="S3Action">S3Action</a>" : <i>[ &lt;a href=&#34;s3action.md&#34;&gt;S3Action&lt;/a&gt;, ... ]</i>,
        "<a href="#snsaction" title="SnsAction">SnsAction</a>" : <i>[ &lt;a href=&#34;snsaction.md&#34;&gt;SnsAction&lt;/a&gt;, ... ]</i>,
        "<a href="#stopaction" title="StopAction">StopAction</a>" : <i>[ &lt;a href=&#34;stopaction.md&#34;&gt;StopAction&lt;/a&gt;, ... ]</i>,
        "<a href="#workmailaction" title="WorkmailAction">WorkmailAction</a>" : <i>[ &lt;a href=&#34;workmailaction.md&#34;&gt;WorkmailAction&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SesReceiptRule
Properties:
    <a href="#after" title="After">After</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
    <a href="#rulesetname" title="RuleSetName">RuleSetName</a>: <i>String</i>
    <a href="#scanenabled" title="ScanEnabled">ScanEnabled</a>: <i>Boolean</i>
    <a href="#tlspolicy" title="TlsPolicy">TlsPolicy</a>: <i>String</i>
    <a href="#addheaderaction" title="AddHeaderAction">AddHeaderAction</a>: <i>
      - &lt;a href=&#34;addheaderaction.md&#34;&gt;AddHeaderAction&lt;/a&gt;</i>
    <a href="#bounceaction" title="BounceAction">BounceAction</a>: <i>
      - &lt;a href=&#34;bounceaction.md&#34;&gt;BounceAction&lt;/a&gt;</i>
    <a href="#lambdaaction" title="LambdaAction">LambdaAction</a>: <i>
      - &lt;a href=&#34;lambdaaction.md&#34;&gt;LambdaAction&lt;/a&gt;</i>
    <a href="#s3action" title="S3Action">S3Action</a>: <i>
      - &lt;a href=&#34;s3action.md&#34;&gt;S3Action&lt;/a&gt;</i>
    <a href="#snsaction" title="SnsAction">SnsAction</a>: <i>
      - &lt;a href=&#34;snsaction.md&#34;&gt;SnsAction&lt;/a&gt;</i>
    <a href="#stopaction" title="StopAction">StopAction</a>: <i>
      - &lt;a href=&#34;stopaction.md&#34;&gt;StopAction&lt;/a&gt;</i>
    <a href="#workmailaction" title="WorkmailAction">WorkmailAction</a>: <i>
      - &lt;a href=&#34;workmailaction.md&#34;&gt;WorkmailAction&lt;/a&gt;</i>
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

#### Id

_Required_: No

_Type_: String

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

_Type_: List of &lt;a href=&#34;addheaderaction.md&#34;&gt;AddHeaderAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BounceAction

_Required_: No

_Type_: List of &lt;a href=&#34;bounceaction.md&#34;&gt;BounceAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaAction

_Required_: No

_Type_: List of &lt;a href=&#34;lambdaaction.md&#34;&gt;LambdaAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Action

_Required_: No

_Type_: List of &lt;a href=&#34;s3action.md&#34;&gt;S3Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsAction

_Required_: No

_Type_: List of &lt;a href=&#34;snsaction.md&#34;&gt;SnsAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopAction

_Required_: No

_Type_: List of &lt;a href=&#34;stopaction.md&#34;&gt;StopAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkmailAction

_Required_: No

_Type_: List of &lt;a href=&#34;workmailaction.md&#34;&gt;WorkmailAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

