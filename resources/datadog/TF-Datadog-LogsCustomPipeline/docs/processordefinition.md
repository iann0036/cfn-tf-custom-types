# TF::Datadog::LogsCustomPipeline ProcessorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>" : <i>[ <a href="arithmeticprocessordefinition.md">ArithmeticProcessorDefinition</a>, ... ]</i>,
    "<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>" : <i>[ <a href="attributeremapperdefinition.md">AttributeRemapperDefinition</a>, ... ]</i>,
    "<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>" : <i>[ <a href="categoryprocessordefinition.md">CategoryProcessorDefinition</a>, ... ]</i>,
    "<a href="#dateremapper" title="DateRemapper">DateRemapper</a>" : <i>[ <a href="dateremapperdefinition.md">DateRemapperDefinition</a>, ... ]</i>,
    "<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>" : <i>[ <a href="geoipparserdefinition.md">GeoIpParserDefinition</a>, ... ]</i>,
    "<a href="#grokparser" title="GrokParser">GrokParser</a>" : <i>[ <a href="grokparserdefinition.md">GrokParserDefinition</a>, ... ]</i>,
    "<a href="#lookupprocessor" title="LookupProcessor">LookupProcessor</a>" : <i>[ <a href="lookupprocessordefinition.md">LookupProcessorDefinition</a>, ... ]</i>,
    "<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>" : <i>[ <a href="messageremapperdefinition.md">MessageRemapperDefinition</a>, ... ]</i>,
    "<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>" : <i>[ <a href="serviceremapperdefinition.md">ServiceRemapperDefinition</a>, ... ]</i>,
    "<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>" : <i>[ <a href="statusremapperdefinition.md">StatusRemapperDefinition</a>, ... ]</i>,
    "<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>" : <i>[ <a href="stringbuilderprocessordefinition.md">StringBuilderProcessorDefinition</a>, ... ]</i>,
    "<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>" : <i>[ <a href="traceidremapperdefinition.md">TraceIdRemapperDefinition</a>, ... ]</i>,
    "<a href="#urlparser" title="UrlParser">UrlParser</a>" : <i>[ <a href="urlparserdefinition.md">UrlParserDefinition</a>, ... ]</i>,
    "<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>" : <i>[ <a href="useragentparserdefinition.md">UserAgentParserDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>: <i>
      - <a href="arithmeticprocessordefinition.md">ArithmeticProcessorDefinition</a></i>
<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>: <i>
      - <a href="attributeremapperdefinition.md">AttributeRemapperDefinition</a></i>
<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>: <i>
      - <a href="categoryprocessordefinition.md">CategoryProcessorDefinition</a></i>
<a href="#dateremapper" title="DateRemapper">DateRemapper</a>: <i>
      - <a href="dateremapperdefinition.md">DateRemapperDefinition</a></i>
<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>: <i>
      - <a href="geoipparserdefinition.md">GeoIpParserDefinition</a></i>
<a href="#grokparser" title="GrokParser">GrokParser</a>: <i>
      - <a href="grokparserdefinition.md">GrokParserDefinition</a></i>
<a href="#lookupprocessor" title="LookupProcessor">LookupProcessor</a>: <i>
      - <a href="lookupprocessordefinition.md">LookupProcessorDefinition</a></i>
<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>: <i>
      - <a href="messageremapperdefinition.md">MessageRemapperDefinition</a></i>
<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>: <i>
      - <a href="serviceremapperdefinition.md">ServiceRemapperDefinition</a></i>
<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>: <i>
      - <a href="statusremapperdefinition.md">StatusRemapperDefinition</a></i>
<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>: <i>
      - <a href="stringbuilderprocessordefinition.md">StringBuilderProcessorDefinition</a></i>
<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>: <i>
      - <a href="traceidremapperdefinition.md">TraceIdRemapperDefinition</a></i>
<a href="#urlparser" title="UrlParser">UrlParser</a>: <i>
      - <a href="urlparserdefinition.md">UrlParserDefinition</a></i>
<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>: <i>
      - <a href="useragentparserdefinition.md">UserAgentParserDefinition</a></i>
</pre>

## Properties

#### ArithmeticProcessor

_Required_: No

_Type_: List of <a href="arithmeticprocessordefinition.md">ArithmeticProcessorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeRemapper

_Required_: No

_Type_: List of <a href="attributeremapperdefinition.md">AttributeRemapperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CategoryProcessor

_Required_: No

_Type_: List of <a href="categoryprocessordefinition.md">CategoryProcessorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRemapper

_Required_: No

_Type_: List of <a href="dateremapperdefinition.md">DateRemapperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoIpParser

_Required_: No

_Type_: List of <a href="geoipparserdefinition.md">GeoIpParserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokParser

_Required_: No

_Type_: List of <a href="grokparserdefinition.md">GrokParserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LookupProcessor

_Required_: No

_Type_: List of <a href="lookupprocessordefinition.md">LookupProcessorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRemapper

_Required_: No

_Type_: List of <a href="messageremapperdefinition.md">MessageRemapperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRemapper

_Required_: No

_Type_: List of <a href="serviceremapperdefinition.md">ServiceRemapperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusRemapper

_Required_: No

_Type_: List of <a href="statusremapperdefinition.md">StatusRemapperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringBuilderProcessor

_Required_: No

_Type_: List of <a href="stringbuilderprocessordefinition.md">StringBuilderProcessorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceIdRemapper

_Required_: No

_Type_: List of <a href="traceidremapperdefinition.md">TraceIdRemapperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlParser

_Required_: No

_Type_: List of <a href="urlparserdefinition.md">UrlParserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgentParser

_Required_: No

_Type_: List of <a href="useragentparserdefinition.md">UserAgentParserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

