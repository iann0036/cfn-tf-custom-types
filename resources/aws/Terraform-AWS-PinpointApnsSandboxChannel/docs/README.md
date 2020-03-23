# Terraform::AWS::PinpointApnsSandboxChannel

Provides a Pinpoint APNs Sandbox Channel resource.

~> **Note:** All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::PinpointApnsSandboxChannel",
    "Properties" : {
        "<a href="#applicationid" title="ApplicationId">ApplicationId</a>" : <i>String</i>,
        "<a href="#bundleid" title="BundleId">BundleId</a>" : <i>String</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#defaultauthenticationmethod" title="DefaultAuthenticationMethod">DefaultAuthenticationMethod</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#tokenkey" title="TokenKey">TokenKey</a>" : <i>String</i>,
        "<a href="#tokenkeyid" title="TokenKeyId">TokenKeyId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::PinpointApnsSandboxChannel
Properties:
    <a href="#applicationid" title="ApplicationId">ApplicationId</a>: <i>String</i>
    <a href="#bundleid" title="BundleId">BundleId</a>: <i>String</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#defaultauthenticationmethod" title="DefaultAuthenticationMethod">DefaultAuthenticationMethod</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#tokenkey" title="TokenKey">TokenKey</a>: <i>String</i>
    <a href="#tokenkeyid" title="TokenKeyId">TokenKeyId</a>: <i>String</i>
</pre>

## Properties

#### ApplicationId

The application ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BundleId

The ID assigned to your iOS app. To find this value, choose Certificates, IDs & Profiles, choose App IDs in the Identifiers section, and choose your app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

The pem encoded TLS Certificate from Apple.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAuthenticationMethod

The default authentication method used for APNs Sandbox.
__NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the channel is enabled or disabled. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The Certificate Private Key file (ie. `.key` file).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

The ID assigned to your Apple developer account team. This value is provided on the Membership page.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenKey

The `.p8` file that you download from your Apple developer account when you create an authentication key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenKeyId

The ID assigned to your signing key. To find this value, choose Certificates, IDs & Profiles, and choose your key in the Keys section.

_Required_: No

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

