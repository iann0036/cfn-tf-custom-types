# Terraform::Datadog::Dashboard Request

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#q" title="Q">Q</a>" : <i>String</i>,
    "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ <a href="request-apmquery.md">ApmQuery</a>, ... ]</i>,
    "<a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>" : <i>[ <a href="request-conditionalformats.md">ConditionalFormats</a>, ... ]</i>,
    "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ <a href="request-logquery.md">LogQuery</a>, ... ]</i>,
    "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ <a href="request-processquery.md">ProcessQuery</a>, ... ]</i>,
    "<a href="#style" title="Style">Style</a>" : <i>[ <a href="request-style.md">Style</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#q" title="Q">Q</a>: <i>String</i>
<a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - <a href="request-apmquery.md">ApmQuery</a></i>
<a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>: <i>
      - <a href="request-conditionalformats.md">ConditionalFormats</a></i>
<a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - <a href="request-logquery.md">LogQuery</a></i>
<a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - <a href="request-processquery.md">ProcessQuery</a></i>
<a href="#style" title="Style">Style</a>: <i>
      - <a href="request-style.md">Style</a></i>
</pre>

## Properties

#### Q

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No

_Type_: List of <a href="request-apmquery.md">ApmQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormats

_Required_: No

_Type_: List of <a href="request-conditionalformats.md">ConditionalFormats</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No

_Type_: List of <a href="request-logquery.md">LogQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of <a href="request-processquery.md">ProcessQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No

_Type_: List of <a href="request-style.md">Style</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

