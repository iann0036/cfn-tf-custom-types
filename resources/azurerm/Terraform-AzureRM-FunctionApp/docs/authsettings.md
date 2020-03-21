# Terraform::AzureRM::FunctionApp AuthSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalloginparams" title="AdditionalLoginParams">AdditionalLoginParams</a>" : <i>[ <a href="authsettings-additionalloginparams.md">AdditionalLoginParams</a>, ... ]</i>,
    "<a href="#allowedexternalredirecturls" title="AllowedExternalRedirectUrls">AllowedExternalRedirectUrls</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultprovider" title="DefaultProvider">DefaultProvider</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
    "<a href="#runtimeversion" title="RuntimeVersion">RuntimeVersion</a>" : <i>String</i>,
    "<a href="#tokenrefreshextensionhours" title="TokenRefreshExtensionHours">TokenRefreshExtensionHours</a>" : <i>Double</i>,
    "<a href="#tokenstoreenabled" title="TokenStoreEnabled">TokenStoreEnabled</a>" : <i>Boolean</i>,
    "<a href="#unauthenticatedclientaction" title="UnauthenticatedClientAction">UnauthenticatedClientAction</a>" : <i>String</i>,
    "<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>" : <i>[ <a href="authsettings-activedirectory.md">ActiveDirectory</a>, ... ]</i>,
    "<a href="#facebook" title="Facebook">Facebook</a>" : <i>[ <a href="authsettings-facebook.md">Facebook</a>, ... ]</i>,
    "<a href="#google" title="Google">Google</a>" : <i>[ <a href="authsettings-google.md">Google</a>, ... ]</i>,
    "<a href="#microsoft" title="Microsoft">Microsoft</a>" : <i>[ <a href="authsettings-microsoft.md">Microsoft</a>, ... ]</i>,
    "<a href="#twitter" title="Twitter">Twitter</a>" : <i>[ <a href="authsettings-twitter.md">Twitter</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#additionalloginparams" title="AdditionalLoginParams">AdditionalLoginParams</a>: <i>
      - <a href="authsettings-additionalloginparams.md">AdditionalLoginParams</a></i>
<a href="#allowedexternalredirecturls" title="AllowedExternalRedirectUrls">AllowedExternalRedirectUrls</a>: <i>
      - String</i>
<a href="#defaultprovider" title="DefaultProvider">DefaultProvider</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
<a href="#runtimeversion" title="RuntimeVersion">RuntimeVersion</a>: <i>String</i>
<a href="#tokenrefreshextensionhours" title="TokenRefreshExtensionHours">TokenRefreshExtensionHours</a>: <i>Double</i>
<a href="#tokenstoreenabled" title="TokenStoreEnabled">TokenStoreEnabled</a>: <i>Boolean</i>
<a href="#unauthenticatedclientaction" title="UnauthenticatedClientAction">UnauthenticatedClientAction</a>: <i>String</i>
<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>: <i>
      - <a href="authsettings-activedirectory.md">ActiveDirectory</a></i>
<a href="#facebook" title="Facebook">Facebook</a>: <i>
      - <a href="authsettings-facebook.md">Facebook</a></i>
<a href="#google" title="Google">Google</a>: <i>
      - <a href="authsettings-google.md">Google</a></i>
<a href="#microsoft" title="Microsoft">Microsoft</a>: <i>
      - <a href="authsettings-microsoft.md">Microsoft</a></i>
<a href="#twitter" title="Twitter">Twitter</a>: <i>
      - <a href="authsettings-twitter.md">Twitter</a></i>
</pre>

## Properties

#### AdditionalLoginParams

Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form "key=value".

_Required_: No

_Type_: List of <a href="authsettings-additionalloginparams.md">AdditionalLoginParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedExternalRedirectUrls

External URLs that can be redirected to as part of logging in or logging out of the app.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultProvider

The default provider to use when multiple providers have been set up. Possible values are `AzureActiveDirectory`, `Facebook`, `Google`, `MicrosoftAccount` and `Twitter`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is Authentication enabled?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. https://sts.windows.net/{tenant-guid}/.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeVersion

The runtime version of the Authentication/Authorization module.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenRefreshExtensionHours

The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenStoreEnabled

If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnauthenticatedClientAction

The action to take when an unauthenticated client attempts to access the app. Possible values are `AllowAnonymous` and `RedirectToLoginPage`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveDirectory

_Required_: No

_Type_: List of <a href="authsettings-activedirectory.md">ActiveDirectory</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facebook

_Required_: No

_Type_: List of <a href="authsettings-facebook.md">Facebook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Google

_Required_: No

_Type_: List of <a href="authsettings-google.md">Google</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Microsoft

_Required_: No

_Type_: List of <a href="authsettings-microsoft.md">Microsoft</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Twitter

_Required_: No

_Type_: List of <a href="authsettings-twitter.md">Twitter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

