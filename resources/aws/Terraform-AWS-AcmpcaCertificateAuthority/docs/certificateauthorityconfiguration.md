# Terraform::AWS::AcmpcaCertificateAuthority CertificateAuthorityConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>" : <i>String</i>,
    "<a href="#signingalgorithm" title="SigningAlgorithm">SigningAlgorithm</a>" : <i>String</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>[ &lt;a href=&#34;certificateauthorityconfiguration-subject.md&#34;&gt;Subject&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>: <i>String</i>
<a href="#signingalgorithm" title="SigningAlgorithm">SigningAlgorithm</a>: <i>String</i>
<a href="#subject" title="Subject">Subject</a>: <i>
      - &lt;a href=&#34;certificateauthorityconfiguration-subject.md&#34;&gt;Subject&lt;/a&gt;</i>
</pre>

## Properties

#### KeyAlgorithm

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SigningAlgorithm

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No
_Type_: List of &lt;a href=&#34;certificateauthorityconfiguration-subject.md&#34;&gt;Subject&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

