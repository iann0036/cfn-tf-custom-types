# TF::Scaleway::LbCertificate LetsencryptDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
    "<a href="#subjectalternativename" title="SubjectAlternativeName">SubjectAlternativeName</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
<a href="#subjectalternativename" title="SubjectAlternativeName">SubjectAlternativeName</a>: <i>
      - String</i>
</pre>

## Properties

#### CommonName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeName

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

