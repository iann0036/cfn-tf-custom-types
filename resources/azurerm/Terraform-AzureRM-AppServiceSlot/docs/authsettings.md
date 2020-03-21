# Terraform::AzureRM::AppServiceSlot AuthSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalloginparams" title="AdditionalLoginParams">AdditionalLoginParams</a>" : <i>[ &lt;a href=&#34;authsettings-additionalloginparams.md&#34;&gt;AdditionalLoginParams&lt;/a&gt;, ... ]</i>,
    "<a href="#allowedexternalredirecturls" title="AllowedExternalRedirectUrls">AllowedExternalRedirectUrls</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultprovider" title="DefaultProvider">DefaultProvider</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
    "<a href="#runtimeversion" title="RuntimeVersion">RuntimeVersion</a>" : <i>String</i>,
    "<a href="#tokenrefreshextensionhours" title="TokenRefreshExtensionHours">TokenRefreshExtensionHours</a>" : <i>Double</i>,
    "<a href="#tokenstoreenabled" title="TokenStoreEnabled">TokenStoreEnabled</a>" : <i>Boolean</i>,
    "<a href="#unauthenticatedclientaction" title="UnauthenticatedClientAction">UnauthenticatedClientAction</a>" : <i>String</i>,
    "<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>" : <i>[ &lt;a href=&#34;authsettings-activedirectory.md&#34;&gt;ActiveDirectory&lt;/a&gt;, ... ]</i>,
    "<a href="#facebook" title="Facebook">Facebook</a>" : <i>[ &lt;a href=&#34;authsettings-facebook.md&#34;&gt;Facebook&lt;/a&gt;, ... ]</i>,
    "<a href="#google" title="Google">Google</a>" : <i>[ &lt;a href=&#34;authsettings-google.md&#34;&gt;Google&lt;/a&gt;, ... ]</i>,
    "<a href="#microsoft" title="Microsoft">Microsoft</a>" : <i>[ &lt;a href=&#34;authsettings-microsoft.md&#34;&gt;Microsoft&lt;/a&gt;, ... ]</i>,
    "<a href="#twitter" title="Twitter">Twitter</a>" : <i>[ &lt;a href=&#34;authsettings-twitter.md&#34;&gt;Twitter&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#additionalloginparams" title="AdditionalLoginParams">AdditionalLoginParams</a>: <i>
      - &lt;a href=&#34;authsettings-additionalloginparams.md&#34;&gt;AdditionalLoginParams&lt;/a&gt;</i>
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
      - &lt;a href=&#34;authsettings-activedirectory.md&#34;&gt;ActiveDirectory&lt;/a&gt;</i>
<a href="#facebook" title="Facebook">Facebook</a>: <i>
      - &lt;a href=&#34;authsettings-facebook.md&#34;&gt;Facebook&lt;/a&gt;</i>
<a href="#google" title="Google">Google</a>: <i>
      - &lt;a href=&#34;authsettings-google.md&#34;&gt;Google&lt;/a&gt;</i>
<a href="#microsoft" title="Microsoft">Microsoft</a>: <i>
      - &lt;a href=&#34;authsettings-microsoft.md&#34;&gt;Microsoft&lt;/a&gt;</i>
<a href="#twitter" title="Twitter">Twitter</a>: <i>
      - &lt;a href=&#34;authsettings-twitter.md&#34;&gt;Twitter&lt;/a&gt;</i>
</pre>

## Properties

#### AdditionalLoginParams

_Required_: No
_Type_: List of &lt;a href=&#34;authsettings-additionalloginparams.md&#34;&gt;AdditionalLoginParams&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedExternalRedirectUrls

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultProvider

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenRefreshExtensionHours

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenStoreEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnauthenticatedClientAction

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveDirectory

_Required_: No
_Type_: List of &lt;a href=&#34;authsettings-activedirectory.md&#34;&gt;ActiveDirectory&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facebook

_Required_: No
_Type_: List of &lt;a href=&#34;authsettings-facebook.md&#34;&gt;Facebook&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Google

_Required_: No
_Type_: List of &lt;a href=&#34;authsettings-google.md&#34;&gt;Google&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Microsoft

_Required_: No
_Type_: List of &lt;a href=&#34;authsettings-microsoft.md&#34;&gt;Microsoft&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Twitter

_Required_: No
_Type_: List of &lt;a href=&#34;authsettings-twitter.md&#34;&gt;Twitter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

