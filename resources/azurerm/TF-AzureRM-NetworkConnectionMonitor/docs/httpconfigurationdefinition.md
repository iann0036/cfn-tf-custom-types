# TF::AzureRM::NetworkConnectionMonitor HttpConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#preferhttps" title="PreferHttps">PreferHttps</a>" : <i>Boolean</i>,
    "<a href="#validstatuscoderanges" title="ValidStatusCodeRanges">ValidStatusCodeRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#requestheader" title="RequestHeader">RequestHeader</a>" : <i>[ <a href="requestheaderdefinition.md">RequestHeaderDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#preferhttps" title="PreferHttps">PreferHttps</a>: <i>Boolean</i>
<a href="#validstatuscoderanges" title="ValidStatusCodeRanges">ValidStatusCodeRanges</a>: <i>
      - String</i>
<a href="#requestheader" title="RequestHeader">RequestHeader</a>: <i>
      - <a href="requestheaderdefinition.md">RequestHeaderDefinition</a></i>
</pre>

## Properties

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferHttps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidStatusCodeRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeader

_Required_: No

_Type_: List of <a href="requestheaderdefinition.md">RequestHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

