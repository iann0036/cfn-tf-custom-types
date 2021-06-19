# TF::OCI::LoadBalancerBackendSet SslConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatename" title="CertificateName">CertificateName</a>" : <i>String</i>,
    "<a href="#ciphersuitename" title="CipherSuiteName">CipherSuiteName</a>" : <i>String</i>,
    "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#serverorderpreference" title="ServerOrderPreference">ServerOrderPreference</a>" : <i>String</i>,
    "<a href="#verifydepth" title="VerifyDepth">VerifyDepth</a>" : <i>Double</i>,
    "<a href="#verifypeercertificate" title="VerifyPeerCertificate">VerifyPeerCertificate</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#certificatename" title="CertificateName">CertificateName</a>: <i>String</i>
<a href="#ciphersuitename" title="CipherSuiteName">CipherSuiteName</a>: <i>String</i>
<a href="#protocols" title="Protocols">Protocols</a>: <i>
      - String</i>
<a href="#serverorderpreference" title="ServerOrderPreference">ServerOrderPreference</a>: <i>String</i>
<a href="#verifydepth" title="VerifyDepth">VerifyDepth</a>: <i>Double</i>
<a href="#verifypeercertificate" title="VerifyPeerCertificate">VerifyPeerCertificate</a>: <i>Boolean</i>
</pre>

## Properties

#### CertificateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherSuiteName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerOrderPreference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyDepth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyPeerCertificate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

