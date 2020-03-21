# Terraform::Datadog::LogsCustomPipeline

CloudFormation equivalent of datadog_logs_custom_pipeline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::LogsCustomPipeline",
    "Properties" : {
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>,
        "<a href="#processor" title="Processor">Processor</a>" : <i>[ <a href="processor.md">Processor</a>, ... ]</i>,
        "<a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>" : <i>[ <a href="arithmeticprocessor.md">ArithmeticProcessor</a>, ... ]</i>,
        "<a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>" : <i>[ <a href="attributeremapper.md">AttributeRemapper</a>, ... ]</i>,
        "<a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>" : <i>[ <a href="categoryprocessor.md">CategoryProcessor</a>, ... ]</i>,
        "<a href="#dateremapper" title="DateRemapper">DateRemapper</a>" : <i>[ <a href="dateremapper.md">DateRemapper</a>, ... ]</i>,
        "<a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>" : <i>[ <a href="geoipparser.md">GeoIpParser</a>, ... ]</i>,
        "<a href="#grokparser" title="GrokParser">GrokParser</a>" : <i>[ <a href="grokparser.md">GrokParser</a>, ... ]</i>,
        "<a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>" : <i>[ <a href="messageremapper.md">MessageRemapper</a>, ... ]</i>,
        "<a href="#pipeline" title="Pipeline">Pipeline</a>" : <i>[ <a href="pipeline.md">Pipeline</a>, ... ]</i>,
        "<a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>" : <i>[ <a href="serviceremapper.md">ServiceRemapper</a>, ... ]</i>,
        "<a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>" : <i>[ <a href="statusremapper.md">StatusRemapper</a>, ... ]</i>,
        "<a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>" : <i>[ <a href="stringbuilderprocessor.md">StringBuilderProcessor</a>, ... ]</i>,
        "<a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>" : <i>[ <a href="traceidremapper.md">TraceIdRemapper</a>, ... ]</i>,
        "<a href="#urlparser" title="UrlParser">UrlParser</a>" : <i>[ <a href="urlparser.md">UrlParser</a>, ... ]</i>,
        "<a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>" : <i>[ <a href="useragentparser.md">UserAgentParser</a>, ... ]</i>,
        "<a href="#category" title="Category">Category</a>" : <i>[ <a href="category.md">Category</a>, ... ]</i>,
        "<a href="#grok" title="Grok">Grok</a>" : <i>[ <a href="grok.md">Grok</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::LogsCustomPipeline
Properties:
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
    <a href="#processor" title="Processor">Processor</a>: <i>
      - <a href="processor.md">Processor</a></i>
    <a href="#arithmeticprocessor" title="ArithmeticProcessor">ArithmeticProcessor</a>: <i>
      - <a href="arithmeticprocessor.md">ArithmeticProcessor</a></i>
    <a href="#attributeremapper" title="AttributeRemapper">AttributeRemapper</a>: <i>
      - <a href="attributeremapper.md">AttributeRemapper</a></i>
    <a href="#categoryprocessor" title="CategoryProcessor">CategoryProcessor</a>: <i>
      - <a href="categoryprocessor.md">CategoryProcessor</a></i>
    <a href="#dateremapper" title="DateRemapper">DateRemapper</a>: <i>
      - <a href="dateremapper.md">DateRemapper</a></i>
    <a href="#geoipparser" title="GeoIpParser">GeoIpParser</a>: <i>
      - <a href="geoipparser.md">GeoIpParser</a></i>
    <a href="#grokparser" title="GrokParser">GrokParser</a>: <i>
      - <a href="grokparser.md">GrokParser</a></i>
    <a href="#messageremapper" title="MessageRemapper">MessageRemapper</a>: <i>
      - <a href="messageremapper.md">MessageRemapper</a></i>
    <a href="#pipeline" title="Pipeline">Pipeline</a>: <i>
      - <a href="pipeline.md">Pipeline</a></i>
    <a href="#serviceremapper" title="ServiceRemapper">ServiceRemapper</a>: <i>
      - <a href="serviceremapper.md">ServiceRemapper</a></i>
    <a href="#statusremapper" title="StatusRemapper">StatusRemapper</a>: <i>
      - <a href="statusremapper.md">StatusRemapper</a></i>
    <a href="#stringbuilderprocessor" title="StringBuilderProcessor">StringBuilderProcessor</a>: <i>
      - <a href="stringbuilderprocessor.md">StringBuilderProcessor</a></i>
    <a href="#traceidremapper" title="TraceIdRemapper">TraceIdRemapper</a>: <i>
      - <a href="traceidremapper.md">TraceIdRemapper</a></i>
    <a href="#urlparser" title="UrlParser">UrlParser</a>: <i>
      - <a href="urlparser.md">UrlParser</a></i>
    <a href="#useragentparser" title="UserAgentParser">UserAgentParser</a>: <i>
      - <a href="useragentparser.md">UserAgentParser</a></i>
    <a href="#category" title="Category">Category</a>: <i>
      - <a href="category.md">Category</a></i>
    <a href="#grok" title="Grok">Grok</a>: <i>
      - <a href="grok.md">Grok</a></i>
</pre>

## Properties

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

_Type_: List of <a href="filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Processor

_Required_: No

_Type_: List of <a href="processor.md">Processor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArithmeticProcessor

_Required_: No

_Type_: List of <a href="arithmeticprocessor.md">ArithmeticProcessor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeRemapper

_Required_: No

_Type_: List of <a href="attributeremapper.md">AttributeRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CategoryProcessor

_Required_: No

_Type_: List of <a href="categoryprocessor.md">CategoryProcessor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRemapper

_Required_: No

_Type_: List of <a href="dateremapper.md">DateRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoIpParser

_Required_: No

_Type_: List of <a href="geoipparser.md">GeoIpParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokParser

_Required_: No

_Type_: List of <a href="grokparser.md">GrokParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRemapper

_Required_: No

_Type_: List of <a href="messageremapper.md">MessageRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pipeline

_Required_: No

_Type_: List of <a href="pipeline.md">Pipeline</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRemapper

_Required_: No

_Type_: List of <a href="serviceremapper.md">ServiceRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusRemapper

_Required_: No

_Type_: List of <a href="statusremapper.md">StatusRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringBuilderProcessor

_Required_: No

_Type_: List of <a href="stringbuilderprocessor.md">StringBuilderProcessor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceIdRemapper

_Required_: No

_Type_: List of <a href="traceidremapper.md">TraceIdRemapper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlParser

_Required_: No

_Type_: List of <a href="urlparser.md">UrlParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgentParser

_Required_: No

_Type_: List of <a href="useragentparser.md">UserAgentParser</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

_Required_: No

_Type_: List of <a href="category.md">Category</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grok

_Required_: No

_Type_: List of <a href="grok.md">Grok</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

