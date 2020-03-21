# Terraform::Panos::GeneralSettings

CloudFormation equivalent of panos_general_settings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::GeneralSettings",
    "Properties" : {
        "<a href="#dnsprimary" title="DnsPrimary">DnsPrimary</a>" : <i>String</i>,
        "<a href="#dnssecondary" title="DnsSecondary">DnsSecondary</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ntpprimaryaddress" title="NtpPrimaryAddress">NtpPrimaryAddress</a>" : <i>String</i>,
        "<a href="#ntpprimaryalgorithm" title="NtpPrimaryAlgorithm">NtpPrimaryAlgorithm</a>" : <i>String</i>,
        "<a href="#ntpprimaryauthkey" title="NtpPrimaryAuthKey">NtpPrimaryAuthKey</a>" : <i>String</i>,
        "<a href="#ntpprimaryauthtype" title="NtpPrimaryAuthType">NtpPrimaryAuthType</a>" : <i>String</i>,
        "<a href="#ntpprimarykeyid" title="NtpPrimaryKeyId">NtpPrimaryKeyId</a>" : <i>Double</i>,
        "<a href="#ntpsecondaryaddress" title="NtpSecondaryAddress">NtpSecondaryAddress</a>" : <i>String</i>,
        "<a href="#ntpsecondaryalgorithm" title="NtpSecondaryAlgorithm">NtpSecondaryAlgorithm</a>" : <i>String</i>,
        "<a href="#ntpsecondaryauthkey" title="NtpSecondaryAuthKey">NtpSecondaryAuthKey</a>" : <i>String</i>,
        "<a href="#ntpsecondaryauthtype" title="NtpSecondaryAuthType">NtpSecondaryAuthType</a>" : <i>String</i>,
        "<a href="#ntpsecondarykeyid" title="NtpSecondaryKeyId">NtpSecondaryKeyId</a>" : <i>Double</i>,
        "<a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>" : <i>String</i>,
        "<a href="#proxyport" title="ProxyPort">ProxyPort</a>" : <i>Double</i>,
        "<a href="#proxyserver" title="ProxyServer">ProxyServer</a>" : <i>String</i>,
        "<a href="#proxyuser" title="ProxyUser">ProxyUser</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#updateserver" title="UpdateServer">UpdateServer</a>" : <i>String</i>,
        "<a href="#verifyupdateserver" title="VerifyUpdateServer">VerifyUpdateServer</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::GeneralSettings
Properties:
    <a href="#dnsprimary" title="DnsPrimary">DnsPrimary</a>: <i>String</i>
    <a href="#dnssecondary" title="DnsSecondary">DnsSecondary</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ntpprimaryaddress" title="NtpPrimaryAddress">NtpPrimaryAddress</a>: <i>String</i>
    <a href="#ntpprimaryalgorithm" title="NtpPrimaryAlgorithm">NtpPrimaryAlgorithm</a>: <i>String</i>
    <a href="#ntpprimaryauthkey" title="NtpPrimaryAuthKey">NtpPrimaryAuthKey</a>: <i>String</i>
    <a href="#ntpprimaryauthtype" title="NtpPrimaryAuthType">NtpPrimaryAuthType</a>: <i>String</i>
    <a href="#ntpprimarykeyid" title="NtpPrimaryKeyId">NtpPrimaryKeyId</a>: <i>Double</i>
    <a href="#ntpsecondaryaddress" title="NtpSecondaryAddress">NtpSecondaryAddress</a>: <i>String</i>
    <a href="#ntpsecondaryalgorithm" title="NtpSecondaryAlgorithm">NtpSecondaryAlgorithm</a>: <i>String</i>
    <a href="#ntpsecondaryauthkey" title="NtpSecondaryAuthKey">NtpSecondaryAuthKey</a>: <i>String</i>
    <a href="#ntpsecondaryauthtype" title="NtpSecondaryAuthType">NtpSecondaryAuthType</a>: <i>String</i>
    <a href="#ntpsecondarykeyid" title="NtpSecondaryKeyId">NtpSecondaryKeyId</a>: <i>Double</i>
    <a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>: <i>String</i>
    <a href="#proxyport" title="ProxyPort">ProxyPort</a>: <i>Double</i>
    <a href="#proxyserver" title="ProxyServer">ProxyServer</a>: <i>String</i>
    <a href="#proxyuser" title="ProxyUser">ProxyUser</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#updateserver" title="UpdateServer">UpdateServer</a>: <i>String</i>
    <a href="#verifyupdateserver" title="VerifyUpdateServer">VerifyUpdateServer</a>: <i>Boolean</i>
</pre>

## Properties

#### DnsPrimary

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSecondary

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAuthKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAuthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryKeyId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAuthKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAuthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryKeyId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyUpdateServer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ProxyPasswordEnc

Returns the &lt;code&gt;ProxyPasswordEnc&lt;/code&gt; value.

