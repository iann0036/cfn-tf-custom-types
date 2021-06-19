# TF::Okta::Factor

Allows you to manage the activation of Okta MFA methods.

This resource allows you to manage Okta MFA methods.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::Factor",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#providerid" title="ProviderId">ProviderId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::Factor
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#providerid" title="ProviderId">ProviderId</a>: <i>String</i>
</pre>

## Properties

#### Active

Whether to activate the provider, by default, it is set to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderId

The MFA provider name.
Allowed values are `"duo"`, `"fido_u2f"`, `"fido_webauthn"`, `"google_otp"`, `"okta_call"`, `"okta_otp"`, `"okta_password"`, `"okta_push"`, `"okta_question"`, `"okta_sms"`, `"okta_email"`, `"rsa_token"`, `"symantec_vip"`, `"yubikey_token"`, or `"hotp"`.

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

