# TF::SDM::Resource AksUserImpersonationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>" : <i>String</i>,
    "<a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>" : <i>String</i>,
    "<a href="#clientkey" title="ClientKey">ClientKey</a>" : <i>String</i>,
    "<a href="#egressfilter" title="EgressFilter">EgressFilter</a>" : <i>String</i>,
    "<a href="#healthchecknamespace" title="HealthcheckNamespace">HealthcheckNamespace</a>" : <i>String</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#secretstorecertificateauthoritykey" title="SecretStoreCertificateAuthorityKey">SecretStoreCertificateAuthorityKey</a>" : <i>String</i>,
    "<a href="#secretstorecertificateauthoritypath" title="SecretStoreCertificateAuthorityPath">SecretStoreCertificateAuthorityPath</a>" : <i>String</i>,
    "<a href="#secretstoreclientcertificatekey" title="SecretStoreClientCertificateKey">SecretStoreClientCertificateKey</a>" : <i>String</i>,
    "<a href="#secretstoreclientcertificatepath" title="SecretStoreClientCertificatePath">SecretStoreClientCertificatePath</a>" : <i>String</i>,
    "<a href="#secretstoreclientkeykey" title="SecretStoreClientKeyKey">SecretStoreClientKeyKey</a>" : <i>String</i>,
    "<a href="#secretstoreclientkeypath" title="SecretStoreClientKeyPath">SecretStoreClientKeyPath</a>" : <i>String</i>,
    "<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>: <i>String</i>
<a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>: <i>String</i>
<a href="#clientkey" title="ClientKey">ClientKey</a>: <i>String</i>
<a href="#egressfilter" title="EgressFilter">EgressFilter</a>: <i>String</i>
<a href="#healthchecknamespace" title="HealthcheckNamespace">HealthcheckNamespace</a>: <i>String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#secretstorecertificateauthoritykey" title="SecretStoreCertificateAuthorityKey">SecretStoreCertificateAuthorityKey</a>: <i>String</i>
<a href="#secretstorecertificateauthoritypath" title="SecretStoreCertificateAuthorityPath">SecretStoreCertificateAuthorityPath</a>: <i>String</i>
<a href="#secretstoreclientcertificatekey" title="SecretStoreClientCertificateKey">SecretStoreClientCertificateKey</a>: <i>String</i>
<a href="#secretstoreclientcertificatepath" title="SecretStoreClientCertificatePath">SecretStoreClientCertificatePath</a>: <i>String</i>
<a href="#secretstoreclientkeykey" title="SecretStoreClientKeyKey">SecretStoreClientKeyKey</a>: <i>String</i>
<a href="#secretstoreclientkeypath" title="SecretStoreClientKeyPath">SecretStoreClientKeyPath</a>: <i>String</i>
<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### CertificateAuthority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckNamespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreCertificateAuthorityKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreCertificateAuthorityPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreClientCertificateKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreClientCertificatePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreClientKeyKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreClientKeyPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
