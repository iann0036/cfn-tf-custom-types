# Terraform::AWS::QuicksightUser

Resource for managing QuickSight User

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::QuicksightUser",
    "Properties" : {
        "<a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#iamarn" title="IamArn">IamArn</a>" : <i>String</i>,
        "<a href="#identitytype" title="IdentityType">IdentityType</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#sessionname" title="SessionName">SessionName</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>,
        "<a href="#userrole" title="UserRole">UserRole</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::QuicksightUser
Properties:
    <a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#iamarn" title="IamArn">IamArn</a>: <i>String</i>
    <a href="#identitytype" title="IdentityType">IdentityType</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#sessionname" title="SessionName">SessionName</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
    <a href="#userrole" title="UserRole">UserRole</a>: <i>String</i>
</pre>

## Properties

#### AwsAccountId

The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The email address of the user that you want to register.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamArn

The ARN of the IAM user or role that you are registering with Amazon QuickSight.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityType

Amazon QuickSight supports several ways of managing the identity of users. This parameter accepts either  `IAM` or `QUICKSIGHT`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

The namespace. Currently, you should set this to `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionName

The name of the IAM session to use when assuming roles that can embed QuickSight dashboards.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

The Amazon QuickSight user name that you want to create for the user you are registering.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserRole

The Amazon QuickSight role of the user. The user role can be one of the following: `READER`, `AUTHOR`, or `ADMIN`.

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

