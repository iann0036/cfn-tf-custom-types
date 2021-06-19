# TF::Volterra::VirtualHost CommonParamsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>" : <i>[ String, ... ]</i>,
    "<a href="#maximumprotocolversion" title="MaximumProtocolVersion">MaximumProtocolVersion</a>" : <i>String</i>,
    "<a href="#minimumprotocolversion" title="MinimumProtocolVersion">MinimumProtocolVersion</a>" : <i>String</i>,
    "<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>" : <i>String</i>,
    "<a href="#tlscertificates" title="TlsCertificates">TlsCertificates</a>" : <i>[ <a href="tlscertificatesdefinition.md">TlsCertificatesDefinition</a>, ... ]</i>,
    "<a href="#validationparams" title="ValidationParams">ValidationParams</a>" : <i>[ <a href="validationparamsdefinition.md">ValidationParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>: <i>
      - String</i>
<a href="#maximumprotocolversion" title="MaximumProtocolVersion">MaximumProtocolVersion</a>: <i>String</i>
<a href="#minimumprotocolversion" title="MinimumProtocolVersion">MinimumProtocolVersion</a>: <i>String</i>
<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>: <i>String</i>
<a href="#tlscertificates" title="TlsCertificates">TlsCertificates</a>: <i>
      - <a href="tlscertificatesdefinition.md">TlsCertificatesDefinition</a></i>
<a href="#validationparams" title="ValidationParams">ValidationParams</a>: <i>
      - <a href="validationparamsdefinition.md">ValidationParamsDefinition</a></i>
</pre>

## Properties

#### CipherSuites

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumProtocolVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumProtocolVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedCaUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsCertificates

_Required_: No

_Type_: List of <a href="tlscertificatesdefinition.md">TlsCertificatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidationParams

_Required_: No

_Type_: List of <a href="validationparamsdefinition.md">ValidationParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

