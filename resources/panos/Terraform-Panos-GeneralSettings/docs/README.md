# Terraform::Panos::GeneralSettings

This resource allows you to update the general device settings, such as DNS
or the hostname.

All params are optional for this resource.  If any options are not specified,
then whatever is already configured on the firewall is left as-is.  The
general device settings will always exist on the firewall, so `terraform
destroy` does not remove config from the firewall.

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

Primary DNS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSecondary

Secondary DNS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Firewall hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAddress

Primary NTP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAlgorithm

Primary NTP `symmetric-key` algorithm.  This can be
`sha1` or `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAuthKey

Primary NTP `symmetric-key` auth key.  This is the
SHA1 hash if the algorithm is `sha1`, or the md5sum if the algorithm is
`md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryAuthType

Primary NTP auth type.  This can be `none`,
`autokey`, or `symmetric-key`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpPrimaryKeyId

Primary NTP `symmetric-key` key ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAddress

Secondary NTP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAlgorithm

Secondary NTP `symmetric-key` algorithm.  This
can be `sha1` or `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAuthKey

Secondary NTP `symmetric-key` auth key.  This is
the SHA1 hash if the algorithm is `sha1`, or the md5sum if the algorithm is
`md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryAuthType

Secondary NTP auth type.  This can be `none`,
`autokey`, or `symmetric-key`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpSecondaryKeyId

Secondary NTP `symmetric-key` key ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPassword

Proxy's password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPort

Proxy's port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyServer

Specify a proxy server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

The timezone (e.g. - `US/Pacific`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateServer

The update server (Default: `updates.paloaltonetworks.com`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyUpdateServer

Verify update server identity (Default: `true`).

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

#### Id

Returns the <code>Id</code> value.

#### ProxyPasswordEnc

Returns the <code>ProxyPasswordEnc</code> value.

