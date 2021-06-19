# TF::Dome9::AttachIamSafe

Attach IAM safe to AWS cloud account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::AttachIamSafe",
    "Properties" : {
        "<a href="#awscloudaccountid" title="AwsCloudAccountId">AwsCloudAccountId</a>" : <i>String</i>,
        "<a href="#awsgrouparn" title="AwsGroupArn">AwsGroupArn</a>" : <i>String</i>,
        "<a href="#awspolicyarn" title="AwsPolicyArn">AwsPolicyArn</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::AttachIamSafe
Properties:
    <a href="#awscloudaccountid" title="AwsCloudAccountId">AwsCloudAccountId</a>: <i>String</i>
    <a href="#awsgrouparn" title="AwsGroupArn">AwsGroupArn</a>: <i>String</i>
    <a href="#awspolicyarn" title="AwsPolicyArn">AwsPolicyArn</a>: <i>String</i>
</pre>

## Properties

#### AwsCloudAccountId

AWS cloud account to attach IAM safe to it.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsGroupArn

AWS group arn.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsPolicyArn

AWS policy arn.

_Required_: Yes

_Type_: String

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

#### Mode

Returns the <code>Mode</code> value.

