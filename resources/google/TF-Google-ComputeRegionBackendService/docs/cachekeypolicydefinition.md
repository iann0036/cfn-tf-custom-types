# TF::Google::ComputeRegionBackendService CacheKeyPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#includehost" title="IncludeHost">IncludeHost</a>" : <i>Boolean</i>,
    "<a href="#includeprotocol" title="IncludeProtocol">IncludeProtocol</a>" : <i>Boolean</i>,
    "<a href="#includequerystring" title="IncludeQueryString">IncludeQueryString</a>" : <i>Boolean</i>,
    "<a href="#querystringblacklist" title="QueryStringBlacklist">QueryStringBlacklist</a>" : <i>[ String, ... ]</i>,
    "<a href="#querystringwhitelist" title="QueryStringWhitelist">QueryStringWhitelist</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#includehost" title="IncludeHost">IncludeHost</a>: <i>Boolean</i>
<a href="#includeprotocol" title="IncludeProtocol">IncludeProtocol</a>: <i>Boolean</i>
<a href="#includequerystring" title="IncludeQueryString">IncludeQueryString</a>: <i>Boolean</i>
<a href="#querystringblacklist" title="QueryStringBlacklist">QueryStringBlacklist</a>: <i>
      - String</i>
<a href="#querystringwhitelist" title="QueryStringWhitelist">QueryStringWhitelist</a>: <i>
      - String</i>
</pre>

## Properties

#### IncludeHost

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeProtocol

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeQueryString

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryStringBlacklist

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryStringWhitelist

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

