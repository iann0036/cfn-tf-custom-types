# TF::Alicloud::OssBucket CorsRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#exposeheaders" title="ExposeHeaders">ExposeHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxageseconds" title="MaxAgeSeconds">MaxAgeSeconds</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>: <i>
      - String</i>
<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>
      - String</i>
<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>: <i>
      - String</i>
<a href="#exposeheaders" title="ExposeHeaders">ExposeHeaders</a>: <i>
      - String</i>
<a href="#maxageseconds" title="MaxAgeSeconds">MaxAgeSeconds</a>: <i>Double</i>
</pre>

## Properties

#### AllowedHeaders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOrigins

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposeHeaders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAgeSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

