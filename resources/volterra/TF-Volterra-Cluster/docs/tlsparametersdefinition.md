# TF::Volterra::Cluster TlsParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablesni" title="DisableSni">DisableSni</a>" : <i>Boolean</i>,
    "<a href="#sni" title="Sni">Sni</a>" : <i>String</i>,
    "<a href="#usehostheaderassni" title="UseHostHeaderAsSni">UseHostHeaderAsSni</a>" : <i>Boolean</i>,
    "<a href="#commonparams" title="CommonParams">CommonParams</a>" : <i>[ <a href="commonparamsdefinition.md">CommonParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablesni" title="DisableSni">DisableSni</a>: <i>Boolean</i>
<a href="#sni" title="Sni">Sni</a>: <i>String</i>
<a href="#usehostheaderassni" title="UseHostHeaderAsSni">UseHostHeaderAsSni</a>: <i>Boolean</i>
<a href="#commonparams" title="CommonParams">CommonParams</a>: <i>
      - <a href="commonparamsdefinition.md">CommonParamsDefinition</a></i>
</pre>

## Properties

#### DisableSni

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sni

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseHostHeaderAsSni

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonParams

_Required_: No

_Type_: List of <a href="commonparamsdefinition.md">CommonParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

