# TF::Spotinst::MultaiListener TlsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateids" title="CertificateIds">CertificateIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxversion" title="MaxVersion">MaxVersion</a>" : <i>String</i>,
    "<a href="#minversion" title="MinVersion">MinVersion</a>" : <i>String</i>,
    "<a href="#preferserverciphersuites" title="PreferServerCipherSuites">PreferServerCipherSuites</a>" : <i>Boolean</i>,
    "<a href="#sessionticketsdisabled" title="SessionTicketsDisabled">SessionTicketsDisabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#certificateids" title="CertificateIds">CertificateIds</a>: <i>
      - String</i>
<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>: <i>
      - String</i>
<a href="#maxversion" title="MaxVersion">MaxVersion</a>: <i>String</i>
<a href="#minversion" title="MinVersion">MinVersion</a>: <i>String</i>
<a href="#preferserverciphersuites" title="PreferServerCipherSuites">PreferServerCipherSuites</a>: <i>Boolean</i>
<a href="#sessionticketsdisabled" title="SessionTicketsDisabled">SessionTicketsDisabled</a>: <i>Boolean</i>
</pre>

## Properties

#### CertificateIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherSuites

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferServerCipherSuites

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTicketsDisabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

