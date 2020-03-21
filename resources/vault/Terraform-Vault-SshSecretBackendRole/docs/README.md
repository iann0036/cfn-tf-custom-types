# Terraform::Vault::SshSecretBackendRole

CloudFormation equivalent of vault_ssh_secret_backend_role

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::SshSecretBackendRole",
    "Properties" : {
        "<a href="#allowbaredomains" title="AllowBareDomains">AllowBareDomains</a>" : <i>Boolean</i>,
        "<a href="#allowhostcertificates" title="AllowHostCertificates">AllowHostCertificates</a>" : <i>Boolean</i>,
        "<a href="#allowsubdomains" title="AllowSubdomains">AllowSubdomains</a>" : <i>Boolean</i>,
        "<a href="#allowusercertificates" title="AllowUserCertificates">AllowUserCertificates</a>" : <i>Boolean</i>,
        "<a href="#allowuserkeyids" title="AllowUserKeyIds">AllowUserKeyIds</a>" : <i>Boolean</i>,
        "<a href="#allowedcriticaloptions" title="AllowedCriticalOptions">AllowedCriticalOptions</a>" : <i>String</i>,
        "<a href="#alloweddomains" title="AllowedDomains">AllowedDomains</a>" : <i>String</i>,
        "<a href="#allowedextensions" title="AllowedExtensions">AllowedExtensions</a>" : <i>String</i>,
        "<a href="#alloweduserkeylengths" title="AllowedUserKeyLengths">AllowedUserKeyLengths</a>" : <i>[ &lt;a href=&#34;alloweduserkeylengths.md&#34;&gt;AllowedUserKeyLengths&lt;/a&gt;, ... ]</i>,
        "<a href="#allowedusers" title="AllowedUsers">AllowedUsers</a>" : <i>String</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#cidrlist" title="CidrList">CidrList</a>" : <i>String</i>,
        "<a href="#defaultcriticaloptions" title="DefaultCriticalOptions">DefaultCriticalOptions</a>" : <i>[ &lt;a href=&#34;defaultcriticaloptions.md&#34;&gt;DefaultCriticalOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultextensions" title="DefaultExtensions">DefaultExtensions</a>" : <i>[ &lt;a href=&#34;defaultextensions.md&#34;&gt;DefaultExtensions&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultuser" title="DefaultUser">DefaultUser</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#keyidformat" title="KeyIdFormat">KeyIdFormat</a>" : <i>String</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::SshSecretBackendRole
Properties:
    <a href="#allowbaredomains" title="AllowBareDomains">AllowBareDomains</a>: <i>Boolean</i>
    <a href="#allowhostcertificates" title="AllowHostCertificates">AllowHostCertificates</a>: <i>Boolean</i>
    <a href="#allowsubdomains" title="AllowSubdomains">AllowSubdomains</a>: <i>Boolean</i>
    <a href="#allowusercertificates" title="AllowUserCertificates">AllowUserCertificates</a>: <i>Boolean</i>
    <a href="#allowuserkeyids" title="AllowUserKeyIds">AllowUserKeyIds</a>: <i>Boolean</i>
    <a href="#allowedcriticaloptions" title="AllowedCriticalOptions">AllowedCriticalOptions</a>: <i>String</i>
    <a href="#alloweddomains" title="AllowedDomains">AllowedDomains</a>: <i>String</i>
    <a href="#allowedextensions" title="AllowedExtensions">AllowedExtensions</a>: <i>String</i>
    <a href="#alloweduserkeylengths" title="AllowedUserKeyLengths">AllowedUserKeyLengths</a>: <i>
      - &lt;a href=&#34;alloweduserkeylengths.md&#34;&gt;AllowedUserKeyLengths&lt;/a&gt;</i>
    <a href="#allowedusers" title="AllowedUsers">AllowedUsers</a>: <i>String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#cidrlist" title="CidrList">CidrList</a>: <i>String</i>
    <a href="#defaultcriticaloptions" title="DefaultCriticalOptions">DefaultCriticalOptions</a>: <i>
      - &lt;a href=&#34;defaultcriticaloptions.md&#34;&gt;DefaultCriticalOptions&lt;/a&gt;</i>
    <a href="#defaultextensions" title="DefaultExtensions">DefaultExtensions</a>: <i>
      - &lt;a href=&#34;defaultextensions.md&#34;&gt;DefaultExtensions&lt;/a&gt;</i>
    <a href="#defaultuser" title="DefaultUser">DefaultUser</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#keyidformat" title="KeyIdFormat">KeyIdFormat</a>: <i>String</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
</pre>

## Properties

#### AllowBareDomains

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowHostCertificates

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSubdomains

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUserCertificates

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUserKeyIds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedCriticalOptions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedDomains

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedExtensions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUserKeyLengths

_Required_: No

_Type_: List of &lt;a href=&#34;alloweduserkeylengths.md&#34;&gt;AllowedUserKeyLengths&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUsers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrList

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCriticalOptions

_Required_: No

_Type_: List of &lt;a href=&#34;defaultcriticaloptions.md&#34;&gt;DefaultCriticalOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultExtensions

_Required_: No

_Type_: List of &lt;a href=&#34;defaultextensions.md&#34;&gt;DefaultExtensions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyIdFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

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

