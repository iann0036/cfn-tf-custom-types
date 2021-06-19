# TF::Volterra::HttpLoadbalancer TlsParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nomtls" title="NoMtls">NoMtls</a>" : <i>Boolean</i>,
    "<a href="#tlscertificates" title="TlsCertificates">TlsCertificates</a>" : <i>[ <a href="tlscertificatesdefinition.md">TlsCertificatesDefinition</a>, ... ]</i>,
    "<a href="#tlsconfig" title="TlsConfig">TlsConfig</a>" : <i>[ <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>, ... ]</i>,
    "<a href="#usemtls" title="UseMtls">UseMtls</a>" : <i>[ <a href="usemtlsdefinition.md">UseMtlsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nomtls" title="NoMtls">NoMtls</a>: <i>Boolean</i>
<a href="#tlscertificates" title="TlsCertificates">TlsCertificates</a>: <i>
      - <a href="tlscertificatesdefinition.md">TlsCertificatesDefinition</a></i>
<a href="#tlsconfig" title="TlsConfig">TlsConfig</a>: <i>
      - <a href="tlsconfigdefinition.md">TlsConfigDefinition</a></i>
<a href="#usemtls" title="UseMtls">UseMtls</a>: <i>
      - <a href="usemtlsdefinition.md">UseMtlsDefinition</a></i>
</pre>

## Properties

#### NoMtls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsCertificates

_Required_: No

_Type_: List of <a href="tlscertificatesdefinition.md">TlsCertificatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsConfig

_Required_: No

_Type_: List of <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMtls

_Required_: No

_Type_: List of <a href="usemtlsdefinition.md">UseMtlsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

