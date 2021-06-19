# TF::AVI::Sslkeyandcertificate KeyParamsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
    "<a href="#ecparams" title="EcParams">EcParams</a>" : <i>[ <a href="ecparamsdefinition.md">EcParamsDefinition</a>, ... ]</i>,
    "<a href="#rsaparams" title="RsaParams">RsaParams</a>" : <i>[ <a href="rsaparamsdefinition.md">RsaParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
<a href="#ecparams" title="EcParams">EcParams</a>: <i>
      - <a href="ecparamsdefinition.md">EcParamsDefinition</a></i>
<a href="#rsaparams" title="RsaParams">RsaParams</a>: <i>
      - <a href="rsaparamsdefinition.md">RsaParamsDefinition</a></i>
</pre>

## Properties

#### Algorithm

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcParams

_Required_: No

_Type_: List of <a href="ecparamsdefinition.md">EcParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RsaParams

_Required_: No

_Type_: List of <a href="rsaparamsdefinition.md">RsaParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

