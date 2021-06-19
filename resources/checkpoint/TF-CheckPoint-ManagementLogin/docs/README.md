# TF::CheckPoint::ManagementLogin

This command resource allows you to log in to the server with username and password.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementLogin",
    "Properties" : {
        "<a href="#continuelastsession" title="ContinueLastSession">ContinueLastSession</a>" : <i>Boolean</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#enterlastpublishedsession" title="EnterLastPublishedSession">EnterLastPublishedSession</a>" : <i>Boolean</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
        "<a href="#sessioncomments" title="SessionComments">SessionComments</a>" : <i>String</i>,
        "<a href="#sessiondescription" title="SessionDescription">SessionDescription</a>" : <i>String</i>,
        "<a href="#sessionname" title="SessionName">SessionName</a>" : <i>String</i>,
        "<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>" : <i>Double</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementLogin
Properties:
    <a href="#continuelastsession" title="ContinueLastSession">ContinueLastSession</a>: <i>Boolean</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#enterlastpublishedsession" title="EnterLastPublishedSession">EnterLastPublishedSession</a>: <i>Boolean</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
    <a href="#sessioncomments" title="SessionComments">SessionComments</a>: <i>String</i>
    <a href="#sessiondescription" title="SessionDescription">SessionDescription</a>: <i>String</i>
    <a href="#sessionname" title="SessionName">SessionName</a>: <i>String</i>
    <a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>: <i>Double</i>
    <a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### ContinueLastSession

When 'continue-last-session' is set to 'True', the new session would continue where the last session was stopped. This option is available when the administrator has only one session that can be continued. If there is more than one session, see 'switch-session' API.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Use domain to login to specific domain. Domain can be identified by name or UID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterLastPublishedSession

Login to the last published session. Such login is done with the Read Only permissions.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Administrator password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

Login with Read Only permissions. This parameter is not considered in case continue-last-session is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionComments

Session comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionDescription

Session description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionName

Session unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTimeout

Session expiration timeout in seconds. Default 600 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

Session unique identifier. Specify it to publish a different session than the one you currently use.

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

