# TF::Kubernetes::CertificateSigningRequest SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#request" title="Request">Request</a>" : <i>String</i>,
    "<a href="#signername" title="SignerName">SignerName</a>" : <i>String</i>,
    "<a href="#usages" title="Usages">Usages</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#request" title="Request">Request</a>: <i>String</i>
<a href="#signername" title="SignerName">SignerName</a>: <i>String</i>
<a href="#usages" title="Usages">Usages</a>: <i>
      - String</i>
</pre>

## Properties

#### Request

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usages

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

