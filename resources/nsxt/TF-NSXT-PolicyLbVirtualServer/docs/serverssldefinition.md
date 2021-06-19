# TF::NSXT::PolicyLbVirtualServer ServerSslDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capaths" title="CaPaths">CaPaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>" : <i>Double</i>,
    "<a href="#clientcertificatepath" title="ClientCertificatePath">ClientCertificatePath</a>" : <i>String</i>,
    "<a href="#crlpaths" title="CrlPaths">CrlPaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#serverauth" title="ServerAuth">ServerAuth</a>" : <i>String</i>,
    "<a href="#sslprofilepath" title="SslProfilePath">SslProfilePath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#capaths" title="CaPaths">CaPaths</a>: <i>
      - String</i>
<a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>: <i>Double</i>
<a href="#clientcertificatepath" title="ClientCertificatePath">ClientCertificatePath</a>: <i>String</i>
<a href="#crlpaths" title="CrlPaths">CrlPaths</a>: <i>
      - String</i>
<a href="#serverauth" title="ServerAuth">ServerAuth</a>: <i>String</i>
<a href="#sslprofilepath" title="SslProfilePath">SslProfilePath</a>: <i>String</i>
</pre>

## Properties

#### CaPaths

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateChainDepth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificatePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlPaths

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAuth

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslProfilePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

