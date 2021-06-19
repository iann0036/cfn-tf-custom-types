# TF::Turbot::SamlDirectory

The `Turbot SAML Directory` resource adds support for creating SAML directories. It is used to create and delete directory settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::SamlDirectory",
    "Properties" : {
        "<a href="#allowgroupsyncing" title="AllowGroupSyncing">AllowGroupSyncing</a>" : <i>Boolean</i>,
        "<a href="#allowidpinitiatedsso" title="AllowIdpInitiatedSso">AllowIdpInitiatedSso</a>" : <i>Boolean</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#entrypoint" title="EntryPoint">EntryPoint</a>" : <i>String</i>,
        "<a href="#groupfilter" title="GroupFilter">GroupFilter</a>" : <i>String</i>,
        "<a href="#groupidtemplate" title="GroupIdTemplate">GroupIdTemplate</a>" : <i>String</i>,
        "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
        "<a href="#nameidformat" title="NameIdFormat">NameIdFormat</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#poolid" title="PoolId">PoolId</a>" : <i>String</i>,
        "<a href="#profilegroupsattribute" title="ProfileGroupsAttribute">ProfileGroupsAttribute</a>" : <i>String</i>,
        "<a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>" : <i>String</i>,
        "<a href="#signrequests" title="SignRequests">SignRequests</a>" : <i>String</i>,
        "<a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>" : <i>String</i>,
        "<a href="#signatureprivatekey" title="SignaturePrivateKey">SignaturePrivateKey</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::SamlDirectory
Properties:
    <a href="#allowgroupsyncing" title="AllowGroupSyncing">AllowGroupSyncing</a>: <i>Boolean</i>
    <a href="#allowidpinitiatedsso" title="AllowIdpInitiatedSso">AllowIdpInitiatedSso</a>: <i>Boolean</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#entrypoint" title="EntryPoint">EntryPoint</a>: <i>String</i>
    <a href="#groupfilter" title="GroupFilter">GroupFilter</a>: <i>String</i>
    <a href="#groupidtemplate" title="GroupIdTemplate">GroupIdTemplate</a>: <i>String</i>
    <a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
    <a href="#nameidformat" title="NameIdFormat">NameIdFormat</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#poolid" title="PoolId">PoolId</a>: <i>String</i>
    <a href="#profilegroupsattribute" title="ProfileGroupsAttribute">ProfileGroupsAttribute</a>: <i>String</i>
    <a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>: <i>String</i>
    <a href="#signrequests" title="SignRequests">SignRequests</a>: <i>String</i>
    <a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>: <i>String</i>
    <a href="#signatureprivatekey" title="SignaturePrivateKey">SignaturePrivateKey</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### AllowGroupSyncing

Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIdpInitiatedSso

Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

The public key certificate ([base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) ) which provides SAML entry point access
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through this directory. For example, email id of the user.
- `issuer` - (Optional) a URL that uniquely identifies your SAML identity provider.
- `name_id_format` - (Optional) The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Brief description of the purpose and details of the directory.
- `entry_point` - (Required) Defines the identity provider single sign-on URL.
- `certificate` - (Required) The public key certificate ([base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) ) which provides SAML entry point access
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through this directory. For example, email id of the user.
- `issuer` - (Optional) a URL that uniquely identifies your SAML identity provider.
- `name_id_format` - (Optional) The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryPoint

Defines the identity provider single sign-on URL.
- `certificate` - (Required) The public key certificate ([base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) ) which provides SAML entry point access
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through this directory. For example, email id of the user.
- `issuer` - (Optional) a URL that uniquely identifies your SAML identity provider.
- `name_id_format` - (Optional) The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupFilter

Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupIdTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

a URL that uniquely identifies your SAML identity provider.
- `name_id_format` - (Optional) The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameIdFormat

The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

The `id` or `aka` of the level at which the SAML directory will be created.
- `title` - (Required) Short descriptive name for the saml directory. This appears as the saml directory name in the Turbot Console.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `entry_point` - (Required) Defines the identity provider single sign-on URL.
- `certificate` - (Required) The public key certificate ([base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) ) which provides SAML entry point access
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through this directory. For example, email id of the user.
- `issuer` - (Optional) a URL that uniquely identifies your SAML identity provider.
- `name_id_format` - (Optional) The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileGroupsAttribute

Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileIdTemplate

A template to generate profile id for users authenticated through this directory. For example, email id of the user.
- `issuer` - (Optional) a URL that uniquely identifies your SAML identity provider.
- `name_id_format` - (Optional) The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignRequests

Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureAlgorithm

If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignaturePrivateKey

Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

User defined label for grouping resources.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Short descriptive name for the saml directory. This appears as the saml directory name in the Turbot Console.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `entry_point` - (Required) Defines the identity provider single sign-on URL.
- `certificate` - (Required) The public key certificate ([base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) ) which provides SAML entry point access
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through this directory. For example, email id of the user.
- `issuer` - (Optional) a URL that uniquely identifies your SAML identity provider.
- `name_id_format` - (Optional) The name identifier format to request from the identity provider. Usually the Email Address is the accepted format.It accepts one of the two values - `UNSPECIFIED` and `EMAIL`. Defaults to `UNSPECIFIED`
- `sign_requests` - (Optional) Signing request for SAML authentication. It accepts one of the two values - `Enabled` and `Disabled`. If enabled, requests will be signed using the specified private key and signature algorithm.
- `signature_private_key` - (Optional) Private key used to sign authentication requests, in multiline PEM format starting with -----BEGIN PRIVATE KEY-----.
- `signature_algorithm` - (Optional) If a private key has been provided, it determines the signature algorithm for signing requests. If not specified defaults to *SHA-1*.
- `allow_group_syncing` -  (Optional) Boolean value to indicate whether groups will be synchronized for SAML users. Defaults to `false`.
- `allow_idp_initiated_sso` -  (Optional) Boolean value to indicate whether directory allows IDP-initiated SSO. Defaults to `false`.
- `profile_groups_attribute` - (Optional) Attribute returning list of groups that a SAML user is a part of.
- `group_filter` -  (Optional) Regular expression to filter out groups that are to be synced from SAML.
- `tags` - (Optional) User defined label for grouping resources.

_Required_: Yes

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

#### DirectoryType

Returns the <code>DirectoryType</code> value.

#### Id

Returns the <code>Id</code> value.

#### ParentAkas

Returns the <code>ParentAkas</code> value.

#### Status

Returns the <code>Status</code> value.

