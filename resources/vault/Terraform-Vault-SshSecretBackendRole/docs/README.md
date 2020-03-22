# Terraform::Vault::SshSecretBackendRole

Provides a resource to manage roles in an SSH secret backend
[SSH secret backend within Vault](https://www.vaultproject.io/docs/secrets/ssh/index.html).

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
        "<a href="#alloweduserkeylengths" title="AllowedUserKeyLengths">AllowedUserKeyLengths</a>" : <i>[ <a href="alloweduserkeylengths.md">AllowedUserKeyLengths</a>, ... ]</i>,
        "<a href="#allowedusers" title="AllowedUsers">AllowedUsers</a>" : <i>String</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#cidrlist" title="CidrList">CidrList</a>" : <i>String</i>,
        "<a href="#defaultcriticaloptions" title="DefaultCriticalOptions">DefaultCriticalOptions</a>" : <i>[ <a href="defaultcriticaloptions.md">DefaultCriticalOptions</a>, ... ]</i>,
        "<a href="#defaultextensions" title="DefaultExtensions">DefaultExtensions</a>" : <i>[ <a href="defaultextensions.md">DefaultExtensions</a>, ... ]</i>,
        "<a href="#defaultuser" title="DefaultUser">DefaultUser</a>" : <i>String</i>,
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
      - <a href="alloweduserkeylengths.md">AllowedUserKeyLengths</a></i>
    <a href="#allowedusers" title="AllowedUsers">AllowedUsers</a>: <i>String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#cidrlist" title="CidrList">CidrList</a>: <i>String</i>
    <a href="#defaultcriticaloptions" title="DefaultCriticalOptions">DefaultCriticalOptions</a>: <i>
      - <a href="defaultcriticaloptions.md">DefaultCriticalOptions</a></i>
    <a href="#defaultextensions" title="DefaultExtensions">DefaultExtensions</a>: <i>
      - <a href="defaultextensions.md">DefaultExtensions</a></i>
    <a href="#defaultuser" title="DefaultUser">DefaultUser</a>: <i>String</i>
    <a href="#keyidformat" title="KeyIdFormat">KeyIdFormat</a>: <i>String</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
</pre>

## Properties

#### AllowBareDomains

Specifies if host certificates that are requested are allowed to use the base domains listed in `allowed_domains`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowHostCertificates

Specifies if certificates are allowed to be signed for use as a 'host'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSubdomains

Specifies if host certificates that are requested are allowed to be subdomains of those listed in `allowed_domains`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUserCertificates

Specifies if certificates are allowed to be signed for use as a 'user'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUserKeyIds

Specifies if users can override the key ID for a signed certificate with the `key_id` field.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedCriticalOptions

Specifies a comma-separated list of critical options that certificates can have when signed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedDomains

The list of domains for which a client can request a host certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedExtensions

Specifies a comma-separated list of extensions that certificates can have when signed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUserKeyLengths

Specifies a map of ssh key types and their expected sizes which are allowed to be signed by the CA type.

_Required_: No

_Type_: List of <a href="alloweduserkeylengths.md">AllowedUserKeyLengths</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUsers

Specifies a comma-separated list of usernames that are to be allowed, only if certain usernames are to be allowed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

The path where the SSH secret backend is mounted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrList

The comma-separated string of CIDR blocks for which this role is applicable.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCriticalOptions

Specifies a map of critical options that certificates have when signed.

_Required_: No

_Type_: List of <a href="defaultcriticaloptions.md">DefaultCriticalOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultExtensions

Specifies a map of extensions that certificates have when signed.

_Required_: No

_Type_: List of <a href="defaultextensions.md">DefaultExtensions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultUser

Specifies the default username for which a credential will be generated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyIdFormat

Specifies a custom format for the key id of a signed certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

Specifies the type of credentials generated by this role. This can be either `otp`, `dynamic` or `ca`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

Specifies the maximum Time To Live value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the role to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Specifies the Time To Live value.

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

