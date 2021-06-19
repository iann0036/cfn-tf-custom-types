# TF::Datadog::SyntheticsTest RequestClientCertificateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cert" title="Cert">Cert</a>" : <i>[ <a href="certdefinition.md">CertDefinition</a>, ... ]</i>,
    "<a href="#key" title="Key">Key</a>" : <i>[ <a href="keydefinition.md">KeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cert" title="Cert">Cert</a>: <i>
      - <a href="certdefinition.md">CertDefinition</a></i>
<a href="#key" title="Key">Key</a>: <i>
      - <a href="keydefinition.md">KeyDefinition</a></i>
</pre>

## Properties

#### Cert

_Required_: No

_Type_: List of <a href="certdefinition.md">CertDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: List of <a href="keydefinition.md">KeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

