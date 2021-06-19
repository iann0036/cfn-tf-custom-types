# TF::AWS::CognitoUserPoolUiCustomization

Provides a Cognito User Pool UI Customization resource.

~> **Note:** To use this resource, the user pool must have a domain associated with it. For more information, see the Amazon Cognito Developer Guide on [Customizing the Built-in Sign-In and Sign-up Webpages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-ui-customization.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CognitoUserPoolUiCustomization",
    "Properties" : {
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#css" title="Css">Css</a>" : <i>String</i>,
        "<a href="#imagefile" title="ImageFile">ImageFile</a>" : <i>String</i>,
        "<a href="#userpoolid" title="UserPoolId">UserPoolId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CognitoUserPoolUiCustomization
Properties:
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#css" title="Css">Css</a>: <i>String</i>
    <a href="#imagefile" title="ImageFile">ImageFile</a>: <i>String</i>
    <a href="#userpoolid" title="UserPoolId">UserPoolId</a>: <i>String</i>
</pre>

## Properties

#### ClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Css

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolId

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

#### CreationDate

Returns the <code>CreationDate</code> value.

#### CssVersion

Returns the <code>CssVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### ImageUrl

Returns the <code>ImageUrl</code> value.

#### LastModifiedDate

Returns the <code>LastModifiedDate</code> value.

