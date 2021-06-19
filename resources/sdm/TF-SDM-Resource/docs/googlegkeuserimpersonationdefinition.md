# TF::SDM::Resource GoogleGkeUserImpersonationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>" : <i>String</i>,
    "<a href="#egressfilter" title="EgressFilter">EgressFilter</a>" : <i>String</i>,
    "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
    "<a href="#healthchecknamespace" title="HealthcheckNamespace">HealthcheckNamespace</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secretstorecertificateauthoritykey" title="SecretStoreCertificateAuthorityKey">SecretStoreCertificateAuthorityKey</a>" : <i>String</i>,
    "<a href="#secretstorecertificateauthoritypath" title="SecretStoreCertificateAuthorityPath">SecretStoreCertificateAuthorityPath</a>" : <i>String</i>,
    "<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>" : <i>String</i>,
    "<a href="#secretstoreserviceaccountkeykey" title="SecretStoreServiceAccountKeyKey">SecretStoreServiceAccountKeyKey</a>" : <i>String</i>,
    "<a href="#secretstoreserviceaccountkeypath" title="SecretStoreServiceAccountKeyPath">SecretStoreServiceAccountKeyPath</a>" : <i>String</i>,
    "<a href="#serviceaccountkey" title="ServiceAccountKey">ServiceAccountKey</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>: <i>String</i>
<a href="#egressfilter" title="EgressFilter">EgressFilter</a>: <i>String</i>
<a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
<a href="#healthchecknamespace" title="HealthcheckNamespace">HealthcheckNamespace</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secretstorecertificateauthoritykey" title="SecretStoreCertificateAuthorityKey">SecretStoreCertificateAuthorityKey</a>: <i>String</i>
<a href="#secretstorecertificateauthoritypath" title="SecretStoreCertificateAuthorityPath">SecretStoreCertificateAuthorityPath</a>: <i>String</i>
<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>: <i>String</i>
<a href="#secretstoreserviceaccountkeykey" title="SecretStoreServiceAccountKeyKey">SecretStoreServiceAccountKeyKey</a>: <i>String</i>
<a href="#secretstoreserviceaccountkeypath" title="SecretStoreServiceAccountKeyPath">SecretStoreServiceAccountKeyPath</a>: <i>String</i>
<a href="#serviceaccountkey" title="ServiceAccountKey">ServiceAccountKey</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### CertificateAuthority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckNamespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreCertificateAuthorityKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreCertificateAuthorityPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreServiceAccountKeyKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreServiceAccountKeyPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

