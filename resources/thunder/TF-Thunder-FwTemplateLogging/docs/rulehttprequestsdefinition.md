# TF::Thunder::FwTemplateLogging RuleHttpRequestsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablesequencecheck" title="DisableSequenceCheck">DisableSequenceCheck</a>" : <i>Double</i>,
    "<a href="#includeallheaders" title="IncludeAllHeaders">IncludeAllHeaders</a>" : <i>Double</i>,
    "<a href="#logeveryhttprequest" title="LogEveryHttpRequest">LogEveryHttpRequest</a>" : <i>Double</i>,
    "<a href="#maxurllen" title="MaxUrlLen">MaxUrlLen</a>" : <i>Double</i>,
    "<a href="#destport" title="DestPort">DestPort</a>" : <i>[ <a href="destportdefinition.md">DestPortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablesequencecheck" title="DisableSequenceCheck">DisableSequenceCheck</a>: <i>Double</i>
<a href="#includeallheaders" title="IncludeAllHeaders">IncludeAllHeaders</a>: <i>Double</i>
<a href="#logeveryhttprequest" title="LogEveryHttpRequest">LogEveryHttpRequest</a>: <i>Double</i>
<a href="#maxurllen" title="MaxUrlLen">MaxUrlLen</a>: <i>Double</i>
<a href="#destport" title="DestPort">DestPort</a>: <i>
      - <a href="destportdefinition.md">DestPortDefinition</a></i>
</pre>

## Properties

#### DisableSequenceCheck

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeAllHeaders

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogEveryHttpRequest

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUrlLen

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestPort

_Required_: No

_Type_: List of <a href="destportdefinition.md">DestPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

