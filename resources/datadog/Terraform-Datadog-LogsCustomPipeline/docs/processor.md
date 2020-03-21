# Terraform::Datadog::LogsCustomPipeline Processor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>" : <i>[ <a href="processor-arithmeticprocessor.md">ArithmeticProcessor</a>, ... ]</i>,
    "<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>" : <i>[ <a href="processor-attributeremapper.md">AttributeRemapper</a>, ... ]</i>,
    "<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>" : <i>[ <a href="processor-categoryprocessor.md">CategoryProcessor</a>, ... ]</i>,
    "<a href="#dateremapper" title="DateRemapper">DateRemapper</a>" : <i>[ <a href="processor-dateremapper.md">DateRemapper</a>, ... ]</i>,
    "<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>" : <i>[ <a href="processor-geoipparser.md">GeoIpParser</a>, ... ]</i>,
    "<a href="#grokparser" title="GrokParser">GrokParser</a>" : <i>[ <a href="processor-grokparser.md">GrokParser</a>, ... ]</i>,
    "<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>" : <i>[ <a href="processor-messageremapper.md">MessageRemapper</a>, ... ]</i>,
    "<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>" : <i>[ <a href="processor-serviceremapper.md">ServiceRemapper</a>, ... ]</i>,
    "<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>" : <i>[ <a href="processor-statusremapper.md">StatusRemapper</a>, ... ]</i>,
    "<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>" : <i>[ <a href="processor-stringbuilderprocessor.md">StringBuilderProcessor</a>, ... ]</i>,
    "<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>" : <i>[ <a href="processor-traceidremapper.md">TraceIdRemapper</a>, ... ]</i>,
    "<a href="#urlparser" title="UrlParser">UrlParser</a>" : <i>[ <a href="processor-urlparser.md">UrlParser</a>, ... ]</i>,
    "<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>" : <i>[ <a href="processor-useragentparser.md">UserAgentParser</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>: <i>
      - <a href="processor-arithmeticprocessor.md">ArithmeticProcessor</a></i>
<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>: <i>
      - <a href="processor-attributeremapper.md">AttributeRemapper</a></i>
<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>: <i>
      - <a href="processor-categoryprocessor.md">CategoryProcessor</a></i>
<a href="#dateremapper" title="DateRemapper">DateRemapper</a>: <i>
      - <a href="processor-dateremapper.md">DateRemapper</a></i>
<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>: <i>
      - <a href="processor-geoipparser.md">GeoIpParser</a></i>
<a href="#grokparser" title="GrokParser">GrokParser</a>: <i>
      - <a href="processor-grokparser.md">GrokParser</a></i>
<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>: <i>
      - <a href="processor-messageremapper.md">MessageRemapper</a></i>
<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>: <i>
      - <a href="processor-serviceremapper.md">ServiceRemapper</a></i>
<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>: <i>
      - <a href="processor-statusremapper.md">StatusRemapper</a></i>
<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>: <i>
      - <a href="processor-stringbuilderprocessor.md">StringBuilderProcessor</a></i>
<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>: <i>
      - <a href="processor-traceidremapper.md">TraceIdRemapper</a></i>
<a href="#urlparser" title="UrlParser">UrlParser</a>: <i>
      - <a href="processor-urlparser.md">UrlParser</a></i>
<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>: <i>
      - <a href="processor-useragentparser.md">UserAgentParser</a></i>
</pre>

## Properties

#### ArithmeticProcessor

_Required_: No
_Type_: List of <a href="processor-arithmeticprocessor.md">ArithmeticProcessor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeRemapper

_Required_: No
_Type_: List of <a href="processor-attributeremapper.md">AttributeRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CategoryProcessor

_Required_: No
_Type_: List of <a href="processor-categoryprocessor.md">CategoryProcessor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRemapper

_Required_: No
_Type_: List of <a href="processor-dateremapper.md">DateRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoIpParser

_Required_: No
_Type_: List of <a href="processor-geoipparser.md">GeoIpParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokParser

_Required_: No
_Type_: List of <a href="processor-grokparser.md">GrokParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRemapper

_Required_: No
_Type_: List of <a href="processor-messageremapper.md">MessageRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRemapper

_Required_: No
_Type_: List of <a href="processor-serviceremapper.md">ServiceRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusRemapper

_Required_: No
_Type_: List of <a href="processor-statusremapper.md">StatusRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringBuilderProcessor

_Required_: No
_Type_: List of <a href="processor-stringbuilderprocessor.md">StringBuilderProcessor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceIdRemapper

_Required_: No
_Type_: List of <a href="processor-traceidremapper.md">TraceIdRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlParser

_Required_: No
_Type_: List of <a href="processor-urlparser.md">UrlParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgentParser

_Required_: No
_Type_: List of <a href="processor-useragentparser.md">UserAgentParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

