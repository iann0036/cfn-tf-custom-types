# TF::AVI::Systemconfiguration PortalConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowbasicauthentication" title="AllowBasicAuthentication">AllowBasicAuthentication</a>" : <i>Boolean</i>,
    "<a href="#apiforcetimeout" title="ApiForceTimeout">ApiForceTimeout</a>" : <i>Double</i>,
    "<a href="#disableremoteclishell" title="DisableRemoteCliShell">DisableRemoteCliShell</a>" : <i>Boolean</i>,
    "<a href="#disableswagger" title="DisableSwagger">DisableSwagger</a>" : <i>Boolean</i>,
    "<a href="#enableclickjackingprotection" title="EnableClickjackingProtection">EnableClickjackingProtection</a>" : <i>Boolean</i>,
    "<a href="#enablehttp" title="EnableHttp">EnableHttp</a>" : <i>Boolean</i>,
    "<a href="#enablehttps" title="EnableHttps">EnableHttps</a>" : <i>Boolean</i>,
    "<a href="#httpport" title="HttpPort">HttpPort</a>" : <i>Double</i>,
    "<a href="#httpsport" title="HttpsPort">HttpsPort</a>" : <i>Double</i>,
    "<a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>" : <i>Double</i>,
    "<a href="#passwordstrengthcheck" title="PasswordStrengthCheck">PasswordStrengthCheck</a>" : <i>Boolean</i>,
    "<a href="#redirecttohttps" title="RedirectToHttps">RedirectToHttps</a>" : <i>Boolean</i>,
    "<a href="#sslkeyandcertificaterefs" title="SslkeyandcertificateRefs">SslkeyandcertificateRefs</a>" : <i>[ String, ... ]</i>,
    "<a href="#sslprofileref" title="SslprofileRef">SslprofileRef</a>" : <i>String</i>,
    "<a href="#useuuidfrominput" title="UseUuidFromInput">UseUuidFromInput</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#allowbasicauthentication" title="AllowBasicAuthentication">AllowBasicAuthentication</a>: <i>Boolean</i>
<a href="#apiforcetimeout" title="ApiForceTimeout">ApiForceTimeout</a>: <i>Double</i>
<a href="#disableremoteclishell" title="DisableRemoteCliShell">DisableRemoteCliShell</a>: <i>Boolean</i>
<a href="#disableswagger" title="DisableSwagger">DisableSwagger</a>: <i>Boolean</i>
<a href="#enableclickjackingprotection" title="EnableClickjackingProtection">EnableClickjackingProtection</a>: <i>Boolean</i>
<a href="#enablehttp" title="EnableHttp">EnableHttp</a>: <i>Boolean</i>
<a href="#enablehttps" title="EnableHttps">EnableHttps</a>: <i>Boolean</i>
<a href="#httpport" title="HttpPort">HttpPort</a>: <i>Double</i>
<a href="#httpsport" title="HttpsPort">HttpsPort</a>: <i>Double</i>
<a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>: <i>Double</i>
<a href="#passwordstrengthcheck" title="PasswordStrengthCheck">PasswordStrengthCheck</a>: <i>Boolean</i>
<a href="#redirecttohttps" title="RedirectToHttps">RedirectToHttps</a>: <i>Boolean</i>
<a href="#sslkeyandcertificaterefs" title="SslkeyandcertificateRefs">SslkeyandcertificateRefs</a>: <i>
      - String</i>
<a href="#sslprofileref" title="SslprofileRef">SslprofileRef</a>: <i>String</i>
<a href="#useuuidfrominput" title="UseUuidFromInput">UseUuidFromInput</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowBasicAuthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiForceTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRemoteCliShell

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSwagger

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClickjackingProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumPasswordLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordStrengthCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectToHttps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslkeyandcertificateRefs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslprofileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseUuidFromInput

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

