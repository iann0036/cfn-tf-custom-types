# TF::AWS::CloudwatchLogResourcePolicy

Provides a resource to manage a CloudWatch log resource policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchLogResourcePolicy",
    "Properties" : {
        "<a href="#policydocument" title="PolicyDocument">PolicyDocument</a>" : <i>String</i>,
        "<a href="#policyname" title="PolicyName">PolicyName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchLogResourcePolicy
Properties:
    <a href="#policydocument" title="PolicyDocument">PolicyDocument</a>: <i>String</i>
    <a href="#policyname" title="PolicyName">PolicyName</a>: <i>String</i>
</pre>

## Properties

#### PolicyDocument

Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyName

Name of the resource policy.

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

