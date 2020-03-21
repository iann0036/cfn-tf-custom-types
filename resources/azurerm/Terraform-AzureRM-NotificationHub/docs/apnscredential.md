# Terraform::AzureRM::NotificationHub ApnsCredential

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationmode" title="ApplicationMode">ApplicationMode</a>" : <i>String</i>,
    "<a href="#bundleid" title="BundleId">BundleId</a>" : <i>String</i>,
    "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
    "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#applicationmode" title="ApplicationMode">ApplicationMode</a>: <i>String</i>
<a href="#bundleid" title="BundleId">BundleId</a>: <i>String</i>
<a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
<a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
<a href="#token" title="Token">Token</a>: <i>String</i>
</pre>

## Properties

#### ApplicationMode

The Application Mode which defines which server the APNS Messages should be sent to. Possible values are `Production` and `Sandbox`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BundleId

The Bundle ID of the iOS/macOS application to send push notifications for, such as `com.hashicorp.example`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

The Apple Push Notifications Service (APNS) Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

The ID of the team the Token.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The Push Token associated with the Apple Developer Account. This is the contents of the `key` downloaded from [the Apple Developer Portal](https://developer.apple.com/account/ios/authkey/) between the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` blocks.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

