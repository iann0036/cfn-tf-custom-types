# TF::AVI::Virtualservice ContentRewriteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#requestrewriteenabled" title="RequestRewriteEnabled">RequestRewriteEnabled</a>" : <i>Boolean</i>,
    "<a href="#responserewriteenabled" title="ResponseRewriteEnabled">ResponseRewriteEnabled</a>" : <i>Boolean</i>,
    "<a href="#rewritablecontentref" title="RewritableContentRef">RewritableContentRef</a>" : <i>String</i>,
    "<a href="#reqmatchreplacepair" title="ReqMatchReplacePair">ReqMatchReplacePair</a>" : <i>[ <a href="reqmatchreplacepairdefinition.md">ReqMatchReplacePairDefinition</a>, ... ]</i>,
    "<a href="#rspmatchreplacepair" title="RspMatchReplacePair">RspMatchReplacePair</a>" : <i>[ <a href="rspmatchreplacepairdefinition.md">RspMatchReplacePairDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#requestrewriteenabled" title="RequestRewriteEnabled">RequestRewriteEnabled</a>: <i>Boolean</i>
<a href="#responserewriteenabled" title="ResponseRewriteEnabled">ResponseRewriteEnabled</a>: <i>Boolean</i>
<a href="#rewritablecontentref" title="RewritableContentRef">RewritableContentRef</a>: <i>String</i>
<a href="#reqmatchreplacepair" title="ReqMatchReplacePair">ReqMatchReplacePair</a>: <i>
      - <a href="reqmatchreplacepairdefinition.md">ReqMatchReplacePairDefinition</a></i>
<a href="#rspmatchreplacepair" title="RspMatchReplacePair">RspMatchReplacePair</a>: <i>
      - <a href="rspmatchreplacepairdefinition.md">RspMatchReplacePairDefinition</a></i>
</pre>

## Properties

#### RequestRewriteEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseRewriteEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewritableContentRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReqMatchReplacePair

_Required_: No

_Type_: List of <a href="reqmatchreplacepairdefinition.md">ReqMatchReplacePairDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RspMatchReplacePair

_Required_: No

_Type_: List of <a href="rspmatchreplacepairdefinition.md">RspMatchReplacePairDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

