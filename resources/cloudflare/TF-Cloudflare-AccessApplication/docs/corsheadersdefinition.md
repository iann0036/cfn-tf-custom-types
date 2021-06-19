# TF::Cloudflare::AccessApplication CorsHeadersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowallheaders" title="AllowAllHeaders">AllowAllHeaders</a>" : <i>Boolean</i>,
    "<a href="#allowallmethods" title="AllowAllMethods">AllowAllMethods</a>" : <i>Boolean</i>,
    "<a href="#allowallorigins" title="AllowAllOrigins">AllowAllOrigins</a>" : <i>Boolean</i>,
    "<a href="#allowcredentials" title="AllowCredentials">AllowCredentials</a>" : <i>Boolean</i>,
    "<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxage" title="MaxAge">MaxAge</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowallheaders" title="AllowAllHeaders">AllowAllHeaders</a>: <i>Boolean</i>
<a href="#allowallmethods" title="AllowAllMethods">AllowAllMethods</a>: <i>Boolean</i>
<a href="#allowallorigins" title="AllowAllOrigins">AllowAllOrigins</a>: <i>Boolean</i>
<a href="#allowcredentials" title="AllowCredentials">AllowCredentials</a>: <i>Boolean</i>
<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>: <i>
      - String</i>
<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>
      - String</i>
<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>: <i>
      - String</i>
<a href="#maxage" title="MaxAge">MaxAge</a>: <i>Double</i>
</pre>

## Properties

#### AllowAllHeaders

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowAllMethods

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowAllOrigins

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowCredentials

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedHeaders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOrigins

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAge

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

