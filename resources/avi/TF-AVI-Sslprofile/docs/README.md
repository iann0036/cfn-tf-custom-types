# TF::AVI::Sslprofile

The SSLProfile resource allows the creation and management of Avi SSLProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Sslprofile",
    "Properties" : {
        "<a href="#acceptedciphers" title="AcceptedCiphers">AcceptedCiphers</a>" : <i>String</i>,
        "<a href="#cipherenums" title="CipherEnums">CipherEnums</a>" : <i>[ String, ... ]</i>,
        "<a href="#ciphersuites" title="Ciphersuites">Ciphersuites</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhparam" title="Dhparam">Dhparam</a>" : <i>String</i>,
        "<a href="#enableearlydata" title="EnableEarlyData">EnableEarlyData</a>" : <i>Boolean</i>,
        "<a href="#enablesslsessionreuse" title="EnableSslSessionReuse">EnableSslSessionReuse</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preferclientcipherordering" title="PreferClientCipherOrdering">PreferClientCipherOrdering</a>" : <i>Boolean</i>,
        "<a href="#sendclosenotify" title="SendCloseNotify">SendCloseNotify</a>" : <i>Boolean</i>,
        "<a href="#sslsessiontimeout" title="SslSessionTimeout">SslSessionTimeout</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#acceptedversions" title="AcceptedVersions">AcceptedVersions</a>" : <i>[ <a href="acceptedversionsdefinition.md">AcceptedVersionsDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#sslrating" title="SslRating">SslRating</a>" : <i>[ <a href="sslratingdefinition.md">SslRatingDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Sslprofile
Properties:
    <a href="#acceptedciphers" title="AcceptedCiphers">AcceptedCiphers</a>: <i>String</i>
    <a href="#cipherenums" title="CipherEnums">CipherEnums</a>: <i>
      - String</i>
    <a href="#ciphersuites" title="Ciphersuites">Ciphersuites</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhparam" title="Dhparam">Dhparam</a>: <i>String</i>
    <a href="#enableearlydata" title="EnableEarlyData">EnableEarlyData</a>: <i>Boolean</i>
    <a href="#enablesslsessionreuse" title="EnableSslSessionReuse">EnableSslSessionReuse</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#preferclientcipherordering" title="PreferClientCipherOrdering">PreferClientCipherOrdering</a>: <i>Boolean</i>
    <a href="#sendclosenotify" title="SendCloseNotify">SendCloseNotify</a>: <i>Boolean</i>
    <a href="#sslsessiontimeout" title="SslSessionTimeout">SslSessionTimeout</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#acceptedversions" title="AcceptedVersions">AcceptedVersions</a>: <i>
      - <a href="acceptedversionsdefinition.md">AcceptedVersionsDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#sslrating" title="SslRating">SslRating</a>: <i>
      - <a href="sslratingdefinition.md">SslRatingDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### AcceptedCiphers

Ciphers suites represented as defined by https //www.openssl.org/docs/apps/ciphers.html.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherEnums

Enum options - tls_ecdhe_ecdsa_with_aes_128_gcm_sha256, tls_ecdhe_ecdsa_with_aes_256_gcm_sha384, tls_ecdhe_rsa_with_aes_128_gcm_sha256, tls_ecdhe_rsa_with_aes_256_gcm_sha384, tls_ecdhe_ecdsa_with_aes_128_cbc_sha256, tls_ecdhe_ecdsa_with_aes_256_cbc_sha384, tls_ecdhe_rsa_with_aes_128_cbc_sha256, tls_ecdhe_rsa_with_aes_256_cbc_sha384, tls_rsa_with_aes_128_gcm_sha256, tls_rsa_with_aes_256_gcm_sha384, tls_rsa_with_aes_128_cbc_sha256, tls_rsa_with_aes_256_cbc_sha256, tls_ecdhe_ecdsa_with_aes_128_cbc_sha, tls_ecdhe_ecdsa_with_aes_256_cbc_sha, tls_ecdhe_rsa_with_aes_128_cbc_sha, tls_ecdhe_rsa_with_aes_256_cbc_sha, tls_rsa_with_aes_128_cbc_sha, tls_rsa_with_aes_256_cbc_sha, tls_rsa_with_3des_ede_cbc_sha, tls_aes_256_gcm_sha384... Allowed in basic(allowed values- tls_ecdhe_ecdsa_with_aes_128_gcm_sha256,tls_ecdhe_ecdsa_with_aes_256_gcm_sha384,tls_ecdhe_rsa_with_aes_128_gcm_sha256,tls_ecdhe_rsa_with_aes_256_gcm_sha384,tls_ecdhe_ecdsa_with_aes_128_cbc_sha256,tls_ecdhe_ecdsa_with_aes_256_cbc_sha384,tls_ecdhe_rsa_with_aes_128_cbc_sha256,tls_ecdhe_rsa_with_aes_256_cbc_sha384,tls_rsa_with_aes_128_gcm_sha256,tls_rsa_with_aes_256_gcm_sha384,tls_rsa_with_aes_128_cbc_sha256,tls_rsa_with_aes_256_cbc_sha256,tls_ecdhe_ecdsa_with_aes_128_cbc_sha,tls_ecdhe_ecdsa_with_aes_256_cbc_sha,tls_ecdhe_rsa_with_aes_128_cbc_sha,tls_ecdhe_rsa_with_aes_256_cbc_sha,tls_rsa_with_aes_128_cbc_sha,tls_rsa_with_aes_256_cbc_sha,tls_rsa_with_3des_ede_cbc_sha) edition, essentials(allowed values- tls_ecdhe_ecdsa_with_aes_128_gcm_sha256,tls_ecdhe_ecdsa_with_aes_256_gcm_sha384,tls_ecdhe_rsa_with_aes_128_gcm_sha256,tls_ecdhe_rsa_with_aes_256_gcm_sha384,tls_ecdhe_ecdsa_with_aes_128_cbc_sha256,tls_ecdhe_ecdsa_with_aes_256_cbc_sha384,tls_ecdhe_rsa_with_aes_128_cbc_sha256,tls_ecdhe_rsa_with_aes_256_cbc_sha384,tls_rsa_with_aes_128_gcm_sha256,tls_rsa_with_aes_256_gcm_sha384,tls_rsa_with_aes_128_cbc_sha256,tls_rsa_with_aes_256_cbc_sha256,tls_ecdhe_ecdsa_with_aes_128_cbc_sha,tls_ecdhe_ecdsa_with_aes_256_cbc_sha,tls_ecdhe_rsa_with_aes_128_cbc_sha,tls_ecdhe_rsa_with_aes_256_cbc_sha,tls_rsa_with_aes_128_cbc_sha,tls_rsa_with_aes_256_cbc_sha,tls_rsa_with_3des_ede_cbc_sha) edition, enterprise edition.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ciphersuites

Tls 1.3 ciphers suites represented as defined by u(https //www.openssl.org/docs/manmaster/man1/ciphers.html). Field introduced in 18.2.6. Allowed in basic edition, essentials edition, enterprise edition. Special default for basic edition is tls_aes_256_gcm_sha384-tls_aes_128_gcm_sha256, essentials edition is tls_aes_256_gcm_sha384-tls_aes_128_gcm_sha256, enterprise is tls_aes_256_gcm_sha384-tls_chacha20_poly1305_sha256-tls_aes_128_gcm_sha256.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhparam

Dh parameters used in ssl. At this time, it is not configurable and is set to 2048 bits.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEarlyData

Enable early data processing for tls1.3 connections. Field introduced in 18.2.6. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSslSessionReuse

Enable ssl session re-use.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferClientCipherOrdering

Prefer the ssl cipher ordering presented by the client during the ssl handshake over the one specified in the ssl profile.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCloseNotify

Send 'close notify' alert message for a clean shutdown of the ssl connection.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSessionTimeout

The amount of time in seconds before an ssl session expires. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Ssl profile type. Enum options - SSL_PROFILE_TYPE_APPLICATION, SSL_PROFILE_TYPE_SYSTEM. Field introduced in 17.2.8.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcceptedVersions

_Required_: No

_Type_: List of <a href="acceptedversionsdefinition.md">AcceptedVersionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslRating

_Required_: No

_Type_: List of <a href="sslratingdefinition.md">SslRatingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

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

