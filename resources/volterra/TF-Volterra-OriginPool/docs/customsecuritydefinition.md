# TF::Volterra::OriginPool CustomSecurityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxversion" title="MaxVersion">MaxVersion</a>" : <i>String</i>,
    "<a href="#minversion" title="MinVersion">MinVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>: <i>
      - String</i>
<a href="#maxversion" title="MaxVersion">MaxVersion</a>: <i>String</i>
<a href="#minversion" title="MinVersion">MinVersion</a>: <i>String</i>
</pre>

## Properties

#### CipherSuites

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

