# Terraform::AWS::DlmLifecyclePolicy

CloudFormation equivalent of aws_dlm_lifecycle_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DlmLifecyclePolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#policydetails" title="PolicyDetails">PolicyDetails</a>" : <i>[ &lt;a href=&#34;policydetails.md&#34;&gt;PolicyDetails&lt;/a&gt;, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;, ... ]</i>,
        "<a href="#createrule" title="CreateRule">CreateRule</a>" : <i>[ &lt;a href=&#34;createrule.md&#34;&gt;CreateRule&lt;/a&gt;, ... ]</i>,
        "<a href="#retainrule" title="RetainRule">RetainRule</a>" : <i>[ &lt;a href=&#34;retainrule.md&#34;&gt;RetainRule&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DlmLifecyclePolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#policydetails" title="PolicyDetails">PolicyDetails</a>: <i>
      - &lt;a href=&#34;policydetails.md&#34;&gt;PolicyDetails&lt;/a&gt;</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;</i>
    <a href="#createrule" title="CreateRule">CreateRule</a>: <i>
      - &lt;a href=&#34;createrule.md&#34;&gt;CreateRule&lt;/a&gt;</i>
    <a href="#retainrule" title="RetainRule">RetainRule</a>: <i>
      - &lt;a href=&#34;retainrule.md&#34;&gt;RetainRule&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDetails

_Required_: No

_Type_: List of &lt;a href=&#34;policydetails.md&#34;&gt;PolicyDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateRule

_Required_: No

_Type_: List of &lt;a href=&#34;createrule.md&#34;&gt;CreateRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainRule

_Required_: No

_Type_: List of &lt;a href=&#34;retainrule.md&#34;&gt;RetainRule&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

