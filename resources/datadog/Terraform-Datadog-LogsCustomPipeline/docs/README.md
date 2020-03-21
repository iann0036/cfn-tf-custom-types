# Terraform::Datadog::LogsCustomPipeline

CloudFormation equivalent of datadog_logs_custom_pipeline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::LogsCustomPipeline",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;, ... ]</i>,
        "<a href="#processor" title="Processor">Processor</a>" : <i>[ &lt;a href=&#34;processor.md&#34;&gt;Processor&lt;/a&gt;, ... ]</i>,
        "<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>" : <i>[ &lt;a href=&#34;arithmeticprocessor.md&#34;&gt;ArithmeticProcessor&lt;/a&gt;, ... ]</i>,
        "<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>" : <i>[ &lt;a href=&#34;attributeremapper.md&#34;&gt;AttributeRemapper&lt;/a&gt;, ... ]</i>,
        "<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>" : <i>[ &lt;a href=&#34;categoryprocessor.md&#34;&gt;CategoryProcessor&lt;/a&gt;, ... ]</i>,
        "<a href="#dateremapper" title="DateRemapper">DateRemapper</a>" : <i>[ &lt;a href=&#34;dateremapper.md&#34;&gt;DateRemapper&lt;/a&gt;, ... ]</i>,
        "<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>" : <i>[ &lt;a href=&#34;geoipparser.md&#34;&gt;GeoIpParser&lt;/a&gt;, ... ]</i>,
        "<a href="#grokparser" title="GrokParser">GrokParser</a>" : <i>[ &lt;a href=&#34;grokparser.md&#34;&gt;GrokParser&lt;/a&gt;, ... ]</i>,
        "<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>" : <i>[ &lt;a href=&#34;messageremapper.md&#34;&gt;MessageRemapper&lt;/a&gt;, ... ]</i>,
        "<a href="#pipeline" title="Pipeline">Pipeline</a>" : <i>[ &lt;a href=&#34;pipeline.md&#34;&gt;Pipeline&lt;/a&gt;, ... ]</i>,
        "<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>" : <i>[ &lt;a href=&#34;serviceremapper.md&#34;&gt;ServiceRemapper&lt;/a&gt;, ... ]</i>,
        "<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>" : <i>[ &lt;a href=&#34;statusremapper.md&#34;&gt;StatusRemapper&lt;/a&gt;, ... ]</i>,
        "<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>" : <i>[ &lt;a href=&#34;stringbuilderprocessor.md&#34;&gt;StringBuilderProcessor&lt;/a&gt;, ... ]</i>,
        "<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>" : <i>[ &lt;a href=&#34;traceidremapper.md&#34;&gt;TraceIdRemapper&lt;/a&gt;, ... ]</i>,
        "<a href="#urlparser" title="UrlParser">UrlParser</a>" : <i>[ &lt;a href=&#34;urlparser.md&#34;&gt;UrlParser&lt;/a&gt;, ... ]</i>,
        "<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>" : <i>[ &lt;a href=&#34;useragentparser.md&#34;&gt;UserAgentParser&lt;/a&gt;, ... ]</i>,
        "<a href="#category" title="Category">Category</a>" : <i>[ &lt;a href=&#34;category.md&#34;&gt;Category&lt;/a&gt;, ... ]</i>,
        "<a href="#grok" title="Grok">Grok</a>" : <i>[ &lt;a href=&#34;grok.md&#34;&gt;Grok&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::LogsCustomPipeline
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;</i>
    <a href="#processor" title="Processor">Processor</a>: <i>
      - &lt;a href=&#34;processor.md&#34;&gt;Processor&lt;/a&gt;</i>
    <a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>: <i>
      - &lt;a href=&#34;arithmeticprocessor.md&#34;&gt;ArithmeticProcessor&lt;/a&gt;</i>
    <a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>: <i>
      - &lt;a href=&#34;attributeremapper.md&#34;&gt;AttributeRemapper&lt;/a&gt;</i>
    <a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>: <i>
      - &lt;a href=&#34;categoryprocessor.md&#34;&gt;CategoryProcessor&lt;/a&gt;</i>
    <a href="#dateremapper" title="DateRemapper">DateRemapper</a>: <i>
      - &lt;a href=&#34;dateremapper.md&#34;&gt;DateRemapper&lt;/a&gt;</i>
    <a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>: <i>
      - &lt;a href=&#34;geoipparser.md&#34;&gt;GeoIpParser&lt;/a&gt;</i>
    <a href="#grokparser" title="GrokParser">GrokParser</a>: <i>
      - &lt;a href=&#34;grokparser.md&#34;&gt;GrokParser&lt;/a&gt;</i>
    <a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>: <i>
      - &lt;a href=&#34;messageremapper.md&#34;&gt;MessageRemapper&lt;/a&gt;</i>
    <a href="#pipeline" title="Pipeline">Pipeline</a>: <i>
      - &lt;a href=&#34;pipeline.md&#34;&gt;Pipeline&lt;/a&gt;</i>
    <a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>: <i>
      - &lt;a href=&#34;serviceremapper.md&#34;&gt;ServiceRemapper&lt;/a&gt;</i>
    <a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>: <i>
      - &lt;a href=&#34;statusremapper.md&#34;&gt;StatusRemapper&lt;/a&gt;</i>
    <a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>: <i>
      - &lt;a href=&#34;stringbuilderprocessor.md&#34;&gt;StringBuilderProcessor&lt;/a&gt;</i>
    <a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>: <i>
      - &lt;a href=&#34;traceidremapper.md&#34;&gt;TraceIdRemapper&lt;/a&gt;</i>
    <a href="#urlparser" title="UrlParser">UrlParser</a>: <i>
      - &lt;a href=&#34;urlparser.md&#34;&gt;UrlParser&lt;/a&gt;</i>
    <a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>: <i>
      - &lt;a href=&#34;useragentparser.md&#34;&gt;UserAgentParser&lt;/a&gt;</i>
    <a href="#category" title="Category">Category</a>: <i>
      - &lt;a href=&#34;category.md&#34;&gt;Category&lt;/a&gt;</i>
    <a href="#grok" title="Grok">Grok</a>: <i>
      - &lt;a href=&#34;grok.md&#34;&gt;Grok&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Processor

_Required_: No

_Type_: List of &lt;a href=&#34;processor.md&#34;&gt;Processor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArithmeticProcessor

_Required_: No

_Type_: List of &lt;a href=&#34;arithmeticprocessor.md&#34;&gt;ArithmeticProcessor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeRemapper

_Required_: No

_Type_: List of &lt;a href=&#34;attributeremapper.md&#34;&gt;AttributeRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CategoryProcessor

_Required_: No

_Type_: List of &lt;a href=&#34;categoryprocessor.md&#34;&gt;CategoryProcessor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRemapper

_Required_: No

_Type_: List of &lt;a href=&#34;dateremapper.md&#34;&gt;DateRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoIpParser

_Required_: No

_Type_: List of &lt;a href=&#34;geoipparser.md&#34;&gt;GeoIpParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokParser

_Required_: No

_Type_: List of &lt;a href=&#34;grokparser.md&#34;&gt;GrokParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRemapper

_Required_: No

_Type_: List of &lt;a href=&#34;messageremapper.md&#34;&gt;MessageRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pipeline

_Required_: No

_Type_: List of &lt;a href=&#34;pipeline.md&#34;&gt;Pipeline&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRemapper

_Required_: No

_Type_: List of &lt;a href=&#34;serviceremapper.md&#34;&gt;ServiceRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusRemapper

_Required_: No

_Type_: List of &lt;a href=&#34;statusremapper.md&#34;&gt;StatusRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringBuilderProcessor

_Required_: No

_Type_: List of &lt;a href=&#34;stringbuilderprocessor.md&#34;&gt;StringBuilderProcessor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceIdRemapper

_Required_: No

_Type_: List of &lt;a href=&#34;traceidremapper.md&#34;&gt;TraceIdRemapper&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlParser

_Required_: No

_Type_: List of &lt;a href=&#34;urlparser.md&#34;&gt;UrlParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgentParser

_Required_: No

_Type_: List of &lt;a href=&#34;useragentparser.md&#34;&gt;UserAgentParser&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

_Required_: No

_Type_: List of &lt;a href=&#34;category.md&#34;&gt;Category&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grok

_Required_: No

_Type_: List of &lt;a href=&#34;grok.md&#34;&gt;Grok&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

