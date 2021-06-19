# TF::Volterra::HttpLoadbalancer TrustedClientsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>Double</i>,
    "<a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>" : <i>String</i>,
    "<a href="#ipprefix" title="IpPrefix">IpPrefix</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#asnumber" title="AsNumber">AsNumber</a>: <i>Double</i>
<a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>: <i>String</i>
<a href="#ipprefix" title="IpPrefix">IpPrefix</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
</pre>

## Properties

#### AsNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationTimestamp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

