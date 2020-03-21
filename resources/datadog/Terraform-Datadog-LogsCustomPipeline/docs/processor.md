# Terraform::Datadog::LogsCustomPipeline Processor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>" : <i>[ &lt;a href=&#34;processor-arithmeticprocessor.md&#34;&gt;ArithmeticProcessor&lt;/a&gt;, ... ]</i>,
    "<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>" : <i>[ &lt;a href=&#34;processor-attributeremapper.md&#34;&gt;AttributeRemapper&lt;/a&gt;, ... ]</i>,
    "<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>" : <i>[ &lt;a href=&#34;processor-categoryprocessor.md&#34;&gt;CategoryProcessor&lt;/a&gt;, ... ]</i>,
    "<a href="#dateremapper" title="DateRemapper">DateRemapper</a>" : <i>[ &lt;a href=&#34;processor-dateremapper.md&#34;&gt;DateRemapper&lt;/a&gt;, ... ]</i>,
    "<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>" : <i>[ &lt;a href=&#34;processor-geoipparser.md&#34;&gt;GeoIpParser&lt;/a&gt;, ... ]</i>,
    "<a href="#grokparser" title="GrokParser">GrokParser</a>" : <i>[ &lt;a href=&#34;processor-grokparser.md&#34;&gt;GrokParser&lt;/a&gt;, ... ]</i>,
    "<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>" : <i>[ &lt;a href=&#34;processor-messageremapper.md&#34;&gt;MessageRemapper&lt;/a&gt;, ... ]</i>,
    "<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>" : <i>[ &lt;a href=&#34;processor-serviceremapper.md&#34;&gt;ServiceRemapper&lt;/a&gt;, ... ]</i>,
    "<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>" : <i>[ &lt;a href=&#34;processor-statusremapper.md&#34;&gt;StatusRemapper&lt;/a&gt;, ... ]</i>,
    "<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>" : <i>[ &lt;a href=&#34;processor-stringbuilderprocessor.md&#34;&gt;StringBuilderProcessor&lt;/a&gt;, ... ]</i>,
    "<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>" : <i>[ &lt;a href=&#34;processor-traceidremapper.md&#34;&gt;TraceIdRemapper&lt;/a&gt;, ... ]</i>,
    "<a href="#urlparser" title="UrlParser">UrlParser</a>" : <i>[ &lt;a href=&#34;processor-urlparser.md&#34;&gt;UrlParser&lt;/a&gt;, ... ]</i>,
    "<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>" : <i>[ &lt;a href=&#34;processor-useragentparser.md&#34;&gt;UserAgentParser&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>: <i>
      - &lt;a href=&#34;processor-arithmeticprocessor.md&#34;&gt;ArithmeticProcessor&lt;/a&gt;</i>
<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>: <i>
      - &lt;a href=&#34;processor-attributeremapper.md&#34;&gt;AttributeRemapper&lt;/a&gt;</i>
<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>: <i>
      - &lt;a href=&#34;processor-categoryprocessor.md&#34;&gt;CategoryProcessor&lt;/a&gt;</i>
<a href="#dateremapper" title="DateRemapper">DateRemapper</a>: <i>
      - &lt;a href=&#34;processor-dateremapper.md&#34;&gt;DateRemapper&lt;/a&gt;</i>
<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>: <i>
      - &lt;a href=&#34;processor-geoipparser.md&#34;&gt;GeoIpParser&lt;/a&gt;</i>
<a href="#grokparser" title="GrokParser">GrokParser</a>: <i>
      - &lt;a href=&#34;processor-grokparser.md&#34;&gt;GrokParser&lt;/a&gt;</i>
<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>: <i>
      - &lt;a href=&#34;processor-messageremapper.md&#34;&gt;MessageRemapper&lt;/a&gt;</i>
<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>: <i>
      - &lt;a href=&#34;processor-serviceremapper.md&#34;&gt;ServiceRemapper&lt;/a&gt;</i>
<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>: <i>
      - &lt;a href=&#34;processor-statusremapper.md&#34;&gt;StatusRemapper&lt;/a&gt;</i>
<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>: <i>
      - &lt;a href=&#34;processor-stringbuilderprocessor.md&#34;&gt;StringBuilderProcessor&lt;/a&gt;</i>
<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>: <i>
      - &lt;a href=&#34;processor-traceidremapper.md&#34;&gt;TraceIdRemapper&lt;/a&gt;</i>
<a href="#urlparser" title="UrlParser">UrlParser</a>: <i>
      - &lt;a href=&#34;processor-urlparser.md&#34;&gt;UrlParser&lt;/a&gt;</i>
<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>: <i>
      - &lt;a href=&#34;processor-useragentparser.md&#34;&gt;UserAgentParser&lt;/a&gt;</i>
</pre>

## Properties

#### ArithmeticProcessor

_Required_: No
_Type_: List of &lt;a href=&#34;processor-arithmeticprocessor.md&#34;&gt;ArithmeticProcessor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeRemapper

_Required_: No
_Type_: List of &lt;a href=&#34;processor-attributeremapper.md&#34;&gt;AttributeRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CategoryProcessor

_Required_: No
_Type_: List of &lt;a href=&#34;processor-categoryprocessor.md&#34;&gt;CategoryProcessor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRemapper

_Required_: No
_Type_: List of &lt;a href=&#34;processor-dateremapper.md&#34;&gt;DateRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoIpParser

_Required_: No
_Type_: List of &lt;a href=&#34;processor-geoipparser.md&#34;&gt;GeoIpParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokParser

_Required_: No
_Type_: List of &lt;a href=&#34;processor-grokparser.md&#34;&gt;GrokParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRemapper

_Required_: No
_Type_: List of &lt;a href=&#34;processor-messageremapper.md&#34;&gt;MessageRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRemapper

_Required_: No
_Type_: List of &lt;a href=&#34;processor-serviceremapper.md&#34;&gt;ServiceRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusRemapper

_Required_: No
_Type_: List of &lt;a href=&#34;processor-statusremapper.md&#34;&gt;StatusRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringBuilderProcessor

_Required_: No
_Type_: List of &lt;a href=&#34;processor-stringbuilderprocessor.md&#34;&gt;StringBuilderProcessor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceIdRemapper

_Required_: No
_Type_: List of &lt;a href=&#34;processor-traceidremapper.md&#34;&gt;TraceIdRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlParser

_Required_: No
_Type_: List of &lt;a href=&#34;processor-urlparser.md&#34;&gt;UrlParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgentParser

_Required_: No
_Type_: List of &lt;a href=&#34;processor-useragentparser.md&#34;&gt;UserAgentParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

